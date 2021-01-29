import { castStringToSingleString, escapeFormat, quoteUrl } from './utils'
import { getFirstAuthors, getIssuedDate } from './helpers'

function getRobustTitle (title, volume) {
  if (volume) {
    if (title) {
      title = `${title} ${volume}`
    } else {
      title = volume
    }
  }
  return escapeFormat(title)
}

export function getFilename (authors, title, doi, issuedDate, md5, extension) {
  const limit = 55

  const processedAuthor = castStringToSingleString((getFirstAuthors(authors, false, 1)).toLowerCase())
  const processedTitle = castStringToSingleString(getRobustTitle(title)).toLowerCase()

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
    if (doi) {
      filename = quoteUrl(doi, '')
    } else {
      filename = md5
    }
  }

  const year = getIssuedDate(issuedDate)

  if (year) {
    filename = `${filename}-${year}`
  }
  filename = filename.replace(/-+/g, '-')

  return `${filename}.${extension}`
}
