"""Génère le site statique Rance Sales dans le dossier de sortie : python3 build.py <out>"""
import os, sys, json, shutil, html
from urllib.parse import quote
from content import *

OUT = sys.argv[1]
SRC = os.path.dirname(os.path.abspath(__file__))
SITE = "https://rancesales.com"
E = html.escape

PATHS = {
 "home": ("/", "/en/"),
 "products": ("/produits/", "/en/products/"),
 "about": ("/a-propos/", "/en/about/"),
 "contact": ("/contact/", "/en/contact/"),
 "thanks": ("/merci/", "/en/thanks/"),
}
def path(key, l): return PATHS[key][0 if l=="fr" else 1]

ICONS = {
 "paper":'<path d="M4 7a3 3 0 1 0 6 0a3 3 0 1 0-6 0"/><path d="M7 4h11a3 3 0 0 1 0 6H7"/><path d="M10 7h11v10H8"/><path d="M4 7v10a3 3 0 0 0 6 0"/>',
 "box":'<path d="M3 7l9-4 9 4-9 4-9-4z"/><path d="M3 7v10l9 4 9-4V7"/><path d="M12 11v10"/>',
 "raw":'<path d="M12 3l9 5-9 5-9-5 9-5z"/><path d="M3 13l9 5 9-5"/><path d="M3 17.5l9 5 9-5"/>',
 "gear":'<circle cx="12" cy="12" r="3.2"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M4.9 19.1L7 17M17 7l2.1-2.1"/>',
 "spark":'<path d="M12 3v5M12 16v5M3 12h5M16 12h5"/><path d="M12 8l1.5 2.5L16 12l-2.5 1.5L12 16l-1.5-2.5L8 12l2.5-1.5z"/>',
 "wrench":'<path d="M14.5 6.5a4 4 0 0 0 5 5L12 19a2.1 2.1 0 0 1-3-3l7.5-7.5a4 4 0 0 0-2-2z"/>',
 "check":'<path d="M4 12.5l5 5L20 6.5"/>',
 "arrow":'<path d="M5 12h14M13 6l6 6-6 6"/>',
 "mail":'<path d="M3 6h18v12H3z"/><path d="M3 7l9 6 9-6"/>',
 "phone":'<path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 5a2 2 0 0 1 2-2"/>',
 "clock":'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "pin":'<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
 "in":'<path d="M4 9h3v11H4zM5.5 4a1.6 1.6 0 1 1 0 3.2a1.6 1.6 0 0 1 0-3.2zM10 9h3v1.6c.5-.9 1.7-1.8 3.4-1.8 3 0 3.6 2 3.6 4.6V20h-3v-5.6c0-1.3 0-3-1.8-3s-2.2 1.4-2.2 2.9V20h-3z"/>',
 "wa":'<path d="M17.47 14.38c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.16-.17.2-.35.22-.64.08-.3-.15-1.26-.46-2.39-1.48-.88-.79-1.48-1.76-1.65-2.06-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.18.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.61-.92-2.2-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48 0 1.46 1.07 2.88 1.21 3.07.15.2 2.1 3.2 5.08 4.49.71.31 1.26.49 1.7.63.71.22 1.36.19 1.87.12.57-.09 1.76-.72 2.01-1.42.25-.69.25-1.29.17-1.41-.07-.12-.27-.2-.57-.35M12.05 21.8h-.01a9.87 9.87 0 0 1-5.03-1.38l-.36-.21-3.74.98 1-3.65-.24-.37a9.86 9.86 0 0 1-1.51-5.26c0-5.45 4.44-9.88 9.89-9.88 2.64 0 5.12 1.03 6.99 2.9a9.83 9.83 0 0 1 2.89 6.99c0 5.45-4.44 9.88-9.89 9.88m8.41-18.3A11.8 11.8 0 0 0 12.05 0C5.5 0 .16 5.34.16 11.89c0 2.1.55 4.14 1.59 5.95L.06 24l6.3-1.65a11.9 11.9 0 0 0 5.69 1.45h.01c6.55 0 11.89-5.34 11.89-11.89 0-3.18-1.24-6.16-3.48-8.41"/>',
 "globe":'<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.6-3.8-9S9.5 5.6 12 3z"/>',
}
def icon(n, cls="ico"): return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true" focusable="false">{ICONS[n]}</svg>'

WORLD = json.load(open(os.path.join(SRC,"data","world.json")))
DESTS = ["na","sa","wa","me","ea","sa2","eas"]

