const fs = require('fs');
const html = fs.readFileSync('admin.html', 'utf-8');
const jsBlocks = html.match(/<script.*?>([\s\S]*?)<\/script>/gi);
let i = 0;
for (const block of jsBlocks) {
    i++;
    const code = block.replace(/<script.*?>/i, '').replace(/<\/script>/i, '');
    try {
        new Function(code);
    } catch (e) {
        console.error(`Syntax error in script block ${i}: ${e.message}`);
        // print a few lines around the error if possible, or just print the block
        // console.log(code.substring(0, 500));
    }
}
