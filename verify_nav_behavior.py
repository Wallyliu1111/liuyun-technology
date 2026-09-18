from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(headless=True, executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
    d=b.new_page(viewport={'width':1440,'height':900})
    d.goto('http://127.0.0.1:8765/', wait_until='networkidle'); d.wait_for_timeout(250)
    initial=d.locator('.nav-dropdown.is-open').count()
    box=d.locator('.nav-dropdown').first.bounding_box(); d.mouse.move(box['x']+box['width']/2, box['y']+12); d.wait_for_timeout(150)
    hover=d.locator('.nav-dropdown.is-open').count(); hover_visible=d.locator('.nav-dropdown').first.locator('.nav-dropdown-panel').is_visible()
    d.mouse.move(10,300); d.wait_for_timeout(150); after_leave=d.locator('.nav-dropdown.is-open').count()
    m=b.new_page(viewport={'width':390,'height':844}); m.goto('http://127.0.0.1:8765/shop_path.html',wait_until='networkidle'); m.wait_for_timeout(250); m.locator('.menu-toggle').click(); m.locator('.nav-dropdown-toggle').first.click(); m.wait_for_timeout(100)
    print({'desktop_initial_open':initial,'desktop_hover_open':hover,'desktop_hover_visible':hover_visible,'desktop_after_leave':after_leave,'mobile_open':m.locator('.nav-dropdown.is-open').count(),'mobile_items':m.locator('.nav-dropdown.is-open .nav-dropdown-link').count()})
    b.close()
