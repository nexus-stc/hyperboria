<template lang="pug">
  div
    .top
      h6 {{ document.title }}
    .top
      i
        h6 {{ document.getFormattedLocator() }}
    table
      tbody
        v-tr(label="DOI", :value="document.doi")
        v-tr(label="Description", :value="document.description", @max-length=300)
        v-tr(label="Tags", :value="tags")
        v-tr(label="ISBNS", :value="isbns")
        v-tr(label="ISSNS", :value="issns")
        v-tr(label="File", :value="document.getFormattedFiledata()")
        v-tr-multi-link(label="Links", :links="links")
</template>

<script>
import { getIssuedDate } from '@/plugins/helpers'
import VTr from './v-tr'
import VTrMultiLink from './v-tr-multi-link'
export default {
  name: 'VScitech',
  components: { VTr, VTrMultiLink },
  props: {
    document: {
      type: Object,
      required: true
    }
  },
  computed: {
    isbns () {
      return (this.document.isbnsList || []).join('; ')
    },
    issns () {
      return (this.document.issnsList || []).join('; ')
    },
    issuedAt () {
      return getIssuedDate(this.document.issuedAt)
    },
    ipfsUrl () {
      if (!this.document.getIpfsMultihash()) return null
      return `${this.$config.ipfs.gateway.url}/ipfs/${this.document.getIpfsMultihash()}?filename=${this.document.getFilename()}&download=true`
    },
    links () {
      const links = []
      if (this.ipfsUrl) {
        links.push({
          url: this.ipfsUrl,
          value: 'IPFS.io'
        })
      } else {
        links.push({
          url: this.document.getTelegramLink(),
          value: 'Nexus Bot'
        })
      }
      return links
    },
    tags () {
      return (this.document.tagsList || []).join('; ')
    }
  }
}
</script>
