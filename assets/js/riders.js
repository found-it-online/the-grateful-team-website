(function () {
  function initials(name) {
    var parts = name.trim().split(/\s+/);
    if (parts.length === 1) return parts[0].slice(0, 2).toUpperCase();
    return (parts[0][0] + parts[parts.length - 1][0]).toUpperCase();
  }

  fetch('/assets/data/participants.json')
    .then(function (r) { return r.json(); })
    .then(function (data) {
      var avatarMap = {};
      data.forEach(function (p) {
        avatarMap[p.displayName.toLowerCase()] = p.avatarImageURL || null;
      });

      document.querySelectorAll('.rider-card').forEach(function (card) {
        var nameEl = card.querySelector('.rider-card-name');
        if (!nameEl) return;
        var name = nameEl.textContent.trim();
        var url = avatarMap[name.toLowerCase()];
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
          el.className += ' rider-card-avatar-placeholder';
        }
        el.className = (el.className + ' rider-card-avatar').trim();
        card.insertBefore(el, nameEl);
      });
    })
    .catch(function () {});
})();
