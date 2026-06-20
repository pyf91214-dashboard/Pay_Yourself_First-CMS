import { mountTemplatePage } from './core.js';

export function mountDuplicatePage(options) {
    return mountTemplatePage({
        templateFile: 'how-we-help-you.html',
        sourcePageId: 'how_we_help_you',
        ...options
    });
}
