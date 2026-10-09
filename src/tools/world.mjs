import fs from 'fs';
import * as topo from 'topojson-client';
import { geoNaturalEarth1, geoPath } from 'd3-geo';
const world = JSON.parse(fs.readFileSync('node_modules/world-atlas/countries-110m.json','utf8'));
const geoms = world.objects.countries.geometries.filter(g => g.id !== '010'); // sans Antarctique
const land = topo.merge(world, geoms);
const W=960,H=520;
const frame={type:"Feature",geometry:{type:"Polygon",coordinates:[[[-130,-42],[-130,70],[155,70],[155,-42],[-130,-42]]]}};
const proj=geoNaturalEarth1().rotate([-12,0]).fitExtent([[0,0],[W,H]],frame);
proj.clipExtent([[-2,-2],[W+2,H+2]]);
const path=geoPath(proj).digits(1);
const O=[6,47];
const dests={na:[-74,40.7],sa:[-46.6,-23.5],wa:[-4,5.4],naf:[3,36.7],me:[46.7,24.7],ea:[39.3,-6.8],sa2:[72.9,19],eas:[121.5,31.2]};
const routes={};
for (const [k,d] of Object.entries(dests)) routes[k]=path({type:"LineString",coordinates:[O,d]});
const pts={}; for (const [k,d] of Object.entries(dests)) pts[k]=proj(d).map(v=>Math.round(v));
const o=proj(O).map(v=>Math.round(v));
fs.writeFileSync('../data/world.json',JSON.stringify({W,H,land:path(land),routes,pts,o}));
console.log(o,pts, path(land).length);
