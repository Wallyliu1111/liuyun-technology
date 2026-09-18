(() => {
  const dropdowns = [...document.querySelectorAll('.nav-dropdown')];
  const closeAll = (except = null) => dropdowns.forEach((dropdown) => {
    if (dropdown !== except) {
      dropdown.classList.remove('is-open');
      dropdown.querySelector('.nav-dropdown-toggle')?.setAttribute('aria-expanded', 'false');
    }
  });

  dropdowns.forEach((dropdown) => {
    const toggle = dropdown.querySelector('.nav-dropdown-toggle');
    if (!toggle) return;
    if (window.matchMedia('(hover: hover) and (min-width: 801px)').matches) {
      dropdown.addEventListener('mouseenter', () => {
        closeAll(dropdown);
        dropdown.classList.add('is-open');
        toggle.setAttribute('aria-expanded', 'true');
      });
      dropdown.addEventListener('mouseleave', () => {
        dropdown.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    }
    toggle.addEventListener('click', (event) => {
      event.preventDefault();
      event.stopPropagation();
      const open = dropdown.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', String(open));
      if (open) closeAll(dropdown);
    });
    toggle.addEventListener('keydown', (event) => {
      if (event.key === 'Escape') {
        closeAll();
        toggle.focus();
      }
    });
  });

  document.addEventListener('click', (event) => {
    if (!event.target.closest('.nav-dropdown')) closeAll();
  });
  document.querySelectorAll('.nav-dropdown-link').forEach((link) => {
    link.addEventListener('click', () => closeAll());
  });
})();
