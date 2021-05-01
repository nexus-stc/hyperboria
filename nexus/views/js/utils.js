const NON_ALNUMWHITESPACE_REGEX = /([^\s\p{L}\p{Nd}])/gu
const MULTIWHITESPACE_REGEX = /\s+/g

export function castStringToSingleString (s) {
  let processed = s.replace(NON_ALNUMWHITESPACE_REGEX, ' ')
  processed = processed.replace(MULTIWHITESPACE_REGEX, '-')
  return processed
}

export function quoteUrl (url, safe) {
  if (typeof (safe) !== 'string') {
    safe = '/'
  }
  url = encodeURIComponent(url)
  const toUnencode = []
  for (let i = safe.length - 1; i >= 0; --i) {
    const encoded = encodeURIComponent(safe[i])
    if (encoded !== safe.charAt(i)) {
      toUnencode.push(encoded)
    }
  }
  url = url.replace(new RegExp(toUnencode.join('|'), 'ig'), decodeURIComponent)
  return url
}