def arc(o, d, bend=0.22):
  (x1,y1),(x2,y2) = o,d
  mx,my = (x1+x2)/2,(y1+y2)/2
  dx,dy = x2-x1,y2-y1
  cx,cy = mx - dy*bend, my + dx*bend
  if cy > my: cx,cy = mx + dy*bend, my - dx*bend   # toujours bombé vers le haut
  return f"M{x1} {y1} Q {cx:.0f} {cy:.0f} {x2} {y2}"

def route_map(l):
  o = WORLD["o"]
  r=[]; dots=[]; ends=[]
  for i,k in enumerate(DESTS):
    d = WORLD["pts"][k]
    r.append(f'<path id="rt-{k}" class="route" d="{arc(o,d)}" style="--d:{0.15+i*0.18:.2f}s"/>')
    dots.append(f'<circle class="ship" r="3.6"><animateMotion dur="{3.2+(i%3)*0.8:.1f}s" begin="{0.6+i*0.35:.2f}s" repeatCount="indefinite"><mpath href="#rt-{k}"/></animateMotion></circle>')
    ends.append(f'<g class="city"><circle class="pulse" cx="{d[0]}" cy="{d[1]}" r="5" style="animation-delay:{i*0.3:.1f}s"/><circle class="dot" cx="{d[0]}" cy="{d[1]}" r="4.5"/></g>')
  origin = f'<g class="origin"><circle class="pulse" cx="{o[0]}" cy="{o[1]}" r="8"/><circle cx="{o[0]}" cy="{o[1]}" r="7"/><text x="{o[0]+14}" y="{o[1]-10}">{"Europe" if l=="fr" else "Europe"}</text></g>'
  return f'''<figure class="map" aria-hidden="true">
<img src="/assets/world.svg" alt="" width="{WORLD["W"]}" height="{WORLD["H"]}" decoding="async">
<svg class="map-overlay" viewBox="0 0 {WORLD["W"]} {WORLD["H"]}" role="presentation">{"".join(r)}{"".join(dots)}{"".join(ends)}{origin}</svg>
</figure>'''

def wa_href(l): return WA + "?text=" + quote(WA_MSG[l])

def wa_link(l, cls):
  return f'<a class="{cls}" href="{wa_href(l)}" target="_blank" rel="noopener">{icon("wa","bi fill")} {"Écrire sur WhatsApp" if l=="fr" else "Message us on WhatsApp"}</a>'

def btn(href, label, cls="btn", ico="arrow"):
  return f'<a class="{cls}" href="{href}"><span>{E(label)}</span>{icon(ico,"bi")}</a>'

def faq_html(items):
  return '<div class="faq">' + "".join(f'<details data-reveal><summary><span>{E(q)}</span><i aria-hidden="true"></i></summary><div class="ans"><p>{E(a)}</p></div></details>' for q,a in items) + '</div>'

def faq_ld(items):
  return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in items]}

def marquee(l):
  i = 0 if l=="fr" else 1
  words = [w for r in RANGES for w in (r["n"][i],) + (r["key"] if l=="fr" else r["key_en"])] + (["Bobines et feuilles","Papeteries européennes"] if l=="fr" else ["Reels and sheets","European paper mills"])
  row = "".join(f'<li>{E(w)}</li>' for w in words)
  return f'<div class="marquee" aria-hidden="true"><ul>{row}{row}</ul></div>'

def gsm(v, l): return f'{v} g/m²' if l=="fr" else f'{v.replace(" ",",")} g/m²'

def range_anchor(r, l): return path("products",l) + "#" + r["id"][0 if l=="fr" else 1]

def range_cards(l):
  i = 0 if l=="fr" else 1; fr = l=="fr"
  out = []
  for n,r in enumerate(RANGES):
    tags = "".join(f'<li>{E(k)}</li>' for k in (r["key"] if fr else r["key_en"]))
    out.append(f'''<a class="card prod rcard" href="{range_anchor(r,l)}" data-reveal style="--i:{n}">{icon(r["icon"],"ico big")}<h3>{E(r["n"][i])}</h3>
<p class="span">{gsm(r["span"],l)} · {"bobines et feuilles" if fr else "reels and sheets"}</p><p>{E(r["intro"][i])}</p><ul class="tags">{tags}</ul>
<span class="more">{"Voir les qualités" if fr else "See all grades"}{icon("arrow","bi")}</span></a>''')
  return '<div class="grid g3">' + "".join(out) + '</div>'

