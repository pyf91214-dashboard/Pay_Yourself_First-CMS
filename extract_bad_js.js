const fs = require('fs');
const html = fs.readFileSync('admin.html', 'utf-8');
const jsBlocks = html.match(/<script.*?>([\s\S]*?)<\/script>/gi);
let blockStr = jsBlocks[6].replace(/<script.*?>/i, '').replace(/<\/script>/i, '');
fs.writeFileSync('bad_code.js', blockStr);
