const fs = require('fs');
const path = require('path');
const vm = require('vm');
const assert = require('assert');

function loadAlpineComponent(htmlPath, componentName) {
  const html = fs.readFileSync(htmlPath, 'utf8');
  const scriptMatches = [...html.matchAll(/<script\b(?![^>]*\bsrc=)[^>]*>([\s\S]*?)<\/script>/gi)];
  const components = {};
  const elementStub = {
    addEventListener: () => {},
    classList: {
      toggle: () => {},
      add: () => {},
      remove: () => {}
    },
    dataset: {},
    appendChild: () => {},
    firstElementChild: null,
    scrollBy: () => {},
    scrollWidth: 0,
    clientWidth: 0,
    scrollLeft: 0
  };

  const sandbox = {
    console,
    setTimeout,
    clearTimeout,
    tailwind: {},
    confirm: () => true,
    alert: () => {},
    fetch: async () => {
      throw new Error('fetch should not be called in tests');
    },
    window: {
      addEventListener: () => {},
      supabase: {
        createClient: () => ({
          from: () => ({
            select: async () => ({ data: [], error: null }),
            upsert: async () => ({ error: null }),
            eq() {
              return this;
            },
            single: async () => ({ data: null, error: null })
          })
        })
      }
    },
    document: {
      addEventListener(eventName, callback) {
        if (eventName === 'alpine:init') {
          callback();
        }
      },
      querySelector: () => null,
      getElementById: () => elementStub
    },
    Alpine: {
      data(name, factory) {
        components[name] = factory;
      },
      raw(value) {
        return value;
      }
    }
  };

  sandbox.window.Alpine = sandbox.Alpine;
  sandbox.global = sandbox;
  sandbox.globalThis = sandbox;

  vm.createContext(sandbox);

  for (const [, scriptContent] of scriptMatches) {
    vm.runInContext(scriptContent, sandbox, { filename: path.basename(htmlPath) });
  }

  if (!components[componentName]) {
    throw new Error(`Component ${componentName} was not found in ${htmlPath}`);
  }

  return components[componentName]();
}

function plain(value) {
  return JSON.parse(JSON.stringify(value));
}

function testAdminHomeButtonNormalization() {
  const cms = loadAlpineComponent(path.join(__dirname, 'admin-cms.html'), 'cmsManager');
  const normalized = cms.normalizeHomeData({
    hero_buttons: [
      { text: 'Hero One', url: '/hero-one' },
      { text: 'Hero Two', url: '/hero-two' }
    ],
    pillars_buttons: [
      { text: 'Pillars One', url: '/pillars-one' }
    ],
    bottom_cta: {
      btn_text: 'Primary CTA',
      btn_link: '/primary'
    },
    tax_systems: {
      btn_text: 'Tax CTA',
      btn_link: '/tax'
    },
    peace_of_mind: {
      btn_text: 'Peace CTA',
      btn_link: '/peace'
    }
  });

  assert.deepStrictEqual(plain(normalized.bottom_cta.buttons), [
    { text: 'Primary CTA', url: '/primary' }
  ]);
  assert.deepStrictEqual(plain(normalized.tax_systems.buttons), [
    { text: 'Tax CTA', url: '/tax' }
  ]);
  assert.deepStrictEqual(plain(normalized.peace_of_mind.buttons), [
    { text: 'Peace CTA', url: '/peace' }
  ]);
  assert.deepStrictEqual(plain(normalized.hero_buttons), [
    { text: 'Hero One', url: '/hero-one' },
    { text: 'Hero Two', url: '/hero-two' }
  ]);
  assert.deepStrictEqual(plain(normalized.pillars_buttons), [
    { text: 'Pillars One', url: '/pillars-one' }
  ]);
}

function testFrontendHomeButtonNormalization() {
  const site = loadAlpineComponent(path.join(__dirname, 'index.html'), 'siteData');
  const normalized = site.normalizeHomeContent({
    hero_buttons: [
      { text: 'Hero One', url: '/hero-one' }
    ],
    pillars_buttons: [
      { text: 'Pillars One', url: '/pillars-one' },
      { text: 'Pillars Two', url: '/pillars-two' }
    ],
    bottom_cta: {
      btn_text: 'Primary CTA',
      btn_link: '/primary'
    },
    tax_systems: {
      btn_text: 'Tax CTA',
      btn_link: '/tax'
    },
    peace_of_mind: {
      btn_text: 'Peace CTA',
      btn_link: '/peace'
    }
  });

  assert.deepStrictEqual(plain(normalized.bottom_cta.buttons), [
    { text: 'Primary CTA', url: '/primary' }
  ]);
  assert.deepStrictEqual(plain(normalized.tax_systems.buttons), [
    { text: 'Tax CTA', url: '/tax' }
  ]);
  assert.deepStrictEqual(plain(normalized.peace_of_mind.buttons), [
    { text: 'Peace CTA', url: '/peace' }
  ]);
  assert.deepStrictEqual(plain(normalized.hero_buttons), [
    { text: 'Hero One', url: '/hero-one' }
  ]);
  assert.deepStrictEqual(plain(normalized.pillars_buttons), [
    { text: 'Pillars One', url: '/pillars-one' },
    { text: 'Pillars Two', url: '/pillars-two' }
  ]);
}

function run() {
  testAdminHomeButtonNormalization();
  testFrontendHomeButtonNormalization();
  console.log('home button tests passed');
}

run();
