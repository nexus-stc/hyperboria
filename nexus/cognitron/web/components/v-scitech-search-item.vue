<template lang="pug">
  div.d-flex
    div
      nuxt-link(:to="{ name: 'documents-schema-id', params: { schema: document.schema, id: document.id }}") {{ document.icon }} {{ document.title }}
      .detail
        div
          i.mr-1(v-if='document.doi') DOI:
          span {{ document.doi }}
        div(v-if='document.getFirstAuthors(false, 1)')
          span {{ document.getFirstAuthors(false, 1) }} {{ issuedAt }}
        .gp
          span.el.text-uppercase {{ document.getFormattedFiledata() }}
</template>

<script>

import { getIssuedDate } from '@/plugins/helpers'

export default {
  name: 'SearchItem',
  props: {
    document: {
      type: Object,
      required: true
    }
  },

  computed: {
    issuedAt: function () {
      const date = getIssuedDate(this.document.issuedAt)
      if (date != null) return '(' + date + ')'
      return null
    },

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
