const ALNUMWHITESPACE_REGEX = /\P{L}/gu
const MULTIWHITESPACE_REGEX = /\s+/g

export function castStringToSingleString (s) {
  return s.replace(ALNUMWHITESPACE_REGEX, ' ').replace(MULTIWHITESPACE_REGEX, '-')
}
