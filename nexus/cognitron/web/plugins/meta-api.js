import MetaApi from 'nexus-meta-api-js-client'

export default ({ $config }, inject) => {
  const metaApi = new MetaApi($config.meta_api)
  inject('meta_api', metaApi)
}
