const { Nuxt } = require('nuxt')
const app = require('express')()
const config = require('./{config_file}')
const nuxtConfig = Object.assign(require('./{nuxt_config_file}'), { dev: false, _start: true })
const nuxt = new Nuxt(nuxtConfig)

app.use(nuxt.render)
app.listen(config.application.port, config.application.host, () => {
  console.log(`Server started and listen on ${config.application.port}`)
})
