<template lang="pug">
  div.d-flex
    div
      nuxt-link(:to="{ name: 'documents-schema-id', params: { schema: schema, id: document.id }}") {{ document.title }}
      .detail
        div
          i.mr-1(v-if='document.doi') DOI:
          span {{ document.doi }}
        div(v-if='document.firstAuthors')
          span {{ document.firstAuthors }} {{ issuedAt }}
        .gp
          span.el.text-uppercase(v-if="document.extension") {{ document.extension }}
          span.el.text-uppercase(v-if="document.language") {{ document.language }}
          span.el.text-uppercase(v-if="document.filesize") {{ document.filesize }}
          span.el(v-if="document.pages")
            span.mr-2 {{ document.pages }}
            span pages

</template>

<script>

import { getIssuedDate } from '@/plugins/helpers'

export default {
  name: 'SearchItem',
  props: {
    scoredDocument: {
      type: Object,
      required: true
    }
  },

  computed: {
    document: function () {
      return this.scoredDocument.typedDocument[this.schema]
    },
    issuedAt: function () {
      const date = getIssuedDate(this.document.issuedAt)
      if (date != null) return '(' + date + ')'
      return null
    },
    schema: function () {
      const td = this.scoredDocument.typedDocument
      return Object.keys(td).filter(k => td[k] !== undefined)[0]
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
