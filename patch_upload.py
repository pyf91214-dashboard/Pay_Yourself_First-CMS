import re

def fix_upload():
    with open('admin-cms.html', 'r', encoding='utf-8') as f:
        content = f.read()

    old_block = """                    const parts = targetPath.split('.');
                    let obj = this;
                    for (let i = 0; i < parts.length - 1; i++) obj = obj[parts[i]];
                    obj[parts[parts.length - 1]] = data.publicUrl;"""

    new_block = """                    const cleanPath = targetPath.replace(/\\[(\\w+)\\]/g, '.$1');
                    const parts = cleanPath.split('.');
                    let obj = this;
                    for (let i = 0; i < parts.length - 1; i++) obj = obj[parts[i]];
                    obj[parts[parts.length - 1]] = data.publicUrl;"""

    content = content.replace(old_block, new_block)

    with open('admin-cms.html', 'w', encoding='utf-8') as f:
        f.write(content)

fix_upload()
