from playwright.sync_api import sync_playwright
from pathlib import Path

out=Path('/Users/laina/.hermes/profiles/sales/workspace/liuyun-technology/qa-pages'); out.mkdir(exist_ok=True)
paths=['index.html','web_path.html','shop_path.html','works.html','food.html','contact.html']
with sync_playwright() as p:
    b=p.chromium.launch(headless=True,executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
    for path in paths:
        for label,viewport in [('desktop',{'width':1440,'height':1000}),('mobile',{'width':390,'height':844})]:
            c=b.new_context(viewport=viewport); page=c.new_page(); page.goto('http://127.0.0.1:8765/'+path,wait_until='networkidle',timeout=60000); page.wait_for_timeout(500)
            for _ in range(14): page.evaluate('window.scrollBy(0, Math.max(700, window.innerHeight*.85))'); page.wait_for_timeout(80)
            page.evaluate('window.scrollTo(0,0)'); page.wait_for_timeout(150)
            page.screenshot(path=str(out/(path.replace('.html','')+'-'+label+'.png')),full_page=True)
            c.close()
    b.close()
print(str(out))
