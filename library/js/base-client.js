import { removeUndefined, toCamel, toSnake } from 'utils'
import Axios from 'axios'

export default class BaseClient {
  constructor ({ baseUrl, headers = null, beforeRequest = null, afterRequest = null, errorHandler = null, withCredentials = false } = {}) {
    this.nativeClient = Axios.create({
      baseURL: baseUrl,
      withCredentials: withCredentials,
      headers: {
        'X-Bypass-Cache': 1,
        'Accept-Language': 'en'
      },
      transformResponse: Axios.defaults.transformResponse.concat([data => {
        return toCamel(data)
      }])
    })
    this.nativeClient.defaults.withCredentials = withCredentials
    this.nativeClient.interceptors.request.use((config) => {
      if (config.data) {
        config.data = removeUndefined(config.data)
        config.data = toSnake(config.data)
      }
      if (config.headers) {
        if (typeof headers === 'function') {
          config.headers = Object.assign(config.headers, headers())
        } else {
          config.headers = Object.assign(config.headers, headers)
        }
      }
      if (beforeRequest) {
        beforeRequest()
      }
      return config
    })

    this.nativeClient.interceptors.response.use((response) => {
      if (afterRequest) {
        afterRequest()
      }
      return response.data
    }, (error) => {
      if (afterRequest) {
        afterRequest()
      }
      if (errorHandler) {
        return errorHandler(error)
      } else {
        return Promise.reject(error)
      }
    })
  }
}
