const config = require('./{config_path}')
const webpackConfig = require('./{webpack_config_path}')
const webpack = require('webpack')
const express = require('express')
const app = express()
const path = require('path')

const outputPath = path.join(process.cwd(), '{static_path}')
webpackConfig.output.path = outputPath

webpack(webpackConfig, (err, stats) => { // Stats Object
  if (err || stats.hasErrors()) {
    console.error(err || stats)
  }
  app.use(express.static(outputPath))
  app.get('/', (req, res) => {
    res.sendFile('./index.html', { root: outputPath })
  })
  app.listen(config.application.port, config.application.host, () => {
    console.log(`Dynamic server is listening on port: ${config.application.port}`)
  })
})
