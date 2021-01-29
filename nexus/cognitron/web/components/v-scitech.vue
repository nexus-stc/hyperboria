<template lang="pug">
  div.document
    .top
      h6 {{document.title}}
      img(:src="coverUrl" alt="" onerror="this.style.display='none'")
    table
      tbody
        v-tr(label="Author", :value="authors")
        v-tr(label="Issued At", :value="issuedAt")
        v-tr(label="Extension", :value="document.extension", value-classes="text-uppercase")
        v-tr(label="Filesize", :value="filesize")
        v-tr(label="Pages", :value="document.pages")
        v-tr(label="Language", :value="document.language", value-classes="text-uppercase")
        v-tr(label="DOI", :value="document.doi")
        v-tr(label="Description", :value="document.description", @max-length=300)
        v-tr(label="Tags", :value="tags")
        v-tr(label="ISBNS", :value="isbns")
        v-tr(label="ISSNS", :value="issns")
        v-tr(label="MD5", :value="document.md5")
        v-tr-link(label="Download link", v-if="ipfsMultihash" :value="filename", :url="ipfsUrl")
</template>

<script>
import { getCoverUrl, getFirstAuthors, getIssuedDate, getMegabytes } from '@/plugins/helpers'
import { getFilename } from '@/plugins/scitech-helpers'
export default {
  name: 'VScitech',
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
    coverUrl: function () {
      return getCoverUrl(this.document.cu, this.document.fictionId,
        this.document.libgenId,
        this.document.cuSuf,
        this.document.md5)
    },
    filesize: function () {
      return getMegabytes(this.document.filesize)
    },
    filename: function () {
      try {
        return getFilename(this.document.authors, this.document.title, this.document.doi,
          this.document.issuedAt, this.document.md5, this.document.extension)
      } catch (e) {
        console.error(e)
        return `file_${this.document.id}.${this.document.extension}`
      }
    },
    isbns: function () {
      return (this.document.isbns || []).join('; ')
    },
    issns: function () {
      return (this.document.issns || []).join('; ')
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
