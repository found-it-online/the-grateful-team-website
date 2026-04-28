// Loads /assets/data/team-stats.json and updates any element with data-team-stat attributes.
// Attributes: data-team-stat="raised|goal|riders|percent|updated"
// Example: <span data-team-stat="raised"></span>

(function () {
  function fmt(n) {
    return '$' + Math.round(n).toLocaleString('en-US');
  }

  fetch('/assets/data/team-stats.json')
    .then(function (r) { return r.json(); })
    .then(function (d) {
      var pct = Math.min(100, Math.round((d.sumDonations / d.fundraisingGoal) * 100));

      document.querySelectorAll('[data-team-stat]').forEach(function (el) {
        switch (el.dataset.teamStat) {
          case 'raised':   el.textContent = fmt(d.sumDonations); break;
          case 'goal':     el.textContent = fmt(d.fundraisingGoal); break;
          case 'riders':   el.textContent = d.numParticipants; break;
          case 'percent':  el.textContent = pct + '%'; break;
          case 'updated':
            var dt = new Date(d.updatedAt);
            el.textContent = dt.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
            break;
        }
      });

      // Update any progress bar with data-team-progress
      document.querySelectorAll('[data-team-progress]').forEach(function (bar) {
        bar.style.width = pct + '%';
        bar.setAttribute('aria-valuenow', pct);
      });
    })
    .catch(function () {
      // Silently fail — static fallback values are already in the HTML
    });
})();
