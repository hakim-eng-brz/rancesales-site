# rancesales.com

Site vitrine bilingue (français / anglais) de Rance Sales, négoce international de papier industriel, matières premières et emballages.

## Contenu du dépôt

Le dépôt contient le site prêt à servir : le dossier racine est la racine web (`public_html` chez Hostinger).

- `index.html`, `produits/`, `a-propos/`, `contact/`, `merci/` : pages en français
- `en/` : pages en anglais
- `assets/` : feuille de style, script des animations, carte du monde, images de partage
- `contact.php` : envoi du formulaire de devis à commercial@rancesales.com (PHP `mail()`)
- `sitemap.xml`, `robots.txt`, `llms.txt` : référencement et lecture par les assistants IA
- `.htaccess` : HTTPS, redirections des anciennes adresses, en-têtes, cache

## Mise en ligne

Hostinger récupère ce dépôt via Git (hPanel, Avancé, Git) sur la branche `main`, dans `public_html`. Chaque push sur `main` peut redéployer le site.

## Modifier un texte

Les pages sont générées à partir des sources dans `src/` (`content.py` pour les textes, `build.py` pour les gabarits) :

```
python3 src/build.py .
```

## Logo et couleurs

Le site reprend le logo d'origine (`assets/logo-rance-sales.png` sur fond clair, `assets/logo-rance-sales-light.png` sur fond sombre) et ses couleurs : vert `#7dc35e`, noir `#111513`, gris `#5d625f`. Les couleurs sont définies en tête de `assets/site.css` (et dans `src/content.py` pour la carte).

Pour régénérer les images de partage et les icônes (Node et Playwright) : `node src/tools/og.js` et `node src/tools/icons.js`.
