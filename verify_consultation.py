from playwright.sync_api import sync_playwright
import json

ROOT='http://127.0.0.1:8876/'
with sync_playwright() as p:
    b=p.chromium.launch(headless=True, executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
    d=b.new_page(viewport={'width':1440,'height':1000})
    errors=[]; failed=[]
    d.on('console', lambda msg: errors.append(msg.text) if msg.type=='error' else None)
    d.on('requestfailed', lambda req: failed.append({'url':req.url,'error':req.failure}))
    d.goto(ROOT+'consultation.html', wait_until='networkidle', timeout=60000); d.wait_for_timeout(300)
    def choose(selector):
        d.locator(selector).evaluate("el => el.closest('label').click()")
    out={'title':d.title(),'initial_total':d.locator('#quote-total').inner_text(),'initial_step':d.locator('[data-step-panel].is-active').get_attribute('data-step-panel')}
    choose('input[name="siteType"][value="landing"]'); out['landing_total']=d.locator('#quote-total').inner_text(); out['next_enabled']=not d.locator('[data-next-step="1"]').first.is_disabled()
    d.locator('[data-next-step="1"]').first.click(); d.wait_for_timeout(100)
    out['step_after_next']=d.locator('[data-step-panel].is-active').get_attribute('data-step-panel')
    choose('input[name="pageScale"][value="medium"]'); d.locator('[data-next-step="2"]').click(); d.wait_for_timeout(100)
    choose('input[name="design"][value="semi"]'); d.locator('[data-next-step="3"]').click(); d.wait_for_timeout(100)
    choose('input[data-group="features"][value="cms"]'); choose('input[data-group="features"][value="motion"]'); d.locator('[data-next-step="4"]').click(); d.wait_for_timeout(100)
    choose('input[data-group="addons"][value="copy"]'); out['configured_total']=d.locator('#quote-total').inner_text(); out['final_step']=d.locator('[data-step-panel].is-active').get_attribute('data-step-panel'); out['summary_has_copy']= '頁面文案架構與初稿' in d.locator('#quote-final-breakdown').inner_text()
    d.locator('#quote-copy').click(); d.wait_for_timeout(100); out['copy_status']=d.locator('#quote-copy-status').inner_text()
    out['desktop_errors']=errors; out['desktop_failed']=failed
    m=b.new_page(viewport={'width':390,'height':844}); m.goto(ROOT+'consultation.html', wait_until='networkidle', timeout=60000); m.wait_for_timeout(300)
    out['mobile_overflow']=m.evaluate('document.documentElement.scrollWidth > document.documentElement.clientWidth')
    out['mobile_menu_before']=m.locator('#site-nav.is-open').count(); m.locator('.menu-toggle').click(); out['mobile_menu_after']=m.locator('#site-nav.is-open').count(); m.locator('.nav-dropdown-toggle').first.click(); out['mobile_dropdown_items']=m.locator('.nav-dropdown.is-open .nav-dropdown-link').count()
    b.close()
print(json.dumps(out, ensure_ascii=False, indent=2))
