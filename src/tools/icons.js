// Icônes (onglet du navigateur, écran d'accueil iOS) tirées de src/static/favicon.svg, le globe du logo simplifié.
//   node src/tools/icons.js   (favicon.ico, déjà fourni, se refait à partir de favicon.png avec n'importe quel convertisseur)
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const S = path.resolve(__dirname, '../static');
const svg = fs.readFileSync(path.join(S, 'favicon.svg'), 'utf8');
(async () => {
  const b = await chromium.launch();
  for (const [file,size,bg,pad] of [['favicon.png',48,null,0],['assets/apple-touch-icon.png',180,'#fff',22]]) {
    const p = await b.newPage({viewport:{width:size,height:size}});
    await p.setContent(`<body style="margin:0;background:${bg||'transparent'}"><div style="padding:${pad}px;width:${size}px;height:${size}px;box-sizing:border-box">${svg.replace('<svg ','<svg width="100%" height="100%" ')}</div></body>`);
    await p.screenshot({path:path.join(S, file), omitBackground:!bg}); await p.close();
  }
  await b.close();
})();
