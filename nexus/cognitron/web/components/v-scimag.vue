<template lang="pug">
  div
    .top
      h6 {{document.title}}
    table
      tbody
        v-tr(label="Author", :value="authors")
        v-tr(label="Issued At", :value="issuedAt")
        v-tr(label="Issue", :value="document.issue")
        v-tr(label="Volume", :value="document.volume")
        v-tr(label="Page", :value="page")
        v-tr(label="Pages", :value="pages")
        v-tr(label="Container Title", :value="document.containerTitle")
        v-tr(label="Language", :value="document.language", value-classes="text-uppercase")
        v-tr(label="DOI", :value="document.doi")
        v-tr(label="Description", :value="document.abstract", @max-length=300)
        v-tr(label="Tags", :value="tags")
        v-tr(label="ISSNS", :value="issns")
        v-tr(label="ISBNS", :value="isbns")
        v-tr-link(label="Download link", v-if="ipfsMultihash" :value="filename", :url="ipfsUrl")

</template>

<script>
import { getFirstAuthors, getIssuedDate } from '@/plugins/helpers'
import { getFilename } from '@/plugins/scimag-helpers'
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
    authors: function () {
      return getFirstAuthors(this.document.authors, false, 3)
    },
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
    filename: function () {
      try {
        return getFilename(this.document.authors, this.document.title, this.document.doi, this.document.issuedAt)
      } catch (e) {
        console.error(e)
        return `file_${this.document.id}.pdf`
      }
    },
    issns: function () {
      return (this.document.issns || []).join('; ')
    },
    isbns: function () {
      return (this.document.isbns || []).join('; ')
    },
    issuedAt: function () {
      return getIssuedDate(this.document.issuedAt)
    },
    ipfsUrl: function () {
      if (!this.ipfsMultihash) return null
      return `${this.$config.ipfsGateway}/ipfs/${this.ipfsMultihash}?filename=${this.filename}`
    },
    ipfsMultihash: function () {
      if (this.document.ipfsMultihashes) {
        return this.document.ipfsMultihashes[0]
      }
      return null
    },
    tags: function () {
      return (this.document.tags || []).join('; ')
    }
  }
}
</script>
