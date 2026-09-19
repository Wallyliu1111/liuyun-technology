(() => {
  const PRICE = {
    consultation: 3000,
    siteTypes: {
      briefing: { label: '只做需求整理／規格書', price: 0 },
      landing: { label: '單頁／活動頁', price: 12000 },
      business: { label: '企業形象網站', price: 35000 },
      b2b: { label: 'B2B／多頁內容網站', price: 55000 },
      shop: { label: '購物網站', price: 65000 },
      custom: { label: '客製功能／資料系統', price: 120000 }
    },
    pageScale: {
      small: { label: '5 頁內', price: 0 },
      medium: { label: '6–10 頁', price: 8000 },
      large: { label: '11–20 頁', price: 18000 },
      xlarge: { label: '20 頁以上', price: 32000 }
    },
    design: {
      template: { label: '快速套版整理', price: 0 },
      semi: { label: '半客製視覺', price: 12000 },
      custom: { label: '完整客製視覺', price: 30000 }
    },
    features: {
      cms: { label: 'CMS 內容管理', price: 8000 },
      form: { label: '詢問表單與通知信', price: 3000 },
      seo: { label: 'SEO 基礎結構', price: 5000 },
      motion: { label: '動畫與互動展示', price: 8000 },
      member: { label: '會員／登入系統', price: 15000 },
      booking: { label: '預約／報名流程', price: 18000 },
      payment: { label: '金流串接', price: 15000 },
      shipping: { label: '物流串接', price: 10000 },
      multilingual: { label: '中英雙語架構', price: 12000 },
      api: { label: '第三方 API／資料串接', price: 25000 }
    },
    addons: {
      copy: { label: '頁面文案架構與初稿', price: 10000 },
      images: { label: '圖片整理與上稿', price: 5000 },
      training: { label: 'CMS 操作教學', price: 5000 },
      launch: { label: '上線前檢查與部署', price: 5000 }
    }
  };

  const STORAGE_KEY = 'liuyun-consultation-v1';
  const $ = (selector, root = document) => root.querySelector(selector);
  const $$ = (selector, root = document) => [...root.querySelectorAll(selector)];
  const money = (value) => `NT$ ${new Intl.NumberFormat('zh-TW').format(value)}`;
  const emptyState = () => ({ step: 0, siteType: null, pageScale: 'small', design: 'template', features: [], addons: [] });
  let state = emptyState();

  try {
    const stored = JSON.parse(localStorage.getItem(STORAGE_KEY) || 'null');
    if (stored) state = { ...emptyState(), ...stored, features: stored.features || [], addons: stored.addons || [] };
  } catch (_) { state = emptyState(); }

  const getBreakdown = () => {
    const rows = [{ label: '需求諮詢與架構整理', price: PRICE.consultation, kind: 'base' }];
    if (state.siteType && PRICE.siteTypes[state.siteType]) rows.push({ label: PRICE.siteTypes[state.siteType].label, price: PRICE.siteTypes[state.siteType].price, kind: 'site' });
    if (PRICE.pageScale[state.pageScale]?.price) rows.push({ label: PRICE.pageScale[state.pageScale].label, price: PRICE.pageScale[state.pageScale].price, kind: 'scale' });
    if (PRICE.design[state.design]?.price) rows.push({ label: PRICE.design[state.design].label, price: PRICE.design[state.design].price, kind: 'design' });
    state.features.forEach((key) => { if (PRICE.features[key]) rows.push({ label: PRICE.features[key].label, price: PRICE.features[key].price, kind: 'feature' }); });
    state.addons.forEach((key) => { if (PRICE.addons[key]) rows.push({ label: PRICE.addons[key].label, price: PRICE.addons[key].price, kind: 'addon' }); });
    return rows;
  };

  const persist = () => localStorage.setItem(STORAGE_KEY, JSON.stringify(state));

  const syncInputs = () => {
    $$('input[data-group], input[type="radio"]').forEach((input) => {
      const group = input.dataset.group || input.name;
      const active = Array.isArray(state[group]) ? state[group].includes(input.value) : state[group] === input.value;
      input.checked = active;
      input.closest('.choice-card')?.classList.toggle('is-selected', active);
    });
  };

  const renderSummary = () => {
    const rows = getBreakdown();
    const total = rows.reduce((sum, row) => sum + row.price, 0);
    const list = $('#quote-summary-list');
    if (list) {
      list.innerHTML = rows.map((row) => `<li><span>${row.label}</span><b>${row.price ? money(row.price) : '包含'}</b></li>`).join('');
    }
    $('#quote-total')?.replaceChildren(document.createTextNode(money(total)));
    $('#quote-summary-total')?.replaceChildren(document.createTextNode(money(total)));
    $('#quote-summary-state')?.replaceChildren(document.createTextNode(state.siteType ? PRICE.siteTypes[state.siteType].label : '尚未選擇網站類型'));
    $('#quote-selection-count')?.replaceChildren(document.createTextNode(`${rows.length} 個費用項目`));
    const final = $('#quote-final-breakdown');
    if (final) final.textContent = rows.map((row) => `${row.label}：${row.price ? money(row.price) : '包含'}`).join('\n') + `\n\n預估合計：${money(total)}`;
    $$('[data-next-step="1"]').forEach((button) => { button.disabled = !state.siteType; });
    syncInputs();
    persist();
  };

  const showStep = (step, shouldScroll = true) => {
    state.step = Math.max(0, Math.min(4, step));
    $$('[data-step-panel]').forEach((panel) => panel.classList.toggle('is-active', Number(panel.dataset.stepPanel) === state.step));
    $$('[data-step-button]').forEach((button) => {
      const target = Number(button.dataset.stepButton);
      button.classList.toggle('is-active', target === state.step);
      button.setAttribute('aria-current', target === state.step ? 'step' : 'false');
    });
    $$('[data-prev-step]').forEach((button) => { button.hidden = state.step === 0; });
    $$('[data-next-step]').forEach((button) => { button.hidden = Number(button.dataset.nextStep) !== state.step + 1; });
    $('#quote-step-label')?.replaceChildren(document.createTextNode(`STEP ${String(state.step + 1).padStart(2, '0')} / 05`));
    renderSummary();
    if (shouldScroll) document.querySelector('.quote-configurator')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
  };

  $$('input[data-group], input[type="radio"]').forEach((input) => {
    input.addEventListener('change', () => {
      const group = input.dataset.group || input.name;
      if (input.type === 'checkbox') {
        state[group] = $$(`input[data-group="${group}"]:checked`).map((item) => item.value);
      } else state[group] = input.value;
      renderSummary();
    });
  });

  $$('[data-step-button]').forEach((button) => button.addEventListener('click', () => {
    const target = Number(button.dataset.stepButton);
    if (target <= 0 || state.siteType || target === 0) showStep(target);
  }));
  $$('[data-next-step]').forEach((button) => button.addEventListener('click', () => {
    if (!button.disabled) showStep(Number(button.dataset.nextStep));
  }));
  $$('[data-prev-step]').forEach((button) => button.addEventListener('click', () => showStep(Number(button.dataset.prevStep))));

  $('#quote-reset')?.addEventListener('click', () => {
    state = emptyState();
    localStorage.removeItem(STORAGE_KEY);
    showStep(0);
  });

  $('#quote-copy')?.addEventListener('click', async () => {
    const text = $('#quote-final-breakdown')?.textContent || '';
    const status = $('#quote-copy-status');
    try {
      await navigator.clipboard.writeText(text);
      if (status) status.textContent = '估算摘要已複製；正式送出端點尚未接上。';
    } catch (_) {
      if (status) status.textContent = '瀏覽器未允許自動複製，請直接選取上方摘要。';
    }
  });

  $('#year')?.append(new Date().getFullYear());
  const menuToggle = $('.menu-toggle');
  const nav = $('.site-nav');
  menuToggle?.addEventListener('click', () => {
    const open = nav.classList.toggle('is-open');
    menuToggle.setAttribute('aria-expanded', String(open));
  });
  nav?.querySelectorAll('.nav-link:not(.nav-dropdown-toggle)').forEach((link) => link.addEventListener('click', () => {
    nav.classList.remove('is-open');
    menuToggle?.setAttribute('aria-expanded', 'false');
  }));
  const header = $('.site-header');
  const updateHeader = () => header?.classList.toggle('is-scrolled', window.scrollY > 24);
  updateHeader();
  window.addEventListener('scroll', updateHeader, { passive: true });

  syncInputs();
  showStep(state.step || 0, false);
})();
