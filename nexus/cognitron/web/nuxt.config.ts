import { defineNuxtConfig } from 'nuxt3'

let buildDir = process.argv.find((s) => s.startsWith('--buildDir='))
if (buildDir) {
  buildDir = buildDir.substr('--buildDir='.length)
}

export default defineNuxtConfig({
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
  nitro: {
    preset: 'server',
    output: {
      dir: buildDir,
    }
  }
})
