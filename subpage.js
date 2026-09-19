(() => {
  const data = window.PAGE_DATA?.[document.body.dataset.page];
  const cases = window.LIUYUN_CASES || [];
  const prefix = document.body.dataset.prefix || '';
  if (!data) return;
  const $ = (s, root=document) => root.querySelector(s);
  const mediaNode = (item) => {
    const node = item.kind === 'video' ? document.createElement('video') : document.createElement('img');
    node.src = prefix + item.src;
    node.alt = item.displayTitle;
    if (item.kind === 'video') { node.autoplay=true; node.loop=true; node.muted=true; node.playsInline=true; node.preload='metadata'; }
    else { node.loading='eager'; node.decoding='async'; }
    return node;
  };
  const caseById = id => cases.find(x => x.id === id);
  const title = $('#page-title');
  const eyebrow = $('#page-eyebrow');
  const lead = $('#page-lead');
  const accent = $('#page-accent');
  document.title = `琉雲科技｜${data.title}`;
  if (title) title.innerHTML = `${data.title}<br><em>${data.accent || ''}</em>`;
  if (eyebrow) eyebrow.textContent = data.eyebrow || '';
  if (lead) lead.textContent = data.lead || '';
  if (accent) accent.textContent = data.accent || '';

  const heroPreview = $('#page-hero-preview');
  const firstCase = caseById((data.case_ids || [])[0]);
  if (heroPreview && firstCase) {
    const frame = document.createElement('div'); frame.className='subpage-preview-frame';
    frame.append(mediaNode(firstCase));
    const label = document.createElement('span'); label.textContent=firstCase.displayTitle;
    heroPreview.append(frame,label);
  }

  const sectionRoot = $('#page-sections');
  (data.sections || []).forEach((section, index) => {
    const block = document.createElement('article'); block.className='subpage-section';
    const grid = document.createElement('div'); grid.className='section-shell subpage-section-grid';
    const h = document.createElement('h2'); h.innerHTML = `${section.title}${index % 2 === 0 ? '<br><em>設計與內容都要到位</em>' : ''}`;
    const copy = document.createElement('p'); copy.className='subpage-copy'; copy.textContent=section.copy;
    grid.append(h, copy); block.append(grid); sectionRoot?.append(block);
  });

  const articleRoot = $('#page-articles');
  if (articleRoot && data.articles) {
    data.articles.forEach((article, index) => {
      const row=document.createElement('a'); row.className='subpage-article'; row.href=`${prefix}contact.html`;
      const no=document.createElement('span'); no.textContent=String(index+1).padStart(2,'0');
      const text=document.createElement('b'); text.textContent=article; row.append(no,text); articleRoot.append(row);
    });
  }


  const grid = $('#page-case-grid');
  const renderCase = item => {
    const card=document.createElement('article'); card.className='subpage-case-card'; card.tabIndex=0;
    const media=document.createElement('div'); media.className='subpage-case-media'; media.append(mediaNode(item));
    const info=document.createElement('div'); info.className='subpage-case-info';
    info.innerHTML=`<h3>${item.displayTitle}</h3><p>${item.filter} / ${item.category}</p>`;
    card.append(media,info);
    card.addEventListener('click',()=>openModal(item));
    card.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();openModal(item);}});
    grid?.append(card);
  };
  const pageCases=(data.case_ids || []).map(caseById).filter(Boolean);
  pageCases.forEach(renderCase);
  const caseCount=$('#page-case-count');
  if (caseCount) caseCount.textContent=data.path==='works.html' ? ` 本頁共 ${pageCases.length} 個案例；首頁保留 6 個精選。` : ` 本頁展示 ${pageCases.length} 個相關案例。`;

  const modal=$('#subpage-modal'); const modalMedia=$('#subpage-modal-media'); const modalTitle=$('#subpage-modal-title'); const modalInfo=$('#subpage-modal-info');
  function openModal(item){ if(!modal)return; modalMedia.innerHTML=''; modalMedia.append(mediaNode(item)); modalTitle.textContent=item.displayTitle; modalInfo.textContent=`${item.filter} / ${item.category}`; modal.classList.add('is-open'); modal.setAttribute('aria-hidden','false'); }
  function closeModal(){ if(!modal)return; modal.classList.remove('is-open'); modal.setAttribute('aria-hidden','true'); modalMedia.innerHTML=''; }
  document.querySelectorAll('[data-subpage-close]').forEach(x=>x.addEventListener('click',closeModal));
  document.addEventListener('keydown',e=>{if(e.key==='Escape')closeModal();});

  const form=$('#quote-form');
  form?.addEventListener('submit',e=>{e.preventDefault(); const status=$('#quote-status'); if(status) status.textContent='需求已整理完成；正式上線前請接上表單／CRM 端點。';});
  const menuToggle=document.querySelector('.menu-toggle'); const nav=document.querySelector('.site-nav');
  menuToggle?.addEventListener('click',()=>{const open=nav.classList.toggle('is-open'); menuToggle.setAttribute('aria-expanded',String(open));});
  nav?.querySelectorAll('.nav-link:not(.nav-dropdown-toggle)').forEach(link=>link.addEventListener('click',()=>{nav.classList.remove('is-open');menuToggle?.setAttribute('aria-expanded','false');}));
  const header=document.querySelector('#site-header'); const headerScroll=()=>header?.classList.toggle('is-scrolled',window.scrollY>24); headerScroll(); window.addEventListener('scroll',headerScroll,{passive:true});
  $('#year')?.append(new Date().getFullYear());
})();
