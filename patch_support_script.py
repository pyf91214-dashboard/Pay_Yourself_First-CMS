import re
import json

def append_script():
    with open('support.html', 'r', encoding='utf-8') as f:
        content = f.read()

    with open('support_data.json', 'r', encoding='utf-8') as f:
        support_data = f.read()
        
    script_block = f"""
    <!-- Supabase Dynamic Data Script -->
    <script>
        const supabaseUrl = 'https://nqwggnereuhphwmkqove.supabase.co';
        const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5xd2dnbmVyZXVocGh3bWtxb3ZlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzU4MDUxMjAsImV4cCI6MjA5MTM4MTEyMH0.1OM-fLTth5FcMKUPHgepeM3BdJMydHiK1coD0vw0o0M';
        
        document.addEventListener('alpine:init', () => {{
            const supabase = window.supabase.createClient(supabaseUrl, supabaseKey);
            
            Alpine.data('siteData', () => ({{
                pageData: {{
                    support: {support_data}
                }},
                
                async init() {{
                    const urlParams = new URLSearchParams(window.location.search);
                    const isPreviewMode = urlParams.get('mode') === 'preview';
                    
                    try {{
                        let {{ data, error }} = await supabase.from('site_content').select('*').eq('page_id', 'support').single();
                        if (data) {{
                            const loadedContent = isPreviewMode ? data.draft_content : data.live_content;
                            this.pageData.support = {{ ...this.pageData.support, ...loadedContent }};
                        }}
                    }} catch (e) {{
                        console.error("Failed to load CMS data", e);
                    }}
                }},
                
                toggleAccordion(event) {{
                    const btn = event.currentTarget;
                    const content = btn.nextElementSibling;
                    const isExpanded = btn.getAttribute('aria-expanded') === 'true';
                    
                    btn.setAttribute('aria-expanded', !isExpanded);
                    
                    if (!isExpanded) {{
                        content.classList.add('active');
                        content.style.maxHeight = content.scrollHeight + "px";
                    }} else {{
                        content.classList.remove('active');
                        content.style.maxHeight = null;
                    }}
                }}
            }}));
        }});
    </script>
</body>
</html>
"""

    end_str = r"</body>"
    idx = content.rfind(end_str)
    if idx != -1:
        content = content[:idx] + script_block
    
    with open('support.html', 'w', encoding='utf-8') as f:
        f.write(content)

append_script()
