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
    const response = await this.$meta_api.getView(this.$route.params.schema, this.$route.params.id)
    this.document = {
      ...response.typedDocument.scitech,
      filedata: response.filedata,
      filename: response.filename,
      filesize: response.filesize,
      firstAuthors: response.firstAuthors,
      locator: response.locator
    }
  },
  fetchOnServer: false
}
</script>
