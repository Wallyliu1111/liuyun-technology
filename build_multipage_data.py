import json
from pathlib import Path

ROOT = Path('/Users/laina/.hermes/profiles/sales/workspace/liuyun-technology')

CASES = [
    'no-code-waitlist','neon-logic','nexacore-control','intelligentx','stillmind','vision-reveal',
    'digital-experiences','wellness-device','cross-border','subscription-agency','beauty-categories','blog-showcase',
    'sky-cookie','coffee-rewards','shop','gear-shop','product-studio'
]

pages = {
 'web_path': {
  'path':'web_path.html','source':'https://www.buyersline.com.tw/web_path.html','eyebrow':'高CP網站設計 / WEB PRICING','title':'高CP網站設計','accent':'設計報價','lead':'設計好視覺，提升品牌價值。琉雲科技是您可以100%信賴的團隊首選。','case_ids':['digital-experiences','nexacore-control','subscription-agency'],
  'sections':[
   {'title':'團隊依您的需求做規劃','copy':'價格的不同是因為模組&客製化不同、設計的深淺不同、執行細節服務不同、耗費的成本不同。'},
   {'title':'如何製作高CP值網站？','copy':'想要降低預算又可以獲得好網站，選版 or 模組設計方案是高CP的好選擇。作業快速省成本、品質優美成果好、配合行銷曝光效益佳，讓1+1>2。'},
   {'title':'好網站展現企業專業度、好感度','copy':'內容企劃為優先，八大重點，專業才能贏得訂單。網站設計不是藝術品，重點是展現企業專業形象、介紹企業優勢，是企業給買主與社會大眾的履歷表。'}
  ],
  'plans':[
   {'name':'物美價廉方案','tag':'選版也能好質感','price':'NT$ 3.6~6.8 萬','items':['網站視覺設計','網站內容規劃','多版型選擇製作','CMS管理功能']},
   {'name':'高CP質感網站','tag':'設計出特色，物超所值','price':'NT$ 8.8~15 萬','items':['網站內容企劃','形象風格規劃','內容視覺設計','高級動態特效','CMS管理模組']},
   {'name':'豪華旗艦形象','tag':'量身創造品牌價值','price':'NT$ 180,000 起','items':['網站整體企劃','品牌形象設計','內容視覺設計','高階動態特效','客製化CMS功能']}
  ]
 },
 'shop': {
  'path':'shop_path.html','source':'https://www.buyersline.com.tw/shop_path.html','eyebrow':'購物網站設計 / SHOPPING WEBSITE','title':'輕鬆開店，積極行銷','accent':'創建一個高人氣網路商店','lead':'視覺瀏覽動線佳，便利消費買氣旺。網站前台：豪華電商格局，增加買氣更安心。','case_ids':['gear-shop','shop','beauty-categories'],
  'sections':[
   {'title':'購物流程方便，消費點單超便利','copy':'後台：訂單、促銷、會員功能完整，操作容易，輕鬆上手。開店不用傷腦筋，行動購物超便利，動動手指就下單。'},
   {'title':'30多項功能，比你要的更完整','copy':'操作簡單，輕鬆管理，時間省更多。產品櫥窗、購物車、訂單管理、會員管理、滿額免運、廣告管理、促銷管理與頁面管理，從前台到後台完整串接。'},
   {'title':'Plus+加值服務讓網站效益加倍','copy':'網址DNS、指向服務、SSL憑證服務、雲端主機管理服務、SEO優化服務、關鍵字廣告服務、商業攝影服務，並可串接金流與物流。'}
  ],
  'plans':[{'name':'購物網站設計','tag':'NT$ 38,800 /起','price':'＋維護與主機年費','items':['SSL加密憑證','金流串接','物流串接','滿件折扣／滿額折扣／優惠碼折扣','Google 關鍵字廣告','SEO排序廣告']}]
 },
 'brand': {
  'path':'brand-web.html','source':'https://www.buyersline.com.tw/brand-web.html','eyebrow':'B2C BRAND WEBSITE','title':'B2C品牌網站','accent':'B2C企業形象網頁設計','lead':'從品牌形象、產品資訊到線上購物，讓企業與消費者之間的溝通更清楚。','case_ids':['beauty-categories','digital-experiences','stillmind'],
  'sections':[
   {'title':'B2C品牌網站','copy':'品牌網站以消費者瀏覽體驗為優先，將企業故事、產品特色與購買動線整合在同一個入口。'},
   {'title':'B2C品牌網站的內容規劃','copy':'從主視覺形象、產品櫥窗、品牌故事、最新消息到聯絡與購買功能，讓品牌內容完整呈現。'},
   {'title':'B2B品牌網站','copy':'若企業同時面對通路商、代理商或國際買主，網站也能依不同閱讀對象建立清楚的資訊層級。'}
  ]
 },
 'b2b': {
  'path':'b2b.html','source':'https://www.buyersline.com.tw/RWD-B2B.html','eyebrow':'B2B WEBSITE','title':'B2B品牌網站','accent':'B2B製造業網站設計','lead':'科技、電子、工業、製造等企業，以網站展現企業優勢、產品能力與合作條件。','case_ids':['nexacore-control','digital-experiences','cross-border'],
  'sections':[
   {'title':'台灣製造','copy':'設備、產能、技術、品質與流程，都是B2B網站需要被清楚整理的企業資產。'},
   {'title':'上市櫃公司／企業品牌','copy':'用企業簡介、沿革、理念、獎項認證與實績案例，建立買主與合作夥伴的信任。'},
   {'title':'全球行銷／線上詢問','copy':'讓產品資料、規格、服務流程與聯絡入口，成為業務開發可以持續使用的工具。'}
  ]
 },
 'system': {
  'path':'system.html','source':'https://www.buyersline.com.tw/system.html','eyebrow':'CUSTOM SYSTEM WEBSITE','title':'客製程式網站','accent':'依企業需求客製化網站程式系統開發','lead':'程式系統的協助，可以讓瀏覽者輕鬆查詢，讓網站維護者工作更省時，提高資訊服務的效益。','case_ids':['nexacore-control','intelligentx','blog-showcase'],
  'sections':[
   {'title':'客製程式網站','copy':'依企業需求客製化網站程式系統開發，從資料查詢、會員管理、內容管理到企業內部流程，建立適合實際作業的網站系統。'},
   {'title':'查詢與管理','copy':'讓瀏覽者輕鬆查詢，也讓網站維護者工作更省時；把原本分散的資料與流程整理成可維護的介面。'},
   {'title':'程式系統案例','copy':'僧伽大學、讀報教育、蔬福生活、永續材質圖書館與企業產品平台，都是客製程式網站可承接的不同場景。'}
  ]
 },
 'cis': {
  'path':'cis-logo.html','source':'https://www.buyersline.com.tw/CIS_path.html','eyebrow':'CIS / LOGO DESIGN','title':'CIS企業識別','accent':'一站式整合服務，展現企業品牌力','lead':'從Logo、企業識別系統到型錄、海報與網站，讓品牌在不同接觸點保持一致。','case_ids':['vision-reveal','digital-experiences','neon-logic'],
  'sections':[
   {'title':'CIS 企業識別系統','copy':'企業識別不只是一個Logo，而是品牌在名片、網站、型錄、包裝與展場上呈現的完整規則。'},
   {'title':'Plus+加值服務強化品牌影響力','copy':'企業識別CIS／Logo設計、型錄設計、海報／易拉展、商品包裝設計，依企業實際使用情境規劃。'},
   {'title':'從識別到網站','copy':'識別完成後，延伸到企業網站、品牌客製網站與數位行銷，讓視覺系統真正被使用。'}
  ]
 },
 'catalog': {
  'path':'catalog-design.html','source':'https://www.buyersline.com.tw/catalog_path.html','eyebrow':'CATALOG / DM DESIGN','title':'型錄DM設計','accent':'好型錄展現品牌專業度、好感度','lead':'型錄設計提升品牌、產品價值贏得顧客信心。','case_ids':['nexacore-control','beauty-categories','digital-experiences'],
  'sections':[
   {'title':'型錄設計','copy':'依產品資料、規格、圖片與品牌識別，整理出能被業務、通路與顧客使用的型錄內容。'},
   {'title':'海報設計','copy':'情境Banner美化視覺，發揮視覺傳達目的；也可延伸到展場海報、易拉展與活動宣傳物。'},
   {'title':'CIS 企業識別 / LOGO 設計','copy':'從平面視覺到網站入口，讓品牌在每個接觸點維持清楚的識別。'}
  ]
 },
 'marketing': {
  'path':'marketing.html','source':'https://www.buyersline.com.tw/marekting.html','eyebrow':'DIGITAL MARKETING','title':'數位網路行銷','accent':'SEM搜尋行銷／SEO排名優化行銷／關鍵字點播廣告行銷','lead':'網站完成後，讓目標顧客找得到、看得懂，再透過持續的內容與廣告累積曝光。','case_ids':['digital-experiences','blog-showcase','no-code-waitlist'],
  'sections':[
   {'title':'SEM搜尋行銷','copy':'依企業服務與產品關鍵字規劃搜尋廣告，讓有需求的顧客在搜尋時找到網站。'},
   {'title':'SEO排名優化行銷','copy':'網站內容豐富瀏覽度就會提升，產業文案關聯度也會提升，對於網站的SEO搜尋排序有很大的幫助。'},
   {'title':'關鍵字點播廣告行銷','copy':'配合季度活動、產品上市與服務方案，建立可追蹤的廣告入口與內容節奏。'}
  ]
 },
 'about': {
  'path':'about.html','source':'https://www.buyersline.com.tw/about_tw_1.php','eyebrow':'ABOUT LIUYUN','title':'公司簡介','accent':'琉雲科技是您可以100%信賴的團隊首選','lead':'以企業需求為出發點，從網站內容、視覺設計到系統功能，整理出能被使用的數位服務。','case_ids':['digital-experiences','nexacore-control','subscription-agency'],
  'sections':[
   {'title':'網站視覺形象需到位','copy':'產業屬性有科技、工業、生活用品、醫療……從B2B到B2C，從製造到零售，產品等級、產業TA不同，風格會有差異。'},
   {'title':'網站設計內容規劃為優先','copy':'網站設計不是藝術品，重點是展現企業專業形象、介紹企業優勢，是企業給買主與社會大眾的履歷表。'},
   {'title':'內容豐富，搜尋與瀏覽才有基礎','copy':'文案可以很創意但不失專業，內容豐富瀏覽度就會提升，產業文案關聯度也會提升。'}
  ]
 },
 'works': {
  'path':'works.html','source':'https://www.buyersline.com.tw/product_tw.php','eyebrow':'WORKS / 網頁作品','title':'網頁設計實績','accent':'作品實績','lead':'從形象網站、購物網站到客製程式網站，依頁面實際畫面與用途整理案例。','case_ids':CASES,
  'sections':[{'title':'作品實績','copy':'以下案例使用本地 MotionSites 公開預覽素材；分類依畫面可辨識的頁面用途整理，未把畫面沒有出現的產業硬套上去。'}]
 },
 'food': {
  'path':'food.html','source':'https://www.buyersline.com.tw/food-web-site.html','eyebrow':'食品 餐旅 / FOOD & HOSPITALITY','title':'食品餐飲、餐廳飯店、伴手禮網站設計','accent':'推薦高CP網頁設計方案','lead':'食品品牌、餐廳、咖啡與餐旅服務，先把產品、故事、場景與到店／購買動線整理清楚。','case_ids':['sky-cookie','coffee-rewards'],
  'sections':[
   {'title':'食品品牌網站','copy':'把產品、成分、包裝、產地與品牌故事整理成清楚的產品入口，讓顧客能從內容走到詢問或購買。'},
   {'title':'餐廳／咖啡網站','copy':'菜單、招牌品項、營業資訊、門市位置與預約入口要被快速找到；咖啡與飲品服務也能用消費紀錄與會員內容延伸互動。'},
   {'title':'餐旅與伴手禮','copy':'餐廳飯店、旅宿、伴手禮與地方品牌，透過場景照片、空間介紹、體驗流程與訂房／訂購動線建立信任。'}
  ]
 },
 'architecture': {
  'path':'architecture.html','source':'https://www.buyersline.com.tw/%E5%BB%BA%E7%AF%89%E5%AE%A4%E5%85%A7%E8%A8%AD%E8%A8%88.html','eyebrow':'建築 建材 / ARCHITECTURE','title':'建築、建材、室內設計、傢俱網站設計','accent':'好設計助您網路商機事半功倍','lead':'專業團隊為您專業服務。從作品、材質、工法、空間與案例故事，建立建築與室內設計品牌的信任。','case_ids':['digital-experiences','stillmind','nexacore-control'],
  'sections':[{'title':'建築 建材','copy':'建築、建材、室內設計、傢俱網站設計，需要用作品展示與內容規劃，讓瀏覽者快速理解風格與能力。'}]
 },
 'technology': {
  'path':'technology.html','source':'https://www.buyersline.com.tw/%E7%A7%91%E6%8A%80%E9%9B%BB%E5%AD%90.html','eyebrow':'科技 電子 / TECHNOLOGY','title':'上市櫃公司網站設計、ESG永續發展網站設計','accent':'B2B品牌網站','lead':'設備、產能、技術、品質與ESG內容，透過網站整理成買主與合作夥伴看得懂的企業資訊。','case_ids':['nexacore-control','no-code-waitlist','digital-experiences'],
  'sections':[{'title':'科技 電子','copy':'以企業簡介、產品服務、品質流程、實績與聯絡入口，建立穩定的企業網站架構。'}]
 },
 'knowledge': {
  'path':'knowledge.html','source':'https://www.buyersline.com.tw/web-design.html','eyebrow':'網頁設計學堂 / KNOWLEDGE','title':'網頁設計相關知識','accent':'網站內容架構規劃','lead':'從網頁設計費用、RWD、內容準備到網站視覺與SEO，整理成企業可以先讀懂的資訊。','case_ids':['blog-showcase','digital-experiences'],
  'articles':['為何市場上網頁設計費用有5~50萬很大的落差？','配色影響網站視覺風格，如何選擇合適的配色？','網站設計有三種面向，面面俱到才能發揮總體效益','網頁設計從無到有的流程說明','網頁設計有哪些類型差異?','網頁設計需要支付哪些費用呢?','5秒讓您瞬懂RWD 與 為何需要RWD網站 !!','初談RWD網站的頁面設計概念 與優缺點說明','什麼是三機一體的RWD智慧型網頁?','網頁設計預算影響品質嗎?'],
  'sections':[{'title':'熱門文章','copy':'網站視覺形象、內容介紹與搜尋曝光，三個面向一起規劃，網站才有總體效益。'}]
 },
 'marketing-knowledge': {
  'path':'marketing-knowledge.html','source':'https://www.buyersline.com.tw/SEO-SEM.html','eyebrow':'網路行銷學堂 / MARKETING','title':'網路行銷相關知識','accent':'Visual Marketing Q&A','lead':'從網站、SEO、SEM到內容與廣告，先把行銷入口與顧客路徑整理清楚。','case_ids':['blog-showcase','no-code-waitlist'],
  'articles':['新創公司，如何運用網站做好網絡行銷？','行動條碼 QR Code 產生器 ～免費好用看這裡','【前4脈】打通您的業績8脈，就靠FB廣告行銷','【後4脈】打通您的業績8脈，就靠FB廣告行銷','觸及全台1600萬人的網路行銷神器，您，還沒使用 ?','橫幅廣告','彈跳視窗廣告','連結行銷','EDM行銷','病毒式行銷'],
  'sections':[{'title':'熱門文章／最新文章','copy':'把網站內容、搜尋排序與廣告入口接在一起，持續累積可被找到的內容。'}]
 },
 'contact': {
  'path':'contact.html','source':'https://www.buyersline.com.tw/contact_tw.php','eyebrow':'CONTACT / 索取報價','title':'聯絡我們','accent':'琉雲科技是您最佳選擇','lead':'請留下需求，讓我們依網站規模、內容規劃、視覺設計與功能需求提供報價方向。','case_ids':['nexacore-control','beauty-categories','digital-experiences'],
  'sections':[{'title':'索取報價','copy':'網站視覺設計、網站內容規劃、購物網站設計、品牌客製網站、CIS企業識別、型錄DM設計與數位網路行銷，請從需求開始說明。'}],
  'form':True
 }
}

# Add one detail page for each curated motion case.
for cid in CASES:
    row = next(x for x in json.loads((ROOT/'cases.json').read_text()) if x['id']==cid)
    pages['work-'+cid] = {
        'path':f'works/{cid}.html','source':row['sourcePage'],'eyebrow':row['filter']+' / WORK DETAIL',
        'title':row['displayTitle'],'accent':row['category'],'lead':'這是一個本地 MotionSites 公開預覽案例；下方說明只採用畫面可辨識的用途與視覺方向。',
        'case_ids':[cid], 'sections':[{'title':'畫面用途','copy':f"{row['displayTitle']}｜{row['category']}。以實際預覽畫面為準，未把未出現的產品或產業資訊寫成事實。"}],
        'sourcePage':row['sourcePage']
    }

(ROOT/'routes.json').write_text(json.dumps({'route_count':len(pages),'routes':[{'key':key,'path':value['path'],'title':value.get('title',''),'source':value.get('source',value.get('sourcePage',''))} for key,value in pages.items()]},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(ROOT/'site-data.js').write_text('window.PAGE_DATA = '+json.dumps(pages,ensure_ascii=False,indent=2)+';\n',encoding='utf-8')
print('page_data',len(pages))
