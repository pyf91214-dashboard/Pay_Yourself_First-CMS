import { mountTemplatePage } from './core.js';

export function mountDuplicatePage(options) {
    return mountTemplatePage({
        templateFile: 'purchase-power.html',
        sourcePageId: 'purchase-power',
        ...options
    });
}
