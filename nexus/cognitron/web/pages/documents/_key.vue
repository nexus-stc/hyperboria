<template>
  <div>
    <document
      v-if="document"
      :document="document"
      :schema="schema"
    />
  </div>
</template>

<script>
export default {
  name: 'Key',
  data () {
    return {
      document: {},
      schema: null
    }
  },
  async fetch () {
    await this.$search_api.search(this.$route.query.schema, this.$route.params.key).then(response => {
      if (response.scoredDocuments.length === 0) {
        this.$nuxt.error(404)
      }
      if (response.scoredDocuments.length > 1) {
        this.$nuxt.error(500)
      }
      this.document = response.scoredDocuments[0].document
      this.schema = this.$route.query.schema
    }).catch(e => {
      console.error(e)
      this.$nuxt.error(e.statusCode)
    })
  },
  fetchOnServer: false
}
</script>

<style scoped>

</style>
