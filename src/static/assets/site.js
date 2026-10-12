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

// Google Analytics 4 : chargé uniquement après accord du visiteur (bandeau cookies, règles CNIL).
(function () {
  var meta = document.querySelector('meta[name="ga-id"]');
  if (!meta) return;
  var id = meta.content, KEY = 'rs-cookies', MAX = 395 * 864e5; // choix gardé 13 mois
  var en = document.documentElement.lang === 'en';
  var txt = en
    ? { msg: 'We use cookies to measure site traffic (Google Analytics) and improve our service. Nothing is collected without your consent.', ok: 'Accept', no: 'Decline', label: 'Cookie consent' }
    : { msg: "Nous utilisons des cookies pour mesurer l'audience du site (Google Analytics) et l'améliorer. Rien n'est collecté sans votre accord.", ok: 'Accepter', no: 'Refuser', label: 'Consentement aux cookies' };

  function read() {
    try { var c = JSON.parse(localStorage.getItem(KEY)); return c && Date.now() - c.t < MAX ? c.v : null; } catch (e) { return null; }
  }
  function save(v) { try { localStorage.setItem(KEY, JSON.stringify({ v: v, t: Date.now() })); } catch (e) {} }

  var loaded = false;
  function load() {
    if (loaded) return; loaded = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { dataLayer.push(arguments); };
    gtag('js', new Date());
    gtag('config', id);
    // Demande de devis envoyée : la page merci / thanks compte comme conversion
    if (document.body.classList.contains('p-thanks')) gtag('event', 'generate_lead', { form: 'devis', language: en ? 'en' : 'fr' });
    var s = document.createElement('script');
    s.async = true; s.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(id);
    document.head.appendChild(s);
  }
  function clear() { // retire les cookies _ga déjà posés après un refus
    document.cookie.split(';').forEach(function (c) {
      var n = c.split('=')[0].trim();
      if (n.indexOf('_ga') === 0) ['', '.' + location.hostname.replace(/^www\./, '')].forEach(function (d) {
        document.cookie = n + '=; Max-Age=0; path=/' + (d ? '; domain=' + d : '');
      });
    });
  }

  var bar;
  function show() {
    if (bar) { bar.hidden = false; bar.querySelector('button').focus(); return; }
    bar = document.createElement('div');
    bar.className = 'cookie-bar'; bar.setAttribute('role', 'region'); bar.setAttribute('aria-label', txt.label);
    bar.innerHTML = '<p>' + txt.msg + '</p><div class="cookie-actions"><button type="button" class="btn ghost-light sm cookie-no">' + txt.no +
      '</button><button type="button" class="btn accent sm cookie-ok">' + txt.ok + '</button></div>';
    bar.addEventListener('click', function (e) {
      var b = e.target.closest('button'); if (!b) return;
      var ok = b.classList.contains('cookie-ok');
      save(ok ? 'yes' : 'no'); bar.hidden = true;
      if (ok) load(); else if (loaded) { clear(); location.reload(); } else clear();
    });
    document.body.appendChild(bar);
  }

  document.querySelectorAll('[data-cookies]').forEach(function (b) { b.addEventListener('click', show); });
  var c = read();
  if (c === 'yes') load(); else if (c !== 'no') show();
})();
