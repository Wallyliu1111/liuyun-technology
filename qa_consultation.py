from playwright.sync_api import sync_playwright
from pathlib import Path
out=Path('/Users/laina/.hermes/profiles/sales/workspace/liuyun-technology/qa-pages'); out.mkdir(exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch(headless=True, executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
    for label,viewport in [('desktop',{'width':1440,'height':1000}),('mobile',{'width':390,'height':844})]:
        c=b.new_context(viewport=viewport); page=c.new_page(); page.goto('http://127.0.0.1:8876/consultation.html',wait_until='networkidle',timeout=60000); page.wait_for_timeout(400)
        page.screenshot(path=str(out/f'consultation-{label}-hero.png'),full_page=False)
        page.locator('input[name="siteType"][value="landing"]').evaluate("el => el.closest('label').click()")
        page.locator('[data-next-step="1"]').first.click(); page.wait_for_timeout(150)
        page.locator('.quote-step-panel.is-active .quote-step-actions').scroll_into_view_if_needed(); page.wait_for_timeout(150)
        page.screenshot(path=str(out/f'consultation-{label}-scale.png'),full_page=False)
        c.close()
    b.close()
print(out)
