import { aggregation } from '~/library/js/utils'
import BaseClient from '~/library/js/base-client'
import HttpClient from './http-client'

export default class Client extends aggregation(
  BaseClient, HttpClient
) {}
