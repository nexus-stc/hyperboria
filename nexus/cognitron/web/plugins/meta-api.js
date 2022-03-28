import { ScimagView, ScitechView } from 'nexus-views-js'
import MetaApi from 'nexus-meta-api-js-client'

function getSchema (typedDocument) {
  return Object.keys(typedDocument).filter(k => typedDocument[k] !== undefined)[0]
}

function indexNameToView (indexName, pb) {
  if (indexName === 'scimag') {
    return new ScimagView(pb)
  } else if (indexName === 'scitech') {
    return new ScitechView(pb)
  }
}

class MetaApiWrapper {
  constructor (metaApiConfig) {
    this.metaApi = new MetaApi(metaApiConfig.url || ('http://' + window.location.host), metaApiConfig.hostname)
  }

  async get (indexName, id) {
    const response = await this.metaApi.get(indexName, id)
    return indexNameToView(indexName, response[indexName])
  }

  async search (names, query, page, pageSize) {
    const response = await this.metaApi.search(names, query, page, pageSize)
    const documents = response.scoredDocumentsList.map((scoredDocument) => {
      const indexName = getSchema(scoredDocument.typedDocument)
      return indexNameToView(indexName, scoredDocument.typedDocument[indexName])
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
