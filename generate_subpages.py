import json, re
from pathlib import Path

ROOT=Path('/Users/laina/.hermes/profiles/sales/workspace/liuyun-technology')
raw=(ROOT/'site-data.js').read_text(encoding='utf-8')
pages=json.loads(raw.split('=',1)[1].rsplit(';',1)[0].strip())

nav_groups=[
    ('網站設計',[('高CP網站設計','web_path.html'),('購物網站設計','shop_path.html'),('品牌客製網站','brand-web.html'),('B2B 品牌網站','b2b.html'),('CIS／Logo 設計','cis-logo.html'),('型錄／DM 設計','catalog-design.html'),('數位網路行銷','marketing.html')]),
    ('網頁作品',[('全部作品','works.html'),('食品餐旅','food.html'),('建築建材','architecture.html'),('科技電子','technology.html')])
]
knowledge_items=[('網頁設計學堂','knowledge.html'),('網路行銷學堂','marketing-knowledge.html')]

def link(prefix,path): return prefix+path

def build_nav_html(prefix):
    html=[f'<a class="nav-link" href="{link(prefix,"index.html#top")}">HOME</a>']
    for label,items in nav_groups:
        children=''.join(f'<a class="nav-dropdown-link" href="{link(prefix,path)}">{child}</a>' for child,path in items)
        html.append(f'<div class="nav-dropdown"><button class="nav-link nav-dropdown-toggle" type="button" aria-expanded="false">{label}<span aria-hidden="true">⌄</span></button><div class="nav-dropdown-panel">{children}</div></div>')
    html.append(f'<a class="nav-link" href="{link(prefix,"about.html")}">公司簡介</a>')
    children=''.join(f'<a class="nav-dropdown-link" href="{link(prefix,path)}">{child}</a>' for child,path in knowledge_items)
    html.append(f'<div class="nav-dropdown"><button class="nav-link nav-dropdown-toggle" type="button" aria-expanded="false">知識學堂<span aria-hidden="true">⌄</span></button><div class="nav-dropdown-panel">{children}</div></div>')
    html.append(f'<a class="nav-link" href="{link(prefix,"consultation.html")}">需求諮詢</a>')
    return ''.join(html)

