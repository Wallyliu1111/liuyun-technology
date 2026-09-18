from playwright.sync_api import sync_playwright
import json, os

ROOT='http://127.0.0.1:8765/'
OUT='/Users/laina/.hermes/profiles/sales/workspace/liuyun-technology'
result={}
with sync_playwright() as p:
    browser=p.chromium.launch(headless=True, executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', args=['--disable-blink-features=AutomationControlled'])

    def run_context(name, viewport, reduced=False):
        context=browser.new_context(viewport=viewport, reduced_motion='reduce' if reduced else 'no-preference')
        page=context.new_page()
        console=[]; failed=[]
        page.on('console', lambda msg: console.append({'type':msg.type,'text':msg.text}))
        page.on('requestfailed', lambda req: failed.append({'url':req.url,'error':req.failure}))
        page.goto(ROOT, wait_until='networkidle', timeout=60000)
        page.wait_for_timeout(1200)
        # Reveal scroll-triggered sections before taking the full-page artifact screenshot.
        for _ in range(18):
            page.evaluate('window.scrollBy(0, Math.max(700, window.innerHeight * 0.85))')
            page.wait_for_timeout(120)
        page.evaluate('window.scrollTo(0, 0)')
        page.wait_for_timeout(300)
        page.screenshot(path=f'{OUT}/{name}.png', full_page=True)
        benign_media_aborts=[x for x in failed if x.get('error')=='net::ERR_ABORTED' and any(x['url'].lower().endswith(ext) for ext in ('.mp4','.webp','.gif','.png'))]
        unexpected_failed=[x for x in failed if x not in benign_media_aborts]
        summary={
          'title':page.title(),
          'body_text_head':page.locator('body').inner_text()[:900],
          'case_cards_initial':page.locator('.case-card').count(),
          'hero_cards':page.locator('.hero-card').count(),
          'visible_videos':page.locator('video').count(),
          'failed_requests':unexpected_failed,
          'benign_media_aborts':benign_media_aborts,
          'console_errors':[x for x in console if x['type']=='error'],
          'screenshot':f'{OUT}/{name}.png'
        }
        if not reduced:
            # Filter interaction
            page.locator('.filter-button[data-filter="食品餐旅"]').click()
            page.wait_for_timeout(250)
            summary['case_cards_cloud']=page.locator('.case-card').count()
            summary['filter_active']=page.locator('.filter-button.is-active').inner_text()
            # Modal interaction
            page.locator('.case-card').first.click()
            page.wait_for_timeout(200)
            summary['modal_open']=page.locator('#case-modal.is-open').count()==1
            summary['modal_title']=page.locator('#modal-title').inner_text()
            page.locator('.modal-close').click()
            summary['modal_closed']=page.locator('#case-modal.is-open').count()==0
        else:
            summary['reduced_motion_reveals']=page.locator('[data-reveal].is-in').count()
        context.close()
        return summary

    result['desktop']=run_context('verification-desktop', {'width':1440,'height':1000})
    result['mobile']=run_context('verification-mobile', {'width':390,'height':844})
    # Separate reduced-motion smoke check.
    result['reduced']=run_context('verification-reduced-motion', {'width':390,'height':844}, reduced=True)
    browser.close()

print(json.dumps(result, ensure_ascii=False, indent=2))