def range_section(r, n, l):
  i = 0 if l=="fr" else 1; fr = l=="fr"
  cards = []
  for j,(tfr,ten,ggsm,grades) in enumerate(r["groups"]):
    rows = "".join(f'<li><span>{E(g[i])}</span>' + (f'<span class="gsm">{gsm(g[2],l)}</span>' if g[2] else '') + '</li>' for g in grades)
    head = f'<p class="gsm-all">{gsm(ggsm,l)}</p>' if ggsm else ''
    cards.append(f'<article class="gcard" data-reveal style="--i:{j%3}"><h3>{E(tfr if fr else ten)}</h3>{head}<ul class="spec">{rows}</ul></article>')
  return f'''<section class="sec range{" alt" if n%2 else ""}" id="{r["id"][i]}"><div class="wrap">
<div class="range-head" data-reveal><div><p class="eyebrow">{"Gamme" if fr else "Range"} {n+1:02d}</p><h2>{E(r["n"][i])}</h2><p class="lead-sm">{E(r["intro"][i])}</p></div>
<ul class="chips"><li>{icon(r["icon"],"bi")}{gsm(r["span"],l)}</li><li>{"Bobines et feuilles" if fr else "Reels and sheets"}</li></ul></div>
<div class="grid g3 grades">{"".join(cards)}</div>
</div></section>'''

def services_grid(l):
  return '<div class="grid g4">' + "".join(f'<article class="card prod" data-reveal style="--i:{i}">{icon(k,"ico big")}<h3>{E(t)}</h3><p>{E(d)}</p></article>' for i,(k,t,d) in enumerate(SERVICES[l])) + '</div>'

def catalog_ld(l):
  i = 0 if l=="fr" else 1
  return {"@context":"https://schema.org","@type":"OfferCatalog","name":"Rance Sales : " + ("papier et carton" if l=="fr" else "paper and board"),"url":SITE+path("products",l),
   "itemListElement":[{"@type":"OfferCatalog","name":r["n"][i],"itemListElement":[{"@type":"Offer","offeredBy":{"@id":SITE+"/#org"},"itemOffered":{"@type":"Product","name":g[i],"category":r["n"][i]}} for grp in r["groups"] for g in grp[3]]} for r in RANGES]}

def steps_html(l):
  return '<ol class="steps">' + "".join(f'<li data-reveal style="--i:{i}"><span class="n">{i+1:02d}</span><h3>{E(t)}</h3><p>{E(d)}</p></li>' for i,(t,d) in enumerate(STEPS[l])) + '</ol>'

def why_html(l):
  return '<div class="grid g3">' + "".join(f'<article class="why" data-reveal style="--i:{i}">{icon("check","ico")}<h3>{E(t)}</h3><p>{E(d)}</p></article>' for i,(t,d) in enumerate(WHY[l])) + '</div>'

def cta_band(l):
  href = path("contact",l) + "#devis"
  if l=="fr":
    return f'''<section class="cta-band"><div class="wrap cta-in" data-reveal>
<div><h2>Parlons de votre prochain approvisionnement</h2><p>Indiquez-nous la qualité, le volume et le pays de livraison. Nous vous répondons avec une offre adaptée.</p></div>
<div class="cta-actions">{btn(href,"Demander un devis","btn accent")}<a class="cta-tel" href="tel:{TEL}">{icon("phone","bi")} {TEL_H}</a>{wa_link(l,"cta-tel")}</div></div></section>'''
  return f'''<section class="cta-band"><div class="wrap cta-in" data-reveal>
<div><h2>Let's talk about your next supply</h2><p>Tell us the grade, volume and delivery country. We will reply with a tailored offer.</p></div>
<div class="cta-actions">{btn(href,"Request a quote","btn accent")}<a class="cta-tel" href="tel:{TEL}">{icon("phone","bi")} {TEL_H}</a>{wa_link(l,"cta-tel")}</div></div></section>'''


