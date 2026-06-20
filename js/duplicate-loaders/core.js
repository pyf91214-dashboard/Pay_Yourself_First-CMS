function replaceQuotedPageId(html, sourcePageId, targetPageId) {
    const escapedSource = String(sourcePageId || '').replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    const singleQuotePattern = new RegExp(`'${escapedSource}'`, 'g');
    const doubleQuotePattern = new RegExp(`"${escapedSource}"`, 'g');

    return String(html || '')
        .replace(singleQuotePattern, `'${targetPageId}'`)
        .replace(doubleQuotePattern, `"${targetPageId}"`);
}

function replaceDocumentTitle(html, nextTitle) {
    const safeTitle = String(nextTitle || '').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    if (!safeTitle) {
        return html;
    }

    if (/<title>[\s\S]*?<\/title>/i.test(html)) {
        return html.replace(/<title>[\s\S]*?<\/title>/i, `<title>${safeTitle}</title>`);
    }

    return html;
}

export async function mountTemplatePage({
    templateFile,
    sourcePageId,
    pageId,
    pageName,
    pageTitle
}) {
    if (!templateFile) {
        throw new Error('A template file is required.');
    }

    if (!sourcePageId) {
        throw new Error('A source template page_id is required.');
    }

    if (!pageId) {
        throw new Error('A duplicate page_id is required.');
    }

    const response = await fetch(`/${String(templateFile).replace(/^\/+/, '')}`, {
        cache: 'no-store'
    });

    if (!response.ok) {
        throw new Error(`Unable to load template file ${templateFile}.`);
    }

    let html = await response.text();
    html = replaceQuotedPageId(html, sourcePageId, pageId);
    html = replaceDocumentTitle(html, pageTitle || pageName || '');

    document.open();
    document.write(html);
    document.close();
}
