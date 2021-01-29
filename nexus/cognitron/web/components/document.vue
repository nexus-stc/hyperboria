<template lang="pug">
  div.document
    v-scimag(v-if="schema === 'scimag' && document", :document="document")
    v-scitech(v-if="schema === 'scitech' && document", :document="document")
</template>

<script>
export default {
  name: 'Document',
  props: {
    document: {
      type: Object,
      required: true
    },
    schema: {
      required: true
    },
  }
}
</script>

<style lang="scss">
  .document {
    .top {
      display: flex;
      justify-content: space-between;
      h6 {
        margin-right: 10px;
        margin-bottom: 0;
      }
      img {
        max-height: 200px;
        max-width: 200px;
        object-fit: contain;
        width: auto;
      }
    }
    padding: 30px 0;
    table {
      font-size: 12px;
      tr {
        word-break: break-all;
      }
      th {
        white-space: nowrap;
      }
    }
  }
</style>
