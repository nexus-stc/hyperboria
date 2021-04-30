import documentsProto from 'meta-api-grpc-web-js/meta-api-grpc-web-js_pb/nexus/meta_api/proto/documents_service_grpc_web_pb'
import searchProto from 'meta-api-grpc-web-js/meta-api-grpc-web-js_pb/nexus/meta_api/proto/search_service_grpc_web_pb'

export default class MetaApi {
  constructor (url, hostname) {
    this.metadata = {}
    if (hostname) {
      this.metadata['X-Forwarded-Host'] = hostname
    }
    this.documentsClient = new documentsProto.DocumentsPromiseClient(url)
    this.searchClient = new searchProto.SearchPromiseClient(url)
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

  prepareMetadata () {
    return Object.assign({ 'request-id': this.generateId(12) }, this.metadata)
  }

  async get (schema, documentId) {
    const request = new documentsProto.TypedDocumentRequest()
    request.setSchema(schema)
    request.setDocumentId(documentId)
    request.setSessionId(this.generateId(8))
    const response = await this.documentsClient.get(request, this.prepareMetadata())
    return response.toObject()
  }

  async search (schemas, query, page, pageSize = 5) {
    const request = new searchProto.SearchRequest()
    request.setPage(page)
    request.setPageSize(pageSize)
    schemas.forEach((schema) => request.addSchemas(schema))
    request.setQuery(query)
    request.setSessionId(this.generateId(8))
    const response = await this.searchClient.search(request, this.prepareMetadata())
    return response.toObject()
  }
}
