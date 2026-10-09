// Images de partage (Open Graph) aux couleurs du logo. Depuis la racine du dépôt, après un build :
//   node src/tools/og.js
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const ROOT = path.resolve(__dirname, '../..');
const A = path.join(ROOT, 'src/static/assets/');
(async () => {
  const b = await chromium.launch();
  const uri = (f,t) => `data:${t};base64,`+fs.readFileSync(f).toString('base64');
  const mapUri = uri(path.join(ROOT, 'assets/world.svg'),'image/svg+xml');
  const logoUri = uri(A+'logo-rance-sales-light.png','image/png');
  const tpl = (t,s) => `<html><body style="margin:0;width:1200px;height:630px;background:#111513;font-family:Arial,Helvetica,sans-serif;position:relative;overflow:hidden">
  <img src="${mapUri}" style="position:absolute;right:-120px;top:120px;width:820px">
  <div style="position:absolute;inset:0;background:linear-gradient(90deg,#111513 45%,rgba(17,21,19,0) 80%)"></div>
  <div style="position:absolute;left:0;right:0;bottom:0;height:10px;background:#7dc35e"></div>
  <div style="position:absolute;left:80px;top:80px;width:660px">
   <img src="${logoUri}" style="height:86px;display:block">
   <div style="color:#fff;font-size:60px;font-weight:800;line-height:1.05;margin-top:46px">${t}</div>
   <div style="color:#7dc35e;font-size:26px;margin-top:28px;font-weight:700;letter-spacing:1px">${s}</div></div></body></html>`;
  const pg = await b.newPage({viewport:{width:1200,height:630}});
  await pg.setContent(tpl("Papier industriel et emballage, de l'Europe au monde entier","NÉGOCE INTERNATIONAL · RENNES, FRANCE")); await pg.screenshot({path:A+'og-fr.png'});
  await pg.setContent(tpl("Industrial paper and packaging, from Europe to the world","INTERNATIONAL TRADING · RENNES, FRANCE")); await pg.screenshot({path:A+'og-en.png'});
  await b.close();
})();