# ---------- pages ----------
def p_home(l):
  fr = l=="fr"
  h = f"""<section class="hero dark"><div class="wrap hero-in">
<div class="hero-copy">
<p class="eyebrow" data-reveal>{"Négoce international de papier · De l'Europe au monde entier" if fr else "International paper trading · From Europe to the world"}</p>
<h1 data-reveal style="--i:1">{"Votre papier industriel, sourcé en Europe, livré dans le monde entier" if fr else "Industrial paper sourced in Europe, delivered worldwide"}</h1>
<p class="lead" data-reveal style="--i:2">{"Rance Sales relie les papeteries européennes aux fabricants d'emballage, imprimeurs et transformateurs, partout dans le monde." if fr else "Rance Sales connects European paper mills with packaging manufacturers, printers and converters around the world."}</p>
<div class="actions" data-reveal style="--i:3">{btn(path("contact",l)+"#devis","Demander un devis" if fr else "Request a quote","btn accent")}{btn(path("products",l),"Voir les produits" if fr else "See our products","btn ghost-light","arrow")}</div>
<ul class="trust" data-reveal style="--i:4"><li>{icon("pin","bi")}{"Siège à Rennes, France" if fr else "Head office in Rennes, France"}</li><li>{icon("globe","bi")}{"Clients dans le monde entier" if fr else "Customers worldwide"}</li><li>{icon("clock","bi")}{"Lun–ven, 8 h–19 h" if fr else "Mon–Fri, 8 am–7 pm"}</li></ul>
</div>
{route_map(l)}
</div></section>
{marquee(l)}
<section class="sec"><div class="wrap">
<div class="sec-head" data-reveal><p class="eyebrow">{"Notre métier" if fr else "What we do"}</p><h2>{"Votre lien entre les papeteries européennes et votre usine" if fr else "Your link between European paper mills and your plant"}</h2>
<p class="lead-sm">{"Nous gérons la sélection des qualités, la constance d'un lot à l'autre et le suivi export, pour que vous receviez le bon papier au bon moment, où que vous soyez." if fr else "We handle grade selection, batch-to-batch consistency and export follow-up, so you receive the right paper at the right time, wherever you are."}</p></div>
{steps_html(l)}
</div></section>
<section class="sec alt"><div class="wrap">
<div class="sec-head split" data-reveal><div><p class="eyebrow">{"Produits" if fr else "Products"}</p><h2>{"Papier graphique, papier d'emballage et carton" if fr else "Graphic paper, packaging paper and board"}</h2></div>{btn(path("products",l),"Toutes les qualités" if fr else "All grades","link")}</div>
{range_cards(l)}
<p class="also" data-reveal>{"Également : emballage sur mesure, machines de transformation, services personnalisés et support technique." if fr else "Also: custom packaging, processing machinery, custom services and technical support."}</p>
</div></section>
<section class="sec dark stats-sec"><div class="wrap stats-in">
<div data-reveal><p class="eyebrow">{"Pourquoi Rance Sales" if fr else "Why Rance Sales"}</p><h2>{"Un expert français des matières premières pour l'emballage et la papeterie" if fr else "A French expert in raw materials for packaging and stationery"}</h2></div>
<dl class="stats"><div data-reveal><dt><span data-count="100">100</span>+</dt><dd>{"produits innovants, performants et écologiques" if fr else "innovative, high-performance and eco-friendly products"}</dd></div><div data-reveal style="--i:1"><dt><span data-count="15">15</span></dt><dd>{"échanges internationaux" if fr else "international exchanges"}</dd></div></dl>
</div><div class="wrap">{why_html(l)}</div></section>
<section class="sec"><div class="wrap narrow">
<div class="sec-head" data-reveal><p class="eyebrow">FAQ</p><h2>{"Questions fréquentes" if fr else "Frequently asked questions"}</h2></div>
{faq_html(HOME_FAQ[l])}
</div></section>
{cta_band(l)}"""
  return h, [faq_ld(HOME_FAQ[l])]

def page_head(l, eyebrow, h1, lead, extra=""):
  return f"""<section class="page-head dark"><div class="wrap ph-in"><div>
<p class="eyebrow" data-reveal>{E(eyebrow)}</p><h1 data-reveal style="--i:1">{E(h1)}</h1><p class="lead" data-reveal style="--i:2">{E(lead)}</p>{extra}</div></div></section>"""

