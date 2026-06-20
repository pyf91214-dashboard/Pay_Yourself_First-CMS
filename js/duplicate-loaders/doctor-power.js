import { mountTemplatePage } from './core.js';

export function mountDuplicatePage(options) {
    return mountTemplatePage({
        templateFile: 'doctor-power.html',
        sourcePageId: 'doctor-power',
        ...options
    });
}
