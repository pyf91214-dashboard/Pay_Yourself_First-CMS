import { mountTemplatePage } from './core.js';

export function mountDuplicatePage(options) {
    return mountTemplatePage({
        templateFile: 'about-us.html',
        sourcePageId: 'about_us',
        ...options
    });
}