def p_products(l):
  fr = l=="fr"; i = 0 if fr else 1
  h = page_head(l, "Produits" if fr else "Products",
      "Papier graphique, papier d'emballage et carton" if fr else "Graphic paper, packaging paper and board",
      "Plus de 50 qualités de papier et de carton, de 20 à 1 500 g/m², en bobines et en feuilles, sourcées auprès de papeteries européennes." if fr else "More than 50 paper and board grades, from 20 to 1,500 g/m², in reels and sheets, sourced from European paper mills.",
      f'<div class="actions" data-reveal style="--i:3">{btn(path("contact",l)+"#devis","Demander un devis" if fr else "Request a quote","btn accent")}</div>')
  nav = "".join(f'<a href="#{r["id"][i]}">{icon(r["icon"],"ico")}<b>{E(r["n"][i])}</b><small>{gsm(r["span"],l)}</small></a>' for r in RANGES)
  h += f'<nav class="range-nav" aria-label="{"Gammes" if fr else "Ranges"}"><div class="wrap">{nav}</div></nav>'
  h += "".join(range_section(r, n, l) for n,r in enumerate(RANGES))
  h += f"""<section class="sec{" alt" if len(RANGES)%2 else ""}"><div class="wrap">
<div class="sec-head" data-reveal><p class="eyebrow">{"Au-delà du papier" if fr else "Beyond paper"}</p><h2>{"Emballage, machines et services" if fr else "Packaging, machinery and services"}</h2>
<p class="lead-sm">{"Disponibilités, formats et délais sur demande : précisez la qualité, le grammage et le volume dont vous avez besoin, nous trouvons la bonne source." if fr else "Availability, formats and lead times on request: tell us the grade, grammage and volume you need, and we find the right source."}</p></div>
{services_grid(l)}
</div></section>
<section class="sec{"" if len(RANGES)%2 else " alt"}"><div class="wrap">
<div class="sec-head" data-reveal><p class="eyebrow">{"Comment ça marche" if fr else "How it works"}</p><h2>{"De la papeterie européenne à votre usine" if fr else "From European paper mills to your plant"}</h2></div>
{steps_html(l)}
</div></section>
{cta_band(l)}"""
  return h, [catalog_ld(l)]

def p_about(l):
  fr = l=="fr"
  h = page_head(l, "À propos" if fr else "About",
      "Un négociant français, des clients dans le monde entier" if fr else "A French trading company with customers worldwide",
      "Rance Sales est un expert français de la fourniture de matières premières de haute qualité pour les industries de l'emballage et de la papeterie." if fr else "Rance Sales is a French expert in high-quality raw materials for the packaging and stationery industries.")
  h += f"""<section class="sec"><div class="wrap about-grid">
<div data-reveal><h2>{"Notre rôle" if fr else "Our role"}</h2>
<p class="lead-sm">{"Nous proposons des solutions sur mesure aux fabricants de papier et d'emballage, conformes aux standards exigeants du marché. Nous travaillons avec des papeteries européennes et accompagnons nos clients à l'international, de la sélection des qualités jusqu'au suivi export." if fr else "We provide tailored solutions for paper and packaging manufacturers that meet demanding market standards. We work with European paper mills and support our customers internationally, from grade selection to export follow-up."}</p>
<p class="lead-sm">{"Basés à Rennes, nous répondons du lundi au vendredi, de 8 h à 19 h (heure de Paris)." if fr else "Based in Rennes, France, we are available Monday to Friday, 8 am to 7 pm (Paris time)."}</p></div>
<dl class="stats light" data-reveal style="--i:1"><div><dt><span data-count="100">100</span>+</dt><dd>{"produits innovants, performants et écologiques" if fr else "innovative, high-performance and eco-friendly products"}</dd></div><div><dt><span data-count="15">15</span></dt><dd>{"échanges internationaux" if fr else "international exchanges"}</dd></div></dl>
</div></section>
<section class="sec alt"><div class="wrap">
<div class="sec-head" data-reveal><p class="eyebrow">{"Nos valeurs" if fr else "Our values"}</p><h2>{"Ce qui nous distingue" if fr else "What sets us apart"}</h2></div>
{why_html(l)}</div></section>
{cta_band(l)}"""
  return h, []

