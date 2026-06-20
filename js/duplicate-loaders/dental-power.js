import { mountTemplatePage } from './core.js';

export function mountDuplicatePage(options) {
    return mountTemplatePage({
        templateFile: 'dental-power.html',
        sourcePageId: 'dental-power',
        ...options
    });
}
