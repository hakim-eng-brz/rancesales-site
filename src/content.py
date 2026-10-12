# Contenu du site Rance Sales (FR / EN). Ne contient que des informations confirmées par Rance Sales.
EMAIL = "commercial@rancesales.com"
TEL = "+33673767059"; TEL_H = "+33 6 73 76 70 59"
WA = "https://wa.me/33673767059"  # même numéro, joignable sur WhatsApp
WA_MSG = {"fr": "Bonjour Rance Sales, je souhaite un devis pour : ", "en": "Hello Rance Sales, I would like a quote for: "}
LI = "https://www.linkedin.com/company/rance-sales"
# Google Analytics 4 : ID de mesure (G-XXXXXXXXXX). Vide = pas de statistiques ni de bandeau cookies.
# La balise ne se charge qu'après accord du visiteur dans le bandeau cookies (règles CNIL).
GA_ID = "G-GVYZ14ZW8T"

# Gammes de papier et carton (grammages en g/m², livrés en bobines et en feuilles).
# Chaque groupe : (titre FR, titre EN, grammage du groupe ou None, [(qualité FR, qualité EN, grammage ou None)])
RANGES = [
 {"id":("papier-graphique","graphic-paper"),"icon":"paper","n":("Papier graphique","Graphic paper"),"span":"30–300",
  "intro":("Papiers d'impression, d'écriture et d'édition, couchés ou non couchés, pour imprimeurs, éditeurs et transformateurs.",
           "Printing, writing and publishing papers, coated or uncoated, for printers, publishers and converters."),
  "key":("Offset","Couché sans bois","LWC","Papier journal"),"key_en":("Offset","Coated woodfree","LWC","Newsprint"),
  "groups":[
   ("Non couché sans bois","Uncoated woodfree",None,[("Offset, écriture et copie","Offset, writing and copy","60–300"),("Papier enveloppe","Envelope paper","80–120"),("Papier bouffant","Bulky paper","60–120"),("Papier traceur","Plotter paper","75–90")]),
   ("Couché sans bois","Coated woodfree",None,[("Couché brillant, satiné ou mat","Gloss, silk or matt coated","70–300"),("Couché une face","One-side coated","70–300")]),
   ("Papier journal et bible","Newsprint and bible paper",None,[("Papier journal standard et amélioré","Standard and improved newsprint","40–60"),("Papier bible blanc, crème ou ivoire","Bible paper, white, cream or ivory","30–40")]),
   ("Non couché avec bois","Uncoated mechanical",None,[("Non couché avec bois","Uncoated mechanical","50–150"),("Papier d'édition satiné","Satin-finish book paper","50–150"),("SC offset et SC héliogravure","SC offset and SC rotogravure","40–60")]),
   ("Couché avec bois (LWC)","Coated mechanical (LWC)",None,[("LWC offset brillant, satiné ou mat","LWC offset, gloss, silk or matt","40–135"),("LWC héliogravure brillant","LWC rotogravure, gloss","40–135")]),
   ("Couleur, affiche et étiquette","Coloured, poster and label paper",None,[("Papier couleur","Coloured paper","40–300"),("Papier étiquette","Label paper","50–90"),("Papier affiche","Poster paper","90–150")]),
   ("Supports papier peint","Wallpaper base paper",None,[("Duplex","Duplex","100–150"),("Simplex","Simplex","90–130"),("Support avec bois","Mechanical base paper","70–130")]),
  ]},
 {"id":("papier-emballage","packaging-paper"),"icon":"box","n":("Papier d'emballage","Packaging paper"),"span":"20–400",
  "intro":("Kraft, papiers pour carton ondulé, kraft blanchi et papiers ingraissables pour l'industrie de l'emballage.",
           "Kraft, corrugating papers, bleached kraft and greaseproof papers for the packaging industry."),
  "key":("Kraftliner","Testliner","Kraft blanchi","Sulfurisé"),"key_en":("Kraftliner","Testliner","Bleached kraft","Greaseproof"),
  "groups":[
   ("Kraft brun et écru","Brown and natural kraft",None,[("Kraft brun ou écru","Brown or natural kraft","20–90"),("Kraftliner brun ou écru","Brown or natural kraftliner","100–400"),("Kraft enduit PE","PE-coated kraft","50–200"),("Kraft crêpé","Creped kraft","50–150"),("Kraft décor","Decor kraft","50–150"),("Kraft latex","Latex kraft","70–300")]),
   ("Papiers pour carton ondulé","Corrugating papers",None,[("Testliner","Testliner","100–300"),("Wellenstoff","Wellenstoff","85–200"),("Fluting","Fluting","90–200"),("Schrenz (papier gris)","Schrenz (grey paper)","70–200"),("Topliner blanc","White top liner","100–240")]),
   ("Kraft blanchi","Bleached kraft",None,[("Kraft blanchi","Bleached kraft","20–180"),("Kraft blanchi couché","Coated bleached kraft","50–200"),("Kraft blanchi enduit PE","PE-coated bleached kraft","50–200"),("Kraft blanchi crêpé","Creped bleached kraft","50–150"),("Papier filtre blanchi","Bleached filter paper","40–150"),("Non-tissé","Nonwoven","40–150")]),
   ("Sulfurisé et ingraissable","Greaseproof and parchment",None,[("Papier sulfurisé blanchi ou non blanchi","Greaseproof paper, bleached or unbleached","30–60"),("Papier cuisson blanchi ou non blanchi","Baking paper, bleached or unbleached","40–60")]),
   ("Papiers techniques","Technical papers",None,[("Papier de masquage","Masking paper","45–60"),("Papier de protection","Protective paper","200–400")]),
  ]},
 {"id":("carton","board"),"icon":"raw","n":("Carton","Board"),"span":"80–1 500",
  "intro":("Cartons couchés et non couchés pour l'étui pliant et le packaging, cartons haute brillance et cartons de spécialité.",
           "Coated and uncoated boards for folding cartons and packaging, high-gloss boards and specialty boards."),
  "key":("GC1","GC2","GD2","SBS"),"key_en":("GC1","GC2","GD2","SBS"),
  "groups":[
   ("Cartons pour étuis","Folding boxboards","150–900",[("Carton gris (gris-gris)","Grey board",None),("GC1 duplex couché dos blanc","GC1 coated duplex, white back",None),("GC2 duplex couché dos manille","GC2 coated duplex, manila back",None),("GT1 triplex couché dos blanc","GT1 coated triplex, white back",None),("GT2 triplex couché dos manille","GT2 coated triplex, manila back",None),("GD2 duplex couché dos gris","GD2 coated duplex, grey back",None),("UD2 duplex non couché dos gris","UD2 uncoated duplex, grey back",None),("UT2 triplex non couché dos gris","UT2 uncoated triplex, grey back",None),("Carton SBS (blanchi massif)","SBS solid bleached board",None)]),
   ("Haute brillance","High gloss","80–300",[("Blanc, couché une ou deux faces","White, coated one or two sides",None),("Couleur, couché une ou deux faces","Coloured, coated one or two sides",None)]),
   ("Cartons de spécialité","Specialty boards",None,[("Carton pour sous-bocks","Beer mat board","500–900"),("Carton pour cartes de vœux","Greeting card board","200–300"),("Carton pour cartes à jouer","Playing card board","200–400"),("Autres spécialités","Other specialty grades","200–1 500")]),
  ]},
]

