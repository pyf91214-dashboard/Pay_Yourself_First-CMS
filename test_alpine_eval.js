const fs = require('fs');
const html = fs.readFileSync('admin.html', 'utf-8');
const jsBlocks = html.match(/<script.*?>([\s\S]*?)<\/script>/gi);
let code = jsBlocks[6].replace(/<script.*?>/i, '').replace(/<\/script>/i, '');
// We will mock Alpine and supabase and see if it throws when initialized.
const mock = `
const window = { location: { search: '' } };
const Alpine = { data: (name, initFunc) => { try { initFunc() } catch(e) { console.error('Error during init', e) } } };
const document = { addEventListener: (event, cb) => cb() };
const supabase = { storage: { from: () => ({ getPublicUrl: () => {} }) }, from: () => ({ select: () => ({ eq: () => ({ single: () => ({}) }) }) }) };

${code}
`;

fs.writeFileSync('test_alpine.js', mock);
