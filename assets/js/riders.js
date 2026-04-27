(function () {
  fetch('/assets/data/participants.json')
    .then(function (r) { return r.json(); })
    .then(function (data) {
      var avatarMap = {};
      data.forEach(function (p) {
        if (p.avatarImageURL) {
          avatarMap[p.displayName.toLowerCase()] = p.avatarImageURL;
        }
      });

      document.querySelectorAll('.rider-card').forEach(function (card) {
        var nameEl = card.querySelector('.rider-card-name');
        if (!nameEl) return;
        var url = avatarMap[nameEl.textContent.trim().toLowerCase()];
        if (!url) return;
        var img = document.createElement('img');
        img.src = url;
        img.alt = '';
        img.className = 'rider-card-avatar';
        img.loading = 'lazy';
        card.insertBefore(img, nameEl);
      });
    })
    .catch(function () {});
})();
