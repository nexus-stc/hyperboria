<template lang="pug">
  div.document
    .top
      h6 {{ document.title }}
    .top
      i
        h6 {{ document.locator }}
    table
      tbody
        v-tr(label="DOI", :value="document.doi")
        v-tr(label="Description", :value="document.description", @max-length=300)
        v-tr(label="Tags", :value="tags")
        v-tr(label="ISBNS", :value="isbns")
        v-tr(label="ISSNS", :value="issns")
        v-tr(label="File", :value="document.filedata")
        v-tr-link(label="Download link", v-if="ipfsMultihash" :value="document.filename", :url="ipfsUrl")
</template>

<script>
import { getIssuedDate } from '@/plugins/helpers'
export default {
  name: 'VScitech',
  props: {
    document: {
      type: Object,
      required: true
    }
  },
  computed: {
    isbns: function () {
      return (this.document.isbnsList || []).join('; ')
    },
    issns: function () {
      return (this.document.issnsList || []).join('; ')
    },
    issuedAt: function () {
      return getIssuedDate(this.document.issuedAt)
    },
    ipfsUrl: function () {
      if (!this.ipfsMultihash) return null
      return `${this.$config.ipfs.gateway.url}/ipfs/${this.ipfsMultihash}?filename=${this.document.filename}&download=true`
    },
    ipfsMultihash: function () {
      if (this.document.ipfsMultihashesList) {
        return this.document.ipfsMultihashesList[0]
      }
      return ''
    },
    tags: function () {
      return (this.document.tagsList || []).join('; ')
    }
  }
}
</script>
