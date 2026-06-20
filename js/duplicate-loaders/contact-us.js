import { mountTemplatePage } from './core.js';

export function mountDuplicatePage(options) {
    return mountTemplatePage({
        templateFile: 'contact-us.html',
        sourcePageId: 'contact_us',
        ...options
    });
}
