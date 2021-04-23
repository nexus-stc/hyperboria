let buildDir = process.argv.find((s) => s.startsWith('--buildDir='))
if (buildDir) {
  buildDir = buildDir.substr('--buildDir='.length)
} else {
  buildDir = 'nexus/cognitron/web/.nuxt'
}

export default {
  server: {
    host: '0.0.0.0',
    port: 8082
  },
  buildDir: buildDir,
  srcDir: 'nexus/cognitron/web',
  modulesDir: ['external/' + process.env.BAZEL_NODE_MODULES_ROOT],
  head: {
    title: 'Nexus Cognitron',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'Biggest Library on both Earth and Mars' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      { rel: 'apple-touch-icon', sizes: '180x180', href: '/apple-touch-icon.png' },
      { rel: 'icon', type: 'image/png', sizes: '32x32', href: '/favicon-32x32.png' },
      { rel: 'icon', type: 'image/png', sizes: '16x16', href: '/favicon-16x16.png' },
      { rel: 'manifest', href: '/site.webmanifest' },
      { rel: 'mask-icon', href: '/safari-pinned-tab.svg', color: '#5bbad5' },
      { name: 'msapplication-TileColor', content: '#603cba' },
      { name: 'theme-color', content: '#ffffff' }
    ]
  },

  // Global CSS (https://go.nuxtjs.dev/config-css)
  css: [
    '@/assets/css/app.scss',
    '@/assets/css/terminal.css'
  ],

  publicRuntimeConfig: {
    meta_api: {
      url: process.env.NEXUS_COGNITRON_WEB_meta_api.url || 'http://nexus-meta-api:8080'
    },
    ipfs: {
      gateway: {
        url: process.env.NEXUS_COGNITRON_WEB_ipfs.gateway.url || 'https://ipfs.io'
      }
    }
  },

  // Plugins to run before rendering page (https://go.nuxtjs.dev/config-plugins)
  plugins: [
    'plugins/helpers',
    'plugins/meta-api',
    'plugins/utils'
  ],

  // Auto import components (https://go.nuxtjs.dev/config-components)
  components: true,

  // Modules for dev and build (recommended) (https://go.nuxtjs.dev/config-modules)
  buildModules: [],

  // Modules (https://go.nuxtjs.dev/config-modules)
  modules: [
    '@nuxtjs/axios',
    // https://go.nuxtjs.dev/bootstrap
    'bootstrap-vue/nuxt'
  ],

  loading: { color: '#1a95e0', throttle: 0 },
  watchers: {
    webpack: {
      poll: true
    }
  },

  // Build Configuration (https://go.nuxtjs.dev/config-build)
  build: {
    extend (config) {
      config.resolve.alias['~'] = process.cwd()
    }
  }
}
