import { mountTemplatePage } from './core.js';

export function mountDuplicatePage(options) {
    return mountTemplatePage({
        templateFile: 'index.html',
        sourcePageId: 'home',
        ...options
    });
}
