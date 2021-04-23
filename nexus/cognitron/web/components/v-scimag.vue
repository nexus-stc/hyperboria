<template lang="pug">
  div
    .top
      h6 {{ document.title }}
      h6
        i {{ document.locator }}
    table
      tbody
        v-tr(label="DOI", :value="document.doi")
        v-tr(label="Description", :value="document.abstract", @max-length=300)
        v-tr(label="Tags", :value="tags")
        v-tr(label="ISSNS", :value="issns")
        v-tr(label="ISBNS", :value="isbns")
        v-tr(label="File", :value="document.filedata")
        v-tr-link(label="Download link", v-if="ipfsMultihash" :value="document.filename", :url="ipfsUrl")
</template>

<script>
import { getIssuedDate } from '@/plugins/helpers'
import VTr from './v-tr'
import VTrLink from './v-tr-link'
export default {
  name: 'VScimag',
  components: { VTrLink, VTr },
  props: {
    document: {
      type: Object,
      required: true
    }
  },
  computed: {
    pages: function () {
      if (this.document.firstPage && this.document.lastPage && this.document.firstPage !== this.document.lastPage) {
        return `${this.document.firstPage}-${this.document.lastPage}`
      }
      return null
    },
    page: function () {
      if (this.document.firstPage) {
        if (this.document.lastPage) {
          if (this.document.firstPage === this.document.lastPage) {
            return this.document.firstPage
          }
        } else {
          return this.document.firstPage
        }
      } else if (this.document.lastPage) {
        return this.document.lastPage
      }
      return null
    },
    issns: function () {
      return (this.document.issnsList || []).join('; ')
    },
    isbns: function () {
      return (this.document.isbnsList || []).join('; ')
    },
    issuedAt: function () {
      return getIssuedDate(this.document.issuedAt)
    },
    ipfsUrl: function () {
      if (!this.ipfsMultihash) return null
      return `${this.$config.ipfs.gateway.url}/ipfs/${this.ipfsMultihash}?filename=${this.filename}&download=true`
    },
    ipfsMultihash: function () {
      if (this.document.ipfsMultihashesList) {
        return this.document.ipfsMultihashesList[0]
      }
      return null
    },
    tags: function () {
      return (this.document.tagsList || []).join('; ')
    }
  }
}
</script>
