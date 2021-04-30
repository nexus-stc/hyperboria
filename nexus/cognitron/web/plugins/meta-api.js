import { ScimagView, ScitechView } from 'nexus-views-js'
import MetaApi from 'nexus-meta-api-js-client'

function getSchema (typedDocument) {
  return Object.keys(typedDocument).filter(k => typedDocument[k] !== undefined)[0]
}

function schemaToView (schema, pb) {
  if (schema === 'scimag') {
    return new ScimagView(pb)
  } else if (schema === 'scitech') {
    return new ScitechView(pb)
  }
}

class MetaApiWrapper {
  constructor (metaApiConfig) {
    this.metaApi = new MetaApi(metaApiConfig.url || ('http://' + window.location.host), metaApiConfig.hostname)
  }

  async get (schema, id) {
    const response = await this.metaApi.get(schema, id)
    return schemaToView(schema, response[schema])
  }

  async search (schemas, query, page, pageSize) {
    const response = await this.metaApi.search(schemas, query, page, pageSize)
    const documents = response.scoredDocumentsList.map((scoredDocument) => {
      const schema = getSchema(scoredDocument.typedDocument)
      return schemaToView(schema, scoredDocument.typedDocument[schema])
    })
    return {
      hasNext: response.hasNext,
      documents: documents
    }
  }
}
export default ({ $config }, inject) => {
  const metaApiWrapper = new MetaApiWrapper($config.meta_api)
  inject('meta_api', metaApiWrapper)
}