# Autres offres de Rance Sales (reprises de l'ancien site)
SERVICES = {
 "fr": [
  ("box","Emballage sur mesure","Des emballages conçus pour protéger et mettre en valeur vos produits industriels."),
  ("gear","Machines de transformation","Des équipements de production pour transformer plus efficacement, dans de nombreux secteurs."),
  ("spark","Services personnalisés","Une offre construite autour de vos contraintes de production, de volume et de délai."),
  ("wrench","Support technique","Assistance technique et maintenance pour que vos machines restent opérationnelles."),
 ],
 "en": [
  ("box","Custom packaging","Packaging designed to protect and present your industrial products."),
  ("gear","Processing machinery","Production equipment for more efficient processing across many sectors."),
  ("spark","Custom services","An offer built around your production, volume and lead-time constraints."),
  ("wrench","Technical support","Technical assistance and maintenance to keep your machines running."),
 ],
}

STEPS = {
 "fr": [("Votre besoin","Qualité, grammage, volume, destination : vous nous décrivez ce qu'il vous faut."),
        ("Sourcing en Europe","Nous identifions la papeterie européenne et la qualité adaptées à votre production."),
        ("Offre et commande","Vous recevez une offre claire, puis nous suivons la commande avec la papeterie."),
        ("Suivi export","Nous suivons l'expédition jusqu'à votre usine, avec une qualité constante d'un lot à l'autre.")],
 "en": [("Your need","Grade, grammage, volume, destination: you tell us what you need."),
        ("Sourcing in Europe","We identify the European mill and paper grade that fit your production."),
        ("Offer and order","You receive a clear offer, then we follow the order with the mill."),
        ("Export follow-up","We follow the shipment to your plant, with consistent quality from batch to batch.")],
}

