export default class HttpClient {
  search (schema, text, page, itemsPerPage) {
    const params = new URLSearchParams()
    params.append('query', text)
    if (page) {
      params.append('page', page)
    }
    if (itemsPerPage) {
      params.append('page_size', itemsPerPage)
    }
    const url = '/v1/' + schema + '/search/?' + params
    return this.nativeClient.request({
      method: 'get',
      url: url,
      cache: false
    })
  }
}
