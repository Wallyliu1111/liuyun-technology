from playwright.sync_api import sync_playwright
import json
with sync_playwright() as p:
    b=p.chromium.launch(headless=True, executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
    c=b.new_context(viewport={'width':390,'height':844})
    page=c.new_page(); page.goto('http://127.0.0.1:8765/',wait_until='networkidle',timeout=60000); page.wait_for_timeout(600)
    before=page.locator('#site-nav.is-open').count()
    page.locator('.menu-toggle').click(); page.wait_for_timeout(200)
    after=page.locator('#site-nav.is-open').count()
    expanded=page.locator('.menu-toggle').get_attribute('aria-expanded')
    page.locator('.nav-link',has_text='網頁作品').click(); page.wait_for_timeout(200)
    closed=page.locator('#site-nav.is-open').count()
    print(json.dumps({'menu_open_before':before,'menu_open_after':after,'aria_expanded_after_open':expanded,'menu_closed_after_link':closed},ensure_ascii=False))
    b.close()