def p_contact(l):
  fr = l=="fr"
  popt = "".join(f'<option>{E(t)}</option>' for t in [r["n"][0 if fr else 1] for r in RANGES] + [SERVICES[l][0][1], SERVICES[l][1][1], "Autre" if fr else "Other"])
  L = (lambda a,b: a if fr else b)
  form = f"""<form class="quote" id="devis" action="/contact.php" method="post" data-reveal>
<input type="hidden" name="lang" value="{l}">
<div class="hp" aria-hidden="true"><label for="website">Website</label><input id="website" name="website" tabindex="-1" autocomplete="off"></div>
<p class="form-error" hidden role="alert">{L("L'envoi n'a pas abouti. Vérifiez votre nom, votre pays et votre e-mail, ou écrivez-nous directement à "+EMAIL+".","Your request could not be sent. Check your name, country and email, or write to us directly at "+EMAIL+".")}</p>
<div class="fields">
<label><span>{L("Nom et prénom","Full name")} *</span><input id="f-name" name="name" required autocomplete="name"></label>
<label><span>{L("Société","Company")}</span><input id="f-company" name="company" autocomplete="organization"></label>
<label><span>{L("Pays de livraison","Delivery country")} *</span><input id="f-country" name="country" required autocomplete="country-name"></label>
<label><span>E-mail *</span><input id="f-email" type="email" name="email" required autocomplete="email"></label>
<label><span>{L("Téléphone","Phone")}</span><input id="f-phone" type="tel" name="phone" autocomplete="tel"></label>
<label><span>{L("Produit recherché","Product needed")}</span><select id="f-product" name="product"><option value="">{L("Choisir…","Choose…")}</option>{popt}</select></label>
<label class="full"><span>{L("Volume estimé","Estimated volume")}</span><input id="f-volume" name="volume" placeholder="{L("Ex. : 25 tonnes par mois","E.g. 25 tonnes per month")}"></label>
<label class="full"><span>{L("Votre besoin","Your request")}</span><textarea id="f-message" name="message" rows="5" placeholder="{L("Qualité, grammage, ville de livraison, délai…","Grade, grammage, delivery city, lead time…")}"></textarea></label>
<label class="check full"><input id="f-wa" type="checkbox" name="whatsapp" value="1"><span>{L("Je préfère être recontacté par WhatsApp","I prefer to be contacted on WhatsApp")}</span></label>
</div>
<button class="btn accent" type="submit"><span>{L("Envoyer ma demande de devis","Send my quote request")}</span>{icon("arrow","bi")}</button>
<p class="fine">{L("Vos informations servent uniquement à répondre à votre demande.","Your details are only used to answer your request.")}</p>
</form>"""
  side = f"""<aside class="contact-side" data-reveal style="--i:1">
<h2 class="h3">{L("Contact direct","Direct contact")}</h2>
<ul class="clist">
<li>{icon("mail","ico")}<div><span>E-mail</span><a href="mailto:{EMAIL}">{EMAIL}</a></div></li>
<li>{icon("phone","ico")}<div><span>{L("Téléphone","Phone")}</span><a href="tel:{TEL}">{TEL_H}</a></div></li>
<li>{icon("wa","ico fill")}<div><span>WhatsApp</span><a href="{wa_href(l)}" target="_blank" rel="noopener">{TEL_H}</a></div></li>
<li>{icon("clock","ico")}<div><span>{L("Horaires","Hours")}</span>{UI[l]["hours"]}</div></li>
<li>{icon("pin","ico")}<div><span>{L("Siège","Head office")}</span>Rennes, France</div></li>
<li>{icon("in","ico fill")}<div><span>LinkedIn</span><a href="{LI}" rel="noopener">rance-sales</a></div></li>
</ul></aside>"""
  h = page_head(l, L("Contact","Contact"), L("Demandez votre devis","Request your quote"),
      L("Décrivez-nous votre besoin : qualité, volume, pays de livraison. Nous revenons vers vous avec une offre adaptée.","Tell us what you need: grade, volume and delivery country. We will get back to you with a tailored offer."))
  h += f'<section class="sec"><div class="wrap contact-grid">{form}{side}</div></section>'
  return h, []

def p_thanks(l):
  fr = l=="fr"
  h = page_head(l, "Merci" if fr else "Thank you", "Votre demande est bien envoyée" if fr else "Your request has been sent",
      "Nous l'étudions et revenons vers vous rapidement. Pour une demande urgente, appelez le " + TEL_H + "." if fr else "We are reviewing it and will get back to you shortly. For urgent requests, call " + TEL_H + ".",
      f'<div class="actions">{btn(path("home",l),"Retour à l\'accueil" if fr else "Back to home","btn accent")}</div>')
  return h, []

