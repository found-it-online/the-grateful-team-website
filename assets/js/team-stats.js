// Updates elements with data-team-stat / data-team-progress.
// Tries DonorDrive team API first (near real-time), then falls back to /assets/data/team-stats.json.
// Attributes: data-team-stat="raised|goal|riders|percent|updated"

(function () {
  var TEAM_API = 'https://makeawishmichigan.donordrive.com/api/teams/5450';
  var FALLBACK_JSON = '/assets/data/team-stats.json';

  function fmt(n) {
    return '$' + Math.round(n).toLocaleString('en-US');
  }

  function normalizeStats(raw) {
    return {
      sumDonations: Number(raw.sumDonations) || 0,
      fundraisingGoal: Number(raw.fundraisingGoal) || 115000,
      numParticipants: Number(raw.numParticipants) || 0,
      updatedAt: raw.updatedDateUTC || raw.updatedAt || new Date().toISOString()
    };
  }

  function apply(d) {
    var pct = Math.min(100, Math.round((d.sumDonations / d.fundraisingGoal) * 100));

    document.querySelectorAll('[data-team-stat]').forEach(function (el) {
      switch (el.dataset.teamStat) {
        case 'raised':   el.textContent = fmt(d.sumDonations); break;
        case 'goal':     el.textContent = fmt(d.fundraisingGoal); break;
        case 'riders':   el.textContent = String(d.numParticipants); break;
        case 'percent':  el.textContent = pct + '%'; break;
        case 'updated':
          var dt = new Date(d.updatedAt);
          el.textContent = isNaN(dt.getTime())
            ? ''
            : dt.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
          break;
      }
    });

    document.querySelectorAll('[data-team-progress]').forEach(function (bar) {
      bar.style.width = pct + '%';
      bar.setAttribute('aria-valuenow', String(pct));
    });
  }

  fetch(TEAM_API, { headers: { Accept: 'application/json' } })
    .then(function (r) {
      if (!r.ok) throw new Error('DonorDrive team API unavailable');
      return r.json();
    })
    .then(function (team) {
      apply(normalizeStats(team));
    })
    .catch(function () {
      fetch(FALLBACK_JSON)
        .then(function (r) { return r.json(); })
        .then(function (d) { apply(normalizeStats(d)); })
        .catch(function () {
          // Silently fail — static fallback values may already be in the HTML
        });
    });
})();
