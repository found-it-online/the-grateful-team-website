(function () {
  function initials(name) {
    var parts = name.trim().split(/\s+/);
    if (parts.length === 1) return parts[0].slice(0, 2).toUpperCase();
    return (parts[0][0] + parts[parts.length - 1][0]).toUpperCase();
  }

  function makeAvatar(name, url) {
    var el;
    if (url) {
      el = document.createElement('img');
      el.src = url;
      el.alt = '';
      el.loading = 'lazy';
    } else {
      el = document.createElement('span');
      el.textContent = initials(name);
      el.setAttribute('aria-hidden', 'true');
      el.className = 'rider-card-avatar-placeholder';
    }
    el.className = (el.className + ' rider-card-avatar').trim();
    return el;
  }

  fetch('/assets/data/participants.json')
    .then(function (r) { return r.json(); })
    .then(function (data) {
      // ── Member page: inject avatars into .rider-card elements ──────────
      var avatarMap = {};
      data.forEach(function (p) {
        avatarMap[p.displayName.toLowerCase()] = p.avatarImageURL || null;
      });

      document.querySelectorAll('.rider-card').forEach(function (card) {
        var nameEl = card.querySelector('.rider-card-name');
        if (!nameEl) return;
        var name = nameEl.textContent.trim();
        card.insertBefore(makeAvatar(name, avatarMap[name.toLowerCase()]), nameEl);
      });

      // ── Home page: build carousel ───────────────────────────────────────
      var track = document.getElementById('riders-carousel-track');
      if (track) {
        data.forEach(function (p) {
          var card = document.createElement('div');
          card.className = 'carousel-card';
          card.appendChild(makeAvatar(p.displayName, p.avatarImageURL));
          var nameEl = document.createElement('p');
          nameEl.className = 'carousel-card-name';
          nameEl.textContent = p.displayName;
          card.appendChild(nameEl);
          track.appendChild(card);
        });

        var prev = document.querySelector('.carousel-btn-prev');
        var next = document.querySelector('.carousel-btn-next');
        var scrollAmt = 360;
        if (prev) prev.addEventListener('click', function () { track.scrollBy({ left: -scrollAmt, behavior: 'smooth' }); });
        if (next) next.addEventListener('click', function () { track.scrollBy({ left:  scrollAmt, behavior: 'smooth' }); });
      }
    })
    .catch(function () {});

  // Mobile collapse — show 10, reveal rest on tap
  var grid = document.querySelector('.riders-grid');
  if (grid && window.innerWidth < 700) {
    var cards = Array.prototype.slice.call(grid.querySelectorAll('.rider-card'));
    var LIMIT = 10;
    if (cards.length > LIMIT) {
      cards.slice(LIMIT).forEach(function (c) { c.classList.add('rider-hidden'); });

      var btn = document.createElement('button');
      btn.className = 'riders-show-more';
      btn.textContent = 'Show all ' + cards.length + ' riders';
      grid.insertAdjacentElement('afterend', btn);

      btn.addEventListener('click', function () {
        cards.forEach(function (c) { c.classList.remove('rider-hidden'); });
        btn.remove();
      });
    }
  }
})();
