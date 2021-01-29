import HttpClient from '~/nexus/cognitron/web/client/index'
import SummaApi from '~/nexus/cognitron/web/client/api'

export default ({ $config }, inject) => {
  const summaApi = new SummaApi(
    new HttpClient({
      baseUrl: $config.searchApi,
      headers: () => {
        return {
          Accept: 'application/json'
        }
      }
    })
  )
  inject('search_api', summaApi)
}
