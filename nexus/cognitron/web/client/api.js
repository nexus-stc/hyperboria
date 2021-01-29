export default class SummaApi {
  constructor (client) {
    this.client = client
  }

  async search (schema, text, page, item_per_page = 5) {
    return await this.client.search(schema, text, page, item_per_page).then(response => {
      return response
    })
  }
}
