import { mountTemplatePage } from './core.js';

export function mountDuplicatePage(options) {
    return mountTemplatePage({
        templateFile: 'support.html',
        sourcePageId: 'support',
        ...options
    });
}
