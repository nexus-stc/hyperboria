import dateFormat from 'dateformat'

export function getIssuedDate (unixtime) {
  if (!unixtime) return null
  try {
    return dateFormat(new Date(unixtime * 1000), 'yyyy')
  } catch (e) {
    return null
  }
}
