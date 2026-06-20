import { mountTemplatePage } from './core.js';

export function mountDuplicatePage(options) {
    return mountTemplatePage({
        templateFile: 'tax-season-discount.html',
        sourcePageId: 'tax',
        ...options
    });
}
