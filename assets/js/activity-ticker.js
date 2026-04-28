/**
 * Activity Ticker — shows recent donations + new riders at the bottom of every page.
 * Tries DonorDrive API directly first (real-time), falls back to /assets/data/activity-feed.json.
 * Dismissed state is stored in sessionStorage so it stays gone until the tab is closed.
 */
(function () {
  'use strict';

  var TEAM_ID   = 5450;
  var API_BASE  = 'https://makeawishmichigan.donordrive.com/api/teams/' + TEAM_ID;
  var LOCAL_URL = '/assets/data/activity-feed.json';
  var SESSION_KEY = 'tgt-ticker-dismissed';
  var ROTATE_MS   = 5500;

  if (sessionStorage.getItem(SESSION_KEY)) return;

  // ── Helpers ────────────────────────────────────────────────────────────────
  function timeAgo(utcStr) {
    var diff = Math.floor((Date.now() - new Date(utcStr).getTime()) / 1000);
    if (diff < 120)    return 'just now';
    if (diff < 3600)   return Math.floor(diff / 60) + 'm ago';
    if (diff < 86400)  return Math.floor(diff / 3600) + 'h ago';
    var d = Math.floor(diff / 86400);
    return d === 1 ? 'yesterday' : d + 'd ago';
  }

  function fmtAmount(n) {
    return '$' + Math.round(n).toLocaleString('en-US');
  }

  // ── Build feed items from raw API data ────────────────────────────────────
  function buildItems(donations, participants) {
    var items = [];

    // Recent donations (skip reg fees)
    (donations || []).slice(0, 20).forEach(function (d) {
      if (d.isRegFee) return;
      var who  = d.displayName || 'A supporter';
      var amt  = fmtAmount(d.amount);
      var self = d.donorIsRecipient || d.displayName === d.recipientName;
      var text = self
        ? who + ' donated ' + amt + ' to the team'
        : who + ' donated ' + amt + ' to ' + d.recipientName;
      items.push({ type: 'donation', text: text, time: d.createdDateUTC });
    });

    // Recently joined riders — anyone who joined in the last 60 days
    var cutoff = Date.now() - 60 * 86400 * 1000;
    (participants || []).forEach(function (p) {
      if (new Date(p.createdDateUTC).getTime() > cutoff) {
        items.push({
          type: 'rider',
          text: p.displayName + ' just joined the team!',
          time: p.createdDateUTC
        });
      }
    });

    // Newest first
    items.sort(function (a, b) { return new Date(b.time) - new Date(a.time); });
    return items.slice(0, 25);
  }

  // ── Render ticker bar ─────────────────────────────────────────────────────
  function render(items) {
    if (!items || !items.length) return;

    var bar = document.createElement('div');
    bar.id = 'tgt-ticker';
    bar.setAttribute('role', 'status');
    bar.setAttribute('aria-live', 'polite');
    bar.innerHTML =
      '<div class="tgt-ticker-inner">' +
        '<span class="tgt-ticker-icon" id="tgt-ticker-icon" aria-hidden="true"></span>' +
        '<span class="tgt-ticker-label" id="tgt-ticker-label"></span>' +
        '<span class="tgt-ticker-text"  id="tgt-ticker-text"></span>' +
        '<span class="tgt-ticker-time"  id="tgt-ticker-time"></span>' +
        '<a href="/donate.html" class="tgt-ticker-cta">Donate →</a>' +
        '<button class="tgt-ticker-close" id="tgt-ticker-close" aria-label="Dismiss ticker">&#x2715;</button>' +
      '</div>';

    document.body.appendChild(bar);

    var idx = 0;

    function update(i) {
      var item = items[i % items.length];
      var isDonation = item.type === 'donation';
      document.getElementById('tgt-ticker-icon').textContent  = isDonation ? '💛' : '🚲';
      document.getElementById('tgt-ticker-label').textContent = isDonation ? 'Donation' : 'New rider';
      document.getElementById('tgt-ticker-label').className   = 'tgt-ticker-label tgt-ticker-label-' + item.type;
      document.getElementById('tgt-ticker-text').textContent  = item.text;
      document.getElementById('tgt-ticker-time').textContent  = timeAgo(item.time);
    }

    update(0);

    // Fade-rotate
    var timer = setInterval(function () {
      bar.classList.add('tgt-ticker-out');
      setTimeout(function () {
        if (!document.getElementById('tgt-ticker-text')) { clearInterval(timer); return; }
        idx++;
        update(idx);
        bar.classList.remove('tgt-ticker-out');
      }, 350);
    }, ROTATE_MS);

    document.getElementById('tgt-ticker-close').addEventListener('click', function () {
      sessionStorage.setItem(SESSION_KEY, '1');
      clearInterval(timer);
      bar.classList.add('tgt-ticker-out');
      setTimeout(function () { if (bar.parentNode) bar.parentNode.removeChild(bar); }, 400);
    });
  }

  // ── Data fetching: live → local fallback ──────────────────────────────────
  function fetchLive() {
    return Promise.all([
      fetch(API_BASE + '/donations?limit=20&orderBy=createdDateUTC&desc=true').then(function (r) { return r.json(); }),
      fetch(API_BASE + '/participants?limit=51&orderBy=createdDateUTC&desc=true').then(function (r) { return r.json(); })
    ]);
  }

  function fetchLocal() {
    return fetch(LOCAL_URL)
      .then(function (r) { return r.json(); })
      .then(function (d) { return [d.donations || [], d.participants || []]; });
  }

  fetchLive()
    .then(function (res) { render(buildItems(res[0], res[1])); })
    .catch(function ()   {
      fetchLocal()
        .then(function (res) { render(buildItems(res[0], res[1])); })
        .catch(function () {});
    });
})();
