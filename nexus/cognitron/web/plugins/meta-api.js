import MetaApi from '~/nexus/meta_api/js/client'

export default ({ $config }, inject) => {
  const metaApi = new MetaApi($config.metaApi)
  inject('meta_api', metaApi)
}