def page_html(key,data):
    path=data['path']; nested='/' in path
    prefix='../' if nested else ''
    nav_html=build_nav_html(prefix)
    base=f'''<!doctype html>
<html lang="zh-Hant">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#081832">
  <meta name="description" content="{data.get('title','')}｜琉雲科技網站規劃、視覺設計、購物網站與客製程式網站服務。">
  <title>琉雲科技｜{data.get('title','')}</title>
  <link rel="icon" href="{prefix}assets/liuyun-logo.png">
  <link rel="stylesheet" href="{prefix}styles.css">
  <link rel="stylesheet" href="{prefix}subpage.css">
</head>
<body class="subpage" data-page="{key}" data-prefix="{prefix}">
  <header class="site-header" id="site-header"><div class="nav-shell">
    <a class="brand" href="{link(prefix,'index.html')}" aria-label="琉雲科技首頁"><img src="{prefix}assets/liuyun-logo.png" alt="琉雲科技 LIUYUN TECHNOLOGY"></a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav"><span></span><span></span><b>MENU</b></button>
    <nav class="site-nav" id="site-nav" aria-label="主要導覽">{nav_html}</nav>
    <a class="nav-cta" href="{link(prefix,'consultation.html')}">需求諮詢 <span aria-hidden="true">↗</span></a>
  </div></header>
  <main>
    <section class="subpage-hero"><div class="section-shell">
      <p class="eyebrow eyebrow--blue" id="page-eyebrow"><span class="eyebrow-dot"></span>{data.get('eyebrow','')}</p>
      <h1 id="page-title">{data.get('title','')}<br><em>{data.get('accent','')}</em></h1>
      <p class="subpage-lead" id="page-lead">{data.get('lead','')}</p>
      <div class="subpage-meta"><span>網站視覺設計</span><span>網站內容規劃</span><span>動畫與互動展示</span><span>RWD 響應式網站</span></div>
      <div class="subpage-orbit" aria-hidden="true"></div><div class="subpage-hero-preview" id="page-hero-preview"></div>
    </div></section>
    <section class="subpage-main"><div id="page-sections"></div>
      <div class="section-shell" id="page-articles"></div>
    </section>
    <section class="subpage-cases"><div class="section-shell"><p class="eyebrow eyebrow--mint"><span class="eyebrow-dot"></span> WORKS / 案例展示</p><h2>依照實際畫面，<br><em>看見服務如何被使用。</em></h2><p class="subpage-cases-intro">案例分類只採用動畫或預覽畫面可以辨識的用途；不把畫面沒有出現的產業硬套上去。<span id="page-case-count"></span></p><div class="subpage-case-grid" id="page-case-grid"></div></div></section>
    <section class="contact-section" id="contact-form"><div class="section-shell contact-layout"><div><p class="eyebrow eyebrow--blue"><span class="eyebrow-dot"></span> CONTACT / 索取報價</p><h2>網站內容與預算，<br><em>先從需求開始整理。</em></h2></div><div class="contact-copy"><p>請留下網站類型、產業場景、內容規模與預計上線時間；正式上線前再接入實際表單端點。</p><form class="subpage-form" id="quote-form"><label>稱呼<input name="name" required placeholder="您的稱呼"></label><label>網站類型<select name="type"><option>企業形象網站</option><option>購物網站</option><option>品牌客製網站</option><option>客製程式網站</option><option>型錄／CIS／平面設計</option></select></label><label>需求說明<textarea name="message" placeholder="請描述產業、網站頁面、案例或功能需求"></textarea></label><button class="button button--dark" type="submit">送出需求 <span aria-hidden="true">↗</span></button><small class="subpage-form-status" id="quote-status"></small></form></div></div></section>
  </main>
  <footer class="site-footer"><div class="section-shell footer-main"><div class="footer-brand"><img src="{prefix}assets/liuyun-logo.png" alt="琉雲科技"><p>高CP網站設計、購物網站設計、品牌客製網站與客製程式網站。</p></div><div class="footer-links"><div><small>設計＆費用</small><a href="{link(prefix,'web_path.html')}">高CP網站設計</a><a href="{link(prefix,'shop_path.html')}">購物網站設計</a><a href="{link(prefix,'brand-web.html')}">品牌客製網站</a></div><div><small>作品實績</small><a href="{link(prefix,'works.html')}">網頁作品</a><a href="{link(prefix,'food.html')}">食品 餐旅</a><a href="{link(prefix,'architecture.html')}">建築 建材</a></div><div><small>內容與系統</small><a href="{link(prefix,'system.html')}">客製程式網站</a><a href="{link(prefix,'knowledge.html')}">網頁設計學堂</a><a href="{link(prefix,'marketing-knowledge.html')}">網路行銷學堂</a></div><div><small>LIUYUN</small><span>LIUYUN TECHNOLOGY</span><a href="{link(prefix,'consultation.html')}">需求諮詢</a><span>© <span id="year"></span> 琉雲科技</span></div></div></div><div class="section-shell footer-bottom"><span>網頁設計｜網站設計｜網路開店</span><span>LIUYUN TECHNOLOGY</span></div></footer>
  <div class="subpage-modal" id="subpage-modal" aria-hidden="true" role="dialog"><div class="subpage-modal-backdrop" data-subpage-close></div><div class="subpage-modal-panel"><button class="subpage-modal-close" type="button" data-subpage-close aria-label="關閉預覽">×</button><div class="subpage-modal-media" id="subpage-modal-media"></div><div class="subpage-modal-info"><h2 id="subpage-modal-title"></h2><p id="subpage-modal-info"></p></div></div></div>
  <script src="{prefix}cases.js"></script><script src="{prefix}site-data.js"></script><script src="{prefix}nav.js"></script><script src="{prefix}subpage.js"></script>
</body></html>'''
    return base

for key,data in pages.items():
    path=ROOT/data['path']; path.parent.mkdir(parents=True,exist_ok=True); path.write_text(page_html(key,data),encoding='utf-8')
print('generated_pages',len(pages))
