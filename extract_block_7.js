const fs = require('fs');
const html = fs.readFileSync('admin.html', 'utf-8');
const jsBlocks = html.match(/<script.*?>([\s\S]*?)<\/script>/gi);
if (jsBlocks && jsBlocks.length >= 7) {
    let blockStr = jsBlocks[6].replace(/<script.*?>/i, '').replace(/<\/script>/i, '');
    fs.writeFileSync('bad_code_7.js', blockStr);
    console.log('Extracted block 7 to bad_code_7.js');
} else {
    console.log('Block 7 not found');
}
