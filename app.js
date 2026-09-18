(() => {
  const CASES = window.LIUYUN_CASES || [];
  const FEATURED_IDS = ['sky-cookie','coffee-rewards','gear-shop','no-code-waitlist','digital-experiences','product-studio'];
  const CASE_POOL = document.body.dataset.homeCases ? CASES.filter(item => FEATURED_IDS.includes(item.id)) : CASES;
  const $ = (selector, root = document) => root.querySelector(selector);
  const $$ = (selector, root = document) => [...root.querySelectorAll(selector)];
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  const createMedia = (item, className = '') => {
    const media = item.kind === 'video' ? document.createElement('video') : document.createElement('img');
    media.className = className;
    media.src = item.src;
    media.alt = `${item.displayTitle} / ${item.category}`;
    if (item.kind === 'video') {
      media.muted = true;
      media.loop = true;
      media.autoplay = true;
      media.playsInline = true;
      media.preload = 'metadata';
      media.setAttribute('aria-label', `${item.displayTitle} 動畫預覽`);
    } else {
      media.loading = 'eager';
      media.decoding = 'async';
    }
    return media;
  };

  const mountHeroSlot = (slot, item) => {
    if (!slot || !item) return;
    slot.innerHTML = '';
    const frame = document.createElement('div');
    frame.className = 'media-frame';
    frame.append(createMedia(item));
    const label = document.createElement('div');
    label.className = 'hero-card-label';
    const title = document.createElement('b');
    title.textContent = item.displayTitle;
    const category = document.createElement('span');
    category.textContent = item.filter;
    label.append(title, category);
    slot.append(frame, label);
    slot.addEventListener('click', () => openModal(item));
    slot.setAttribute('tabindex', '0');
    slot.setAttribute('role', 'button');
    slot.setAttribute('aria-label', `查看${item.displayTitle}案例`);
    slot.addEventListener('keydown', (event) => {
      if (event.key === 'Enter' || event.key === ' ') { event.preventDefault(); openModal(item); }
    });
  };

  $$('.hero-card[data-case-slot]').forEach((slot) => mountHeroSlot(slot, CASES[Number(slot.dataset.caseSlot)]));

  const grid = $('#case-grid');
  const filters = $$('.filter-button');
  const renderCases = (filter = 'all') => {
    if (!grid) return;
    grid.innerHTML = '';
    CASE_POOL.filter((item) => filter === 'all' || item.filter === filter).forEach((item, index) => {
      const card = document.createElement('article');
      card.className = 'case-card';
      card.style.animationDelay = `${Math.min(index * 55, 440)}ms`;
      card.tabIndex = 0;
      card.setAttribute('role', 'button');
      card.setAttribute('aria-label', `查看${item.displayTitle}案例`);
      const media = document.createElement('div');
      media.className = 'case-media';
      media.append(createMedia(item));
      const meta = document.createElement('div');
      meta.className = 'case-card-meta';
      const text = document.createElement('div');
      const title = document.createElement('h3');
      title.textContent = item.displayTitle;
      const category = document.createElement('span');
      category.textContent = `${item.filter} / ${item.category}`;
      text.append(title, category);
      const arrow = document.createElement('i');
      arrow.textContent = '↗';
      meta.append(text, arrow);
      card.append(media, meta);
      card.addEventListener('click', () => openModal(item));
      card.addEventListener('keydown', (event) => {
        if (event.key === 'Enter' || event.key === ' ') { event.preventDefault(); openModal(item); }
      });
      grid.append(card);
    });
  };
  renderCases();
  filters.forEach((button) => button.addEventListener('click', () => {
    filters.forEach((other) => other.classList.toggle('is-active', other === button));
    renderCases(button.dataset.filter);
  }));

  const modal = $('#case-modal');
  const modalMedia = $('#modal-media');
  const modalTitle = $('#modal-title');
  const modalCategory = $('#modal-category');
  let lastFocused = null;
  const openModal = (item) => {
    if (!modal) return;
    lastFocused = document.activeElement;
    modalMedia.innerHTML = '';
    modalMedia.append(createMedia(item));
    modalTitle.textContent = item.displayTitle;
    modalCategory.textContent = `${item.title} · ${item.filter} / ${item.category}`;
    modal.classList.add('is-open');
    modal.setAttribute('aria-hidden', 'false');
    document.body.classList.add('modal-lock');
    $('.modal-close', modal)?.focus();
  };
  const closeModal = () => {
    if (!modal) return;
    modal.classList.remove('is-open');
    modal.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('modal-lock');
    modalMedia.innerHTML = '';
    if (lastFocused && typeof lastFocused.focus === 'function') lastFocused.focus();
  };
  $$('[data-modal-close]').forEach((element) => element.addEventListener('click', closeModal));
  document.addEventListener('keydown', (event) => { if (event.key === 'Escape' && modal?.classList.contains('is-open')) closeModal(); });

  const header = $('#site-header');
  const onScroll = () => header?.classList.toggle('is-scrolled', window.scrollY > 24);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  const menuToggle = $('.menu-toggle');
  const nav = $('#site-nav');
  menuToggle?.addEventListener('click', () => {
    const open = nav.classList.toggle('is-open');
    menuToggle.setAttribute('aria-expanded', String(open));
  });
  $$('.nav-link:not(.nav-dropdown-toggle)', nav).forEach((link) => link.addEventListener('click', () => {
    nav.classList.remove('is-open');
    menuToggle?.setAttribute('aria-expanded', 'false');
  }));

  const revealNodes = $$('[data-reveal]');
  if ('IntersectionObserver' in window && !reducedMotion) {
    const observer = new IntersectionObserver((entries, instance) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) { entry.target.classList.add('is-in'); instance.unobserve(entry.target); }
      });
    }, { threshold: .12, rootMargin: '0px 0px -50px' });
    revealNodes.forEach((node) => observer.observe(node));
  } else revealNodes.forEach((node) => node.classList.add('is-in'));

  if (!reducedMotion) {
    window.addEventListener('pointermove', (event) => {
      document.documentElement.style.setProperty('--cursor-x', `${event.clientX}px`);
      document.documentElement.style.setProperty('--cursor-y', `${event.clientY}px`);
      const stage = $('.hero-stage');
      if (stage && window.innerWidth > 800) {
        const x = (event.clientX / window.innerWidth - .5) * 14;
        const y = (event.clientY / window.innerHeight - .5) * 14;
        stage.style.setProperty('--mx', x.toFixed(2));
        stage.style.setProperty('--my', y.toFixed(2));
      }
    }, { passive: true });
  }

  $('#year').textContent = new Date().getFullYear();
  $('#contact-button')?.addEventListener('click', () => {
    const status = $('#contact-status');
    if (status) status.textContent = '索取報價表單入口尚待接上。';
  });
})();