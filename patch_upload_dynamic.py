import re

def fix_upload_image_to(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    new_fn = """async uploadImageTo(event, targetPath) {
                const file = event.target.files[0];
                if (!file) return;
                
                this.isUploadingImage = true;
                try {
                    const fileExt = file.name.split('.').pop();
                    const fileName = Math.random().toString(36).substring(2, 15) + '.' + fileExt;
                    
                    let folder = 'general';
                    if (targetPath.startsWith('pageData.')) {
                        folder = targetPath.split('.')[1];
                    }
                    const filePath = folder + '/' + fileName;

                    let { error: uploadError } = await supabase.storage.from('cms_images').upload(filePath, file);
                    if (uploadError) throw uploadError;
                    
                    const { data } = supabase.storage.from('cms_images').getPublicUrl(filePath);
                    
                    let cleanPath = targetPath.replace(/\\[/g, ".").replace(/\\]/g, "").replace(/'|"/g, "");
                    const parts = cleanPath.split('.');
                    let obj = this;
                    for (let i = 0; i < parts.length - 1; i++) {
                        if (!obj[parts[i]]) obj[parts[i]] = {};
                        obj = obj[parts[i]];
                    }
                    obj[parts[parts.length - 1]] = data.publicUrl;
                    
                    this.pageData = JSON.parse(JSON.stringify(this.pageData));
                    await this.saveDraft(false);
                } catch (e) {
                    console.error("Image upload failed", e);
                    alert("Failed to upload image. Make sure bucket permissions are set.");
                } finally {
                    this.isUploadingImage = false;
                    event.target.value = '';
                }
            }"""

    # regex to match the old function
    pattern = r'async uploadImageTo\(event, targetPath\) \{.*?this\.isUploadingImage = false;\s*event\.target\.value = \'\';\s*\}'
    html = re.sub(pattern, new_fn, html, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Fixed uploadImageTo in {filepath}")

fix_upload_image_to("admin.html")
fix_upload_image_to("admin-cms.html")
