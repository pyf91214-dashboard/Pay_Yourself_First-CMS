const fs = require('fs');
const html = fs.readFileSync('admin.html', 'utf-8');
const jsBlocks = html.match(/<script.*?>([\s\S]*?)<\/script>/gi);
let hasError = false;

if (jsBlocks) {
    jsBlocks.forEach((block, index) => {
        let code = block.replace(/<script.*?>/i, '').replace(/<\/script>/i, '');
        // We write to a temp file and check
        fs.writeFileSync('temp_check.js', code);
        try {
            require('child_process').execSync('node -c temp_check.js', {stdio: 'pipe'});
            console.log(`Block ${index + 1} OK`);
        } catch (e) {
            console.log(`Block ${index + 1} ERROR!`);
            console.log(e.message);
            hasError = true;
        }
    });
}
if (!hasError) console.log("All blocks passed syntax check.");
