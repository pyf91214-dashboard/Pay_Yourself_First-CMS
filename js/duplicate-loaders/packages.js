import { mountTemplatePage } from './core.js';

export function mountDuplicatePage(options) {
    return mountTemplatePage({
        templateFile: 'packages.html',
        sourcePageId: 'packages',
        ...options
    });
}
