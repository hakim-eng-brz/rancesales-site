(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var head = document.querySelector('.site-head');

  // En-tête compact au défilement
  function onScroll() { head && head.classList.toggle('scrolled', window.scrollY > 10); }
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  // Menu mobile
  var burger = document.querySelector('.burger');
  var nav = document.getElementById('nav');
  if (burger && nav) {
    burger.addEventListener('click', function () {
      var open = burger.getAttribute('aria-expanded') !== 'true';
      burger.setAttribute('aria-expanded', String(open));
      nav.classList.toggle('open', open);
    });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) { burger.setAttribute('aria-expanded', 'false'); nav.classList.remove('open'); }
    });
  }

  // Compteurs
  function count(el) {
    var target = parseInt(el.getAttribute('data-count'), 10);
    if (reduce || !target) { el.textContent = target; return; }
    var start = null, dur = 1400;
    function step(t) {
      if (!start) start = t;
      var p = Math.min((t - start) / dur, 1);
      el.textContent = Math.round(target * (1 - Math.pow(1 - p, 3)));
      if (p < 1) requestAnimationFrame(step);
    }
    el.textContent = '0';
    requestAnimationFrame(step);
  }

  // Apparitions au défilement
  var items = document.querySelectorAll('[data-reveal], .steps, [data-count]');
  if (!('IntersectionObserver' in window) || reduce) {
    items.forEach(function (el) { el.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add('in');
        if (e.target.hasAttribute('data-count')) count(e.target);
        io.unobserve(e.target);
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.12 });
    items.forEach(function (el) { io.observe(el); });
  }

  // Page produits : la gamme affichée est mise en avant dans la barre des gammes
  var rlinks = document.querySelectorAll('.range-nav a');
  if (rlinks.length && 'IntersectionObserver' in window) {
    var ro = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        rlinks.forEach(function (a) {
          var on = a.getAttribute('href') === '#' + e.target.id;
          if (on) { a.setAttribute('aria-current', 'true'); a.parentNode.scrollLeft = a.offsetLeft - 20; }
          else a.removeAttribute('aria-current');
        });
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    document.querySelectorAll('section.range').forEach(function (s) { ro.observe(s); });
  }

  // Mouvement réduit : arrêter les trajets animés de la carte
  if (reduce) document.querySelectorAll('animateMotion').forEach(function (a) { a.parentNode.remove(); });

  // Formulaire : message d'erreur après un envoi refusé
  var params = new URLSearchParams(location.search);
  var err = document.querySelector('.form-error');
  if (err && params.get('erreur')) err.hidden = false;
})();