PAGES = {"home":p_home,"products":p_products,"about":p_about,"contact":p_contact,"thanks":p_thanks}
META = {
 "home":{"fr":("Rance Sales | Négoce international de papier industriel et emballage","Papier graphique, papier d'emballage et carton (kraftliner, testliner, couché, GC1…) de papeteries européennes pour les industriels du monde entier. Devis rapide."),
         "en":("Rance Sales | International Industrial Paper and Packaging Trading","Graphic paper, packaging paper and board (kraftliner, testliner, coated, GC1…) from European paper mills for manufacturers worldwide. Request a quote.")},
 "products":{"fr":("Papier graphique, papier d'emballage et carton | Rance Sales","Kraftliner, testliner, kraft, papier couché, offset, LWC, carton GC1, GC2, SBS… plus de 50 qualités de 20 à 1 500 g/m², en bobines et en feuilles."),
         "en":("Graphic Paper, Packaging Paper and Board | Rance Sales","Kraftliner, testliner, kraft, coated, offset, LWC, GC1, GC2 and SBS board… more than 50 grades from 20 to 1,500 g/m², in reels and sheets.")},
 "about":{"fr":("À propos de Rance Sales | Négoce de papier, Rennes","Rance Sales, société française basée à Rennes, fournit des matières premières de haute qualité aux industries de l'emballage et de la papeterie dans le monde entier."),
         "en":("About Rance Sales | Paper Trading, Rennes, France","Rance Sales, a French company based in Rennes, supplies high-quality raw materials to the packaging and stationery industries worldwide.")},
 "contact":{"fr":("Demande de devis papier industriel | Rance Sales","Demandez un devis pour du papier industriel, des emballages ou des matières premières. E-mail commercial@rancesales.com, tél. +33 6 73 76 70 59."),
         "en":("Request a Quote for Industrial Paper | Rance Sales","Request a quote for industrial paper, packaging or raw materials. Email commercial@rancesales.com, phone +33 6 73 76 70 59.")},
 "thanks":{"fr":("Merci | Rance Sales","Votre demande de devis a bien été envoyée."),"en":("Thank you | Rance Sales","Your quote request has been sent.")},
}

ORG = {"@context":"https://schema.org","@type":"Organization","@id":SITE+"/#org","name":"Rance Sales","url":SITE+"/","logo":SITE+"/assets/logo.png",
 "description":"Négoce international de papier industriel, matières premières et emballages entre papeteries européennes et industriels du monde entier.",
 "email":EMAIL,"telephone":TEL,"address":{"@type":"PostalAddress","addressLocality":"Rennes","addressCountry":"FR"},
 "areaServed":"Worldwide","sameAs":[LI],
 "contactPoint":{"@type":"ContactPoint","contactType":"sales","email":EMAIL,"telephone":TEL,"availableLanguage":["fr","en"],
   "hoursAvailable":{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"08:00","closes":"19:00"}}}

def nav_html(l, key):
  ui = UI[l]
  return "".join(f'<a href="{path(k,l)}"{" aria-current=\"page\"" if key==k else ""}>{label}</a>' for k,label in ui["nav"])

