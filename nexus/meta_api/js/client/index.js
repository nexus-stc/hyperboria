import documentsProto from '~/nexus/meta_api/proto/documents_service_grpc_web_pb'
import searchProto from '~/nexus/meta_api/proto/search_service_grpc_web_pb'

export default class MetaApi {
  constructor (config) {
    this.documentsClient = new documentsProto.DocumentsPromiseClient(config.url)
    this.searchClient = new searchProto.SearchPromiseClient(config.url)
  }

  generateId (length) {
    const result = []
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    const charactersLength = characters.length
    for (let i = 0; i < length; i++) {
      result.push(characters.charAt(Math.floor(Math.random() * charactersLength)))
    }
    return result.join('')
  }

  async getView (schema, documentId) {
    const request = new documentsProto.TypedDocumentRequest()
    request.setSchema(schema)
    request.setDocumentId(documentId)
    request.setSessionId(this.generateId(8))
    const response = await this.documentsClient.get_view(request, { 'request-id': this.generateId(12) })
    return response.toObject()
  }

  async search (schema, query, page, pageSize = 5) {
    const request = new searchProto.SearchRequest()
    request.setPage(page)
    request.setPageSize(pageSize)
    request.addSchemas(schema)
    request.setQuery(query)
    request.setSessionId(this.generateId(8))
    const response = await this.searchClient.search(request, { 'request-id': this.generateId(12) })
    return response.toObject()
  }
}
