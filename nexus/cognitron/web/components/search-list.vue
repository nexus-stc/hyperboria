<template lang="pug">
  ul
    li(v-for='scoredDocument in scoredDocuments')
      search-item(:scored-document='scoredDocument', :key='scoredDocument.typedDocument.scitech.id')
</template>

<script>
import SearchItem from '@/components/search-item'
export default {
  name: 'SearchList',
  components: { SearchItem },
  props: {
    scoredDocuments: {
      type: Array,
      required: true
    }
  }
}
</script>

<style scoped lang="scss">
  li {
    padding-bottom: 15px;
    padding-left: 0;
    &:after {
      content: none;
    }
  }
</style>