def render(l, key, body, extra_ld):
  ui = UI[l]
  title, desc = META[key][l]
  fr_p, en_p = PATHS[key]; self_p = path(key,l); other_p = en_p if l=="fr" else fr_p
  ld = [ORG]
  if key=="home": ld.append({"@context":"https://schema.org","@type":"WebSite","@id":SITE+"/#site","name":"Rance Sales","url":SITE+"/","inLanguage":["fr","en"],"publisher":{"@id":SITE+"/#org"}})
  else:
    crumbs=[{"@type":"ListItem","position":1,"name":ui["breadcrumb_home"],"item":SITE+path("home",l)}]
    crumbs.append({"@type":"ListItem","position":len(crumbs)+1,"name":title.split(" | ")[0],"item":SITE+self_p})
    ld.append({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":crumbs})
  ld += extra_ld
  ldtxt = "\n".join(f'<script type="application/ld+json">{json.dumps(x,ensure_ascii=False)}</script>' for x in ld)
  robots = "noindex, follow" if key=="thanks" else "index, follow, max-image-preview:large"
  alt = "" if key=="thanks" else f'''<link rel="alternate" hreflang="fr" href="{SITE}{fr_p}">
<link rel="alternate" hreflang="en" href="{SITE}{en_p}">
<link rel="alternate" hreflang="x-default" href="{SITE}{fr_p}">'''
  mk = "".join(f'<li><a href="{path(k,l)}">{label}</a></li>' for k,label in ui["nav"])
  doc = f'''<!doctype html>
<html lang="{l}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{SITE}{self_p}">
{alt}
<meta name="theme-color" content="#ffffff">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Rance Sales">
<meta property="og:locale" content="{ui['locale']}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{SITE}{self_p}">
<meta property="og:image" content="{SITE}/assets/og-{l}.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@75..100,500..800&family=Source+Sans+3:wght@400;600&display=swap">
<link rel="stylesheet" href="/assets/site.css">
<script>document.documentElement.classList.add('js')</script>
{ldtxt}
</head>
<body class="p-{key}">
<a class="skip" href="#main">{ui['skip']}</a>
<header class="site-head"><div class="wrap hd">
<a class="brand" href="{path('home',l)}">{LOGO}</a>
<button class="burger" type="button" aria-expanded="false" aria-controls="nav"><span></span><span></span><span class="sr">{ui['menu']}</span></button>
<nav id="nav" aria-label="{'Navigation principale' if l=='fr' else 'Main navigation'}">{nav_html(l,key)}
<a class="lang" href="{other_p}" hreflang="{ui['other']}" lang="{ui['other']}">{ui['other_short']}<span class="sr"> {ui['other_label']}</span></a>
<a class="btn accent sm" href="{path('contact',l)}#devis"><span>{ui['cta']}</span></a></nav>
</div></header>
<main id="main">
{body}
</main>
<footer class="site-foot"><div class="wrap ft">
<div class="ft-brand">{LOGO_LIGHT}<p>{ui['foot_tag']}</p></div>
<div><h2 class="ft-h">{ui['nav_label']}</h2><ul>{mk}</ul></div>
<div><h2 class="ft-h">Contact</h2><ul><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="tel:{TEL}">{TEL_H}</a></li><li><a href="{wa_href(l)}" target="_blank" rel="noopener">WhatsApp</a></li><li>{ui['hours']}</li></ul></div>
<div><h2 class="ft-h">Rance Sales</h2><ul><li><a href="{path('products',l)}">{dict(ui['nav'])['products']}</a></li><li><a href="{LI}" rel="noopener">LinkedIn</a></li><li><a href="{other_p}" hreflang="{ui['other']}" lang="{ui['other']}">{ui['other_label']}</a></li></ul></div>
</div><div class="wrap ft-bottom"><p>© 2024–2026 Rance Sales. {ui['rights']}</p></div></footer>
<a class="wa-float" href="{wa_href(l)}" target="_blank" rel="noopener" aria-label="{"Écrire à Rance Sales sur WhatsApp" if l=="fr" else "Message Rance Sales on WhatsApp"}">{icon("wa","ico fill")}<span class="wa-tip" aria-hidden="true">{"Écrire sur WhatsApp" if l=="fr" else "Chat on WhatsApp"}</span></a>
<script src="/assets/site.js" defer></script>
</body>
</html>
'''
  d = os.path.join(OUT, self_p.strip("/")); os.makedirs(d, exist_ok=True)
  open(os.path.join(d,"index.html"),"w").write(doc)

# Logo d'origine de Rance Sales : version sombre pour l'en-tête blanc, version claire pour le pied de page.
LOGO = '<img class="logo" src="/assets/logo-rance-sales.png" alt="Rance Sales" width="346" height="86">'
LOGO_LIGHT = '<img class="logo" src="/assets/logo-rance-sales-light.png" alt="Rance Sales" width="346" height="86" loading="lazy">'

os.makedirs(OUT, exist_ok=True)
for l in ["fr","en"]:
  for k,fn in PAGES.items():
    b, ld = fn(l); render(l,k,b,ld)

# static files
shutil.copytree(os.path.join(SRC,"static"), OUT, dirs_exist_ok=True)

# carte du monde aux couleurs du logo
os.makedirs(os.path.join(OUT,"assets"), exist_ok=True)
open(os.path.join(OUT,"assets","world.svg"),"w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WORLD["W"]} {WORLD["H"]}"><defs><path id="l" d="{WORLD["land"]}"/><pattern id="d" width="6" height="6" patternUnits="userSpaceOnUse"><circle cx="3" cy="3" r="1.4" fill="{PALETTE["dot"]}"/></pattern></defs><use href="#l" fill="{PALETTE["land"]}"/><use href="#l" fill="url(#d)"/></svg>')

# sitemap
urls=[]
for k,(f,e) in PATHS.items():
  if k=="thanks": continue
  pr = "1.0" if k=="home" else ("0.9" if k=="contact" else "0.8")
  for loc in (f,e):
    urls.append(f'<url><loc>{SITE}{loc}</loc><xhtml:link rel="alternate" hreflang="fr" href="{SITE}{f}"/><xhtml:link rel="alternate" hreflang="en" href="{SITE}{e}"/><xhtml:link rel="alternate" hreflang="x-default" href="{SITE}{f}"/><priority>{pr}</priority></url>')
open(os.path.join(OUT,"sitemap.xml"),"w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'+"\n".join(urls)+"\n</urlset>\n")
print("built", sum(len(fs) for _,_,fs in os.walk(OUT)), "files")
