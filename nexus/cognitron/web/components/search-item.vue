<template lang="pug">
  div.d-flex
    div
      nuxt-link(:to="link") {{ document.title }}
      .detail
        div
          i.mr-1(v-if='document.doi') DOI:
          span {{ document.doi }}
        div(v-if='authors')
          span {{ authors }} {{ issuedAt }}
        .gp
          span.el.text-uppercase(v-if="document.extension") {{ document.extension }}
          span.el.text-uppercase(v-if="document.language") {{ document.language }}
          span.el.text-uppercase(v-if="filesize") {{ filesize }}
          span.el(v-if="document.pages")
            span.mr-2 {{ document.pages }}
            span pages
    img(:src="coverUrl" alt="" onerror="this.style.display='none'")

</template>

<script>

import { getCoverUrl, getFirstAuthors, getIssuedDate, getMegabytes } from '@/plugins/helpers'

export default {
  name: 'SearchItem',
  props: {
    scoredDocument: {
      type: Object,
      required: true
    }
  },

  computed: {
    authors: function () {
      return getFirstAuthors(this.document.authors, false, 3)
    },
    coverUrl: function () {
      return getCoverUrl(this.document.cu, this.document.fictionId, this.document.libgenId, this.document.cuSuf, this.document.md5)
    },
    document: function () {
      return this.scoredDocument.document
    },
    issuedAt: function () {
      const date = getIssuedDate(this.document.issuedAt)
      if (date != null) return '(' + date + ')'
      return null
    },
    filesize: function () {
      return getMegabytes(this.document.filesize)
    },
    link: function () {
      return `/documents/id:${this.document.id}?schema=${this.scoredDocument.schema}`
    }
  }
}
</script>

<style scoped lang="scss">
  .el {
    display: block;
    line-height: 1em;
    margin-right: 10px;
    padding-right: 10px;
    border-right: 1px solid;
    &:last-child {
      border-right: 0;
    }
  }

  img {
    margin-left: 15px;
    max-width: 48px;
    max-height: 48px;
    object-fit: contain;
    width: auto;
  }
  .key {
    font-weight: bold;
  }
  .gp {
    margin-top: 2px;
    display: flex;
  }
  .detail {
    font-size: 12px;
  }
  i {
    text-transform: uppercase;
  }
</style>
