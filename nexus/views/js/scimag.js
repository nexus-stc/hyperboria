import { BaseView } from './base'

export class ScimagView extends BaseView {
  schema = 'scimag'
  icon = '🔬'

  getFormattedLocator () {
    const parts = []
    if (this.authorsList) {
      parts.push(this.getFirstAuthors(true, 3))
    }
    const journal = this.getRobustJournal()
    if (journal) {
      parts.push('in', journal)
    }
    const dt = this.getFormattedDatetime()
    if (dt) {
      parts.push(`(${dt})`)
    }
    if (this.getRobustVolume()) {
      parts.push(this.getRobustVolume())
    }
    if (this.getPages()) {
      parts.push(this.getPages())
    }
    return parts.join(' ')
  }

  getPages () {
    if (this.firstPage) {
      if (this.lastPage) {
        if (this.firstPage === this.lastPage) {
          return `p. ${this.firstPage}`
        } else {
          return `pp. ${this.firstPage}-${this.lastPage}`
        }
      } else {
        return `p. ${this.firstPage}`
      }
    } else if (this.lastPage) {
      return `p. ${this.lastPage}`
    }
  }

  getRobustJournal () {
    if (this.type !== 'chapter' && this.type !== 'book-chapter') {
      return this.containerTitle
    }
  }

  getRobustTitle () {
    let result = this.title || this.doi
    if (this.volume) {
      if (this.type === 'chapter' || this.type === 'book-chapter') {
        result += `in ${this.containerTitle} ${this.volume}`
      } else {
        result = this.volume
      }
    }
    return result
  }

  getRobustVolume () {
    if (this.volume) {
      if (this.issue) {
        return `vol. ${this.volume}(${this.issue})`
      } else {
        if (this.volume === parseInt(this.volume, 10)) {
          return `vol. ${this.volume}`
        } else {
          return this.volume
        }
      }
    }
  }
}
