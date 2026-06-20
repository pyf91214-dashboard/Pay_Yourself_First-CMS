import { mountTemplatePage } from './core.js';

export function mountDuplicatePage(options) {
    return mountTemplatePage({
        templateFile: 'business-support-package.html',
        sourcePageId: 'business-support-package',
        ...options
    });
}
