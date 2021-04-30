import dateFormat from 'dateformat'

export function getMegabytes (bytes) {
  try {
    if (bytes) {
      return (bytes / (1024 * 1024)).toFixed(2) + ' Mb'
    }
  } catch {
    return null
  }
}

export function getIssuedDate (unixtime) {
  if (!unixtime) return null
  try {
    return dateFormat(new Date(unixtime * 1000), 'yyyy')
  } catch (e) {
    console.error(e)
    return null
  }
}

export function getCoverUrl (cu, fictionId, libgenId, cuSuf, md5) {
  if (cu) return cu
  let r = ''
  if (libgenId || fictionId) {
    if (libgenId) {
      const bulkId = (libgenId - (libgenId % 1000))
      r = `covers/${bulkId}/${md5}`
    } else if (fictionId) {
      const bulkId = (fictionId - (fictionId % 1000))
      r = `fictioncovers/${bulkId}/${md5}`
    } else {
      return null
    }
  }
  if (cuSuf) {
    r = r + `-${cuSuf}`
    return `http://gen.lib.rus.ec/${r}.jpg`
  }
  return null
}
