import { castStringToSingleString, quoteUrl } from './utils'
import { getIssuedDate } from './helpers'

export class BaseView {
  constructor (dataPb) {
    Object.assign(this, dataPb)
  }

  getFilename () {
    const processedAuthor = castStringToSingleString((this.getFirstAuthors()).toLowerCase())
    const processedTitle = castStringToSingleString(this.getRobustTitle()).toLowerCase()

    const parts = []
    if (processedAuthor) {
      parts.push(processedAuthor)
    }
    if (processedTitle) {
      parts.push(processedTitle)
    }

    let filename = parts.join('-')

    if (!filename) {
      if (this.doi) {
        filename = quoteUrl(this.doi, '')
      } else {
        filename = this.md5
      }
    }

    const year = getIssuedDate(this.issuedDate)

    if (year) {
      filename = `${filename}-${year}`
    }
    filename = filename.replace(/-+/g, '-')

    return `${filename}.${this.extension}`
  }

  getExtension () {
    if (this.extension) {
      return this.extension
    } else {
      return 'pdf'
    }
  }

  getFirstAuthors (etAl = true, firstNAuthors = 1) {
    let etAlSuffix = ''
    if (etAl) {
      etAlSuffix = ' et al'
    }
    if (this.authorsList) {
      if (this.authorsList.length > firstNAuthors) {
        return this.authorsList.slice(0, firstNAuthors).join('; ') + etAlSuffix
      } else if (this.authorsList.length === 1) {
        if (this.authorsList[0].split(';').length - 1 >= 1) {
          const commaAuthors = this.authorsList[0].split(';').map(function (el) {
            return el.trim()
          })
          if (commaAuthors.length > firstNAuthors) {
            return (commaAuthors.slice(0, firstNAuthors)).join('; ') + etAlSuffix
          } else {
            return commaAuthors.join('; ')
          }
        }
        return this.authorsList[0]
      } else {
        return this.authorsList.join('; ')
      }
    } else {
      return ''
    }
  }

  getFormattedDatetime () {
    if (this.issuedAt) {
      const date = new Date(this.issuedAt * 1000)
      const today = new Date()
      const diffTime = Math.abs(date - today)
      const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24))
      if (diffDays < 365) {
        return `${date.getUTCFullYear()}.${date.getUTCMonth()}`
      } else {
        return date.getUTCFullYear()
      }
    }
  }

  getFormattedFiledata () {
    const parts = []
    if (this.language) {
      parts.push(this.language.toUpperCase())
    }
    parts.push(this.getExtension().toUpperCase())
    if (this.filesize) {
      parts.push(this.getFormattedFilesize())
    }
    return parts.join(' | ')
  }

  getFormattedFilesize () {
    if (this.filesize) {
      return (Math.max(1024, this.filesize) / (1024 * 1024)).toFixed(2) + 'Mb'
    }
    return ''
  }

  getIpfsMultihash () {
    if (this.ipfsMultihashesList) {
      return this.ipfsMultihashesList[0]
    }
    return ''
  }

  getTelegramLink () {
    return `https://t.me/libgen_scihub_bot?start=${Buffer.from('NID: ' + this.id.toString()).toString('base64')}`
  }

  getRobustTitle () {
    let result = this.title || ''
    if (this.volume) {
      if (this.title) {
        result += ` ${this.volume}`
      } else {
        result += this.volume
      }
    }
    return result
  }
}
