/* ═══════════════════════════════════════════════════════
   TGT site nav — partial injection, mobile drawer,
   dropdown, active-page highlighting
═══════════════════════════════════════════════════════ */
(function () {
  'use strict';

  const NAV_SLOT = 'nav-slot';
  const FOOTER_SLOT = 'footer-slot';

  function pageKey() {
    let path = window.location.pathname;
    if (path === '/' || path === '/index.html' || path.endsWith('/index.html')) return 'home';
    const file = path.split('/').pop() || '';
    return file.replace(/\.html$/, '');
  }

  function highlightActive(root) {
    const key = pageKey();
    const links = root.querySelectorAll('[data-nav-key]');
    links.forEach((link) => {
      if (link.getAttribute('data-nav-key') === key) {
        link.setAttribute('aria-current', 'page');
        const dropdown = link.closest('.nav-dropdown');
        if (dropdown) dropdown.setAttribute('data-active-child', 'true');
      }
    });
  }

  function wireDropdowns(root) {
    const dropdowns = root.querySelectorAll('.nav-dropdown');
    dropdowns.forEach((dd) => {
      const toggle = dd.querySelector('.nav-dropdown-toggle');
      if (!toggle) return;
      toggle.addEventListener('click', (e) => {
        e.stopPropagation();
        const open = dd.getAttribute('data-open') === 'true';
        document.querySelectorAll('.nav-dropdown').forEach((d) => d.setAttribute('data-open', 'false'));
        dd.setAttribute('data-open', open ? 'false' : 'true');
        toggle.setAttribute('aria-expanded', open ? 'false' : 'true');
      });
    });
    document.addEventListener('click', () => {
      document.querySelectorAll('.nav-dropdown').forEach((d) => d.setAttribute('data-open', 'false'));
    });
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        document.querySelectorAll('.nav-dropdown').forEach((d) => d.setAttribute('data-open', 'false'));
        document.body.removeAttribute('data-drawer-open');
        const tgl = document.querySelector('.nav-toggle');
        if (tgl) tgl.setAttribute('aria-expanded', 'false');
      }
    });
  }

  function wireDrawer(root) {
    const toggle = root.querySelector('.nav-toggle');
    if (!toggle) return;
    toggle.addEventListener('click', () => {
      const open = document.body.getAttribute('data-drawer-open') === 'true';
      document.body.setAttribute('data-drawer-open', open ? 'false' : 'true');
      toggle.setAttribute('aria-expanded', open ? 'false' : 'true');
      toggle.setAttribute('aria-label', open ? 'Open menu' : 'Close menu');
    });
    root.querySelectorAll('.nav-drawer a').forEach((a) => {
      a.addEventListener('click', () => {
        document.body.setAttribute('data-drawer-open', 'false');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.setAttribute('aria-label', 'Open menu');
      });
    });
  }

  async function inject(slotId, partialPath) {
    const slot = document.getElementById(slotId);
    if (!slot) return null;
    try {
      const res = await fetch(partialPath, { cache: 'no-cache' });
      if (!res.ok) throw new Error(`Failed to load ${partialPath}: ${res.status}`);
      slot.innerHTML = await res.text();
      return slot;
    } catch (err) {
      console.error('[nav.js]', err);
      slot.innerHTML = '<!-- partial load failed -->';
      return null;
    }
  }

  document.addEventListener('DOMContentLoaded', async () => {
    const navRoot = await inject(NAV_SLOT, '/partials/nav.html');
    await inject(FOOTER_SLOT, '/partials/footer.html');
    if (navRoot) {
      highlightActive(navRoot);
      wireDropdowns(navRoot);
      wireDrawer(navRoot);
    }
  });
})();
