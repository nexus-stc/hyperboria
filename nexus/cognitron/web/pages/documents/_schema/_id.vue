<template>
  <div>
    <document
      v-if="document"
      :document="document"
    />
  </div>
</template>

<script>
export default {
  data () {
    return {
      document: {}
    }
  },
  async fetch () {
    this.document = await this.$meta_api.get(this.$route.params.schema, this.$route.params.id)
  },
  fetchOnServer: false
}
</script>
