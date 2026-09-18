from playwright.sync_api import sync_playwright
import json, re
from pathlib import Path

ROOT='http://127.0.0.1:8765/'
SITE=Path('/Users/laina/.hermes/profiles/sales/workspace/liuyun-technology')
raw_page_data=(SITE/'site-data.js').read_text(encoding='utf-8')
page_data=json.loads(raw_page_data.split('=',1)[1].rsplit(';',1)[0].strip())
paths=['index.html'] + sorted({v['path'] for v in page_data.values()})
results=[]
with sync_playwright() as p:
    b=p.chromium.launch(headless=True,executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
    c=b.new_context(viewport={'width':1440,'height':1000})
    page=c.new_page(); console=[]; failed=[]
    page.on('console',lambda msg: console.append({'type':msg.type,'text':msg.text,'url':page.url}))
    page.on('requestfailed',lambda req: failed.append({'url':req.url,'error':req.failure}))
    for path in paths:
        console.clear(); failed.clear()
        try:
            page.goto(ROOT+path,wait_until='networkidle',timeout=60000)
            page.wait_for_timeout(350)
            benign_media_aborts=[x for x in failed if x.get('error')=='net::ERR_ABORTED' and any(x['url'].lower().endswith(ext) for ext in ('.mp4','.webp','.gif','.png'))]
            unexpected_failed=[x for x in failed if x not in benign_media_aborts]
            result={
              'path':path,'url':page.url,'title':page.title(),'status_text':page.locator('body').inner_text()[:300],
              'subpage':page.locator('body.subpage').count()==1,'case_cards':page.locator('.subpage-case-card').count(),
              'has_nav':page.locator('.site-nav').count()==1,'has_footer':page.locator('.site-footer').count()==1,
              'nav_signature':' '.join(page.locator('.site-nav').inner_text().split()),'dropdown_count':page.locator('.nav-dropdown').count(),
              'console_errors':[x for x in console if x['type']=='error'],'failed_requests':unexpected_failed,'benign_media_aborts':benign_media_aborts
            }
            if path in ('index.html','web_path.html'):
                dropdown=page.locator('.nav-dropdown').first
                dropdown.hover(); page.wait_for_timeout(80)
                result['website_dropdown_visible']=dropdown.locator('.nav-dropdown-panel').is_visible()
                result['website_dropdown_items']=dropdown.locator('.nav-dropdown-link').all_inner_texts()
            if path=='web_path.html':
                h=page.locator('#page-title').bounding_box(); preview=page.locator('#page-hero-preview').bounding_box()
                result['hero_overlap']=bool(h and preview and h['x'] < preview['x']+preview['width'] and h['x']+h['width'] > preview['x'] and h['y'] < preview['y']+preview['height'] and h['y']+h['height'] > preview['y'])
                page.locator('.subpage-case-card').first.click(); page.wait_for_timeout(150)
                result['modal_open']=page.locator('#subpage-modal.is-open').count()==1
                page.locator('.subpage-modal-close').click(); result['modal_closed']=page.locator('#subpage-modal.is-open').count()==0
            results.append(result)
        except Exception as e:
            results.append({'path':path,'error':type(e).__name__+': '+str(e)[:500]})
    # Mobile menu + responsive check on a page route.
    c.close(); c=b.new_context(viewport={'width':390,'height':844}); m=c.new_page(); m.goto(ROOT+'shop_path.html',wait_until='networkidle',timeout=60000); m.wait_for_timeout(300)
    mobile={'path':'shop_path.html','menu_before':m.locator('#site-nav.is-open').count(),'cards':m.locator('.subpage-case-card').count()}
    m.locator('.menu-toggle').click(); mobile['menu_after']=m.locator('#site-nav.is-open').count(); mobile['aria']=m.locator('.menu-toggle').get_attribute('aria-expanded')
    m.locator('.nav-dropdown-toggle').first.click(); mobile['dropdown_after']=m.locator('.nav-dropdown.is-open').count(); mobile['dropdown_items']=m.locator('.nav-dropdown.is-open .nav-dropdown-link').count(); mobile['menu_after_dropdown']=m.locator('#site-nav.is-open').count(); results.append({'mobile':mobile})
    b.close()

route_results=[x for x in results if x.get('path')]
signatures={x.get('nav_signature') for x in route_results}
expected_signature=next(iter(signatures),None)
structural_errors=[x for x in route_results if x.get('nav_signature') != expected_signature or x.get('dropdown_count') != 3 or x.get('website_dropdown_visible') is False or x.get('hero_overlap') is True]
summary={
 'route_count':len(paths),'results':results,'nav_signatures':len(signatures),'structural_errors':structural_errors,
 'routes_ok':sum(1 for x in route_results if not x.get('error') and not x.get('console_errors') and not x.get('failed_requests') and x not in structural_errors),
 'errors':[x for x in route_results if x.get('error') or x.get('console_errors') or x.get('failed_requests')] + structural_errors,
}
(SITE/'multipage_verification.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'route_count':summary['route_count'],'routes_ok':summary['routes_ok'],'errors':len(summary['errors']),'mobile':next((x['mobile'] for x in results if 'mobile' in x),None)},ensure_ascii=False))
