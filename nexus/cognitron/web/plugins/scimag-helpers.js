import { castStringToSingleString, quoteUrl } from './utils'
import { getIssuedDate } from './helpers'

export function getFilename (authors, title, doi, issuedDate) {
  const limit = 55

  let processedAuthor = ''
  if (authors) {
    processedAuthor = authors[0]
  }

  processedAuthor = castStringToSingleString((processedAuthor || '').toLowerCase())
  const processedTitle = castStringToSingleString((title || '').toLowerCase())

  const parts = []
  if (processedAuthor) {
    parts.push(processedAuthor)
  }
  if (processedTitle) {
    parts.push(processedTitle)
  }

  let filename = parts.join('-')
  const chars = []
  let size = 0
  let hitLimit = false

  for (const c of filename) {
    const currentSize = size + c.length
    if (currentSize > limit) {
      hitLimit = true
      break
    }
    chars.push(c)
    size = currentSize
  }

  filename = chars.join('')
  if (hitLimit) {
    const glyph = filename.lastIndexOf('-')
    if (glyph !== -1) {
      filename = filename.substr(0, glyph)
    }
  }

  if (!filename) {
    filename = quoteUrl(doi, '').substr(0, limit)
  }

  const year = getIssuedDate(issuedDate)

  if (year) {
    filename = `${filename}-${year}`
  }

  filename = filename.replace(/-+/g, '-')

  return `${filename}.pdf`
}