WHY = {
 "fr": [("Innovation","Nous adaptons notre offre à l'évolution des tendances du marché."),
        ("Proximité","Des relations de confiance fondées sur l'écoute, la réactivité et la transparence."),
        ("Qualité","Des matériaux fiables et innovants qui soutiennent la performance de votre production.")],
 "en": [("Innovation","We adapt our offer to changing market trends."),
        ("Proximity","Trust-based relationships built on listening, responsiveness and transparency."),
        ("Quality","Reliable, innovative materials that support your production performance.")],
}

HOME_FAQ = {
 "fr": [
  ("Travaillez-vous à l'international ?", "Oui. Nos clients sont présents dans le monde entier. Indiquez-nous votre pays de livraison et vos volumes dans la demande de devis."),
  ("Quels produits proposez-vous ?", "Trois gammes, en bobines et en feuilles, de 20 à 1 500 g/m² : papier graphique (offset, couché, LWC, papier journal…), papier d'emballage (kraft, kraftliner, testliner, kraft blanchi, sulfurisé…) et carton (GC1, GC2, GD2, SBS…). Nous proposons aussi des emballages sur mesure, des machines de transformation et un support technique."),
  ("D'où vient votre papier ?", "Nous travaillons avec des papeteries européennes et sélectionnons la qualité adaptée à chaque production."),
  ("Comment demander un devis ?", f"Via le formulaire de demande de devis, par e-mail à {EMAIL}, par téléphone ou sur WhatsApp au {TEL_H}, du lundi au vendredi de 8 h à 19 h (heure de Paris)."),
  ("Où êtes-vous basés ?", "Rance Sales est une société française basée à Rennes."),
 ],
 "en": [
  ("Do you work internationally?", "Yes. Our customers are located worldwide. Tell us your delivery country and volumes in the quote request."),
  ("What products do you offer?", "Three ranges, in reels and sheets, from 20 to 1,500 g/m²: graphic paper (offset, coated, LWC, newsprint…), packaging paper (kraft, kraftliner, testliner, bleached kraft, greaseproof…) and board (GC1, GC2, GD2, SBS…). We also offer custom packaging, processing machinery and technical support."),
  ("Where does your paper come from?", "We work with European paper mills and select the right grade for each production."),
  ("How do I request a quote?", f"Use the quote request form, email {EMAIL}, or call or WhatsApp {TEL_H}, Monday to Friday, 8 am to 7 pm (Paris time)."),
  ("Where are you based?", "Rance Sales is a French company based in Rennes."),
 ],
}

UI = {
 "fr": {
  "lang":"fr","locale":"fr_FR","other":"en","other_label":"English","other_short":"EN",
  "nav":[("home","Accueil"),("products","Produits"),("about","À propos"),("contact","Contact")],
  "cta":"Demander un devis","menu":"Menu","skip":"Aller au contenu",
  "foot_tag":"Négoce international de papier graphique, papier d'emballage et carton, de l'Europe au monde entier. Rennes, France.",
  "hours":"Du lundi au vendredi, de 8 h à 19 h (heure de Paris)",
  "rights":"Tous droits réservés.","nav_label":"Navigation","cookies":"Cookies",
  "breadcrumb_home":"Accueil",
 },
 "en": {
  "lang":"en","locale":"en_GB","other":"fr","other_label":"Français","other_short":"FR",
  "nav":[("home","Home"),("products","Products"),("about","About"),("contact","Contact")],
  "cta":"Request a quote","menu":"Menu","skip":"Skip to content",
  "foot_tag":"International trading in graphic paper, packaging paper and board, from Europe to the world. Rennes, France.",
  "hours":"Monday to Friday, 8 am to 7 pm (Paris time)",
  "rights":"All rights reserved.","nav_label":"Navigation","cookies":"Cookies",
  "breadcrumb_home":"Home",
 },
}

# Palette reprise du logo (à ajuster avec le fichier du logo)
PALETTE = {"ink":"#111513","land":"#1a201c","dot":"#5b635e","accent":"#7dc35e"}  # couleurs du logo ; carte en pointillés comme le globe
