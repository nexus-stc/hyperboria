import { BaseView } from './base'

export class ScitechView extends BaseView {
    index = 'scitech'
    icon = '📚'

    getFormattedLocator () {
      const parts = []
      if (this.authorsList) {
        parts.push(this.getFirstAuthors(true, 3))
      }
      if (this.issuedAt) {
        const date = new Date(this.issuedAt * 1000)
        parts.push(`(${date.getUTCFullYear()})`)
      }
      if (this.pages) {
        parts.push(`pp. ${self.pages}`)
      }
      return parts.join(' ')
    }
}
