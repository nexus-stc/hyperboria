<template lang="pug">
ul
  li(v-for='document in documents')
    v-scimag-search-item(v-if="document.index_alias == 'scimag'", :document='document', :key='document.id')
    v-scitech-search-item(v-if="document.index_alias == 'scitech'", :document='document', :key='document.id')
</template>

<script>
import VScimagSearchItem from '@/components/v-scimag-search-item'
import VScitechSearchItem from '@/components/v-scitech-search-item'

export default {
  name: 'SearchList',
  components: { VScimagSearchItem, VScitechSearchItem },
  props: {
    documents: {
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
