import { mountTemplatePage } from './core.js';

export function mountDuplicatePage(options) {
    return mountTemplatePage({
        templateFile: 'affiliate-plan.html',
        sourcePageId: 'affiliate',
        ...options
    });
}
