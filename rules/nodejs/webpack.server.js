const config = require('./{config_path}')
const express = require('express')
const app = express()

app.use(express.static('{static_path}'))
app.get('/', (req, res) => {
  res.sendFile('./index.html', { root: '{static_path}' })
})
app.listen(config.application.port, config.application.host, () => {
  console.log(`Server is listening on port: ${config.application.port}`)
})
