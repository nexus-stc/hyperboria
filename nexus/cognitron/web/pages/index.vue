<template lang="pug">
  div
    form
      .input-group
        b-form-input(v-model='query' placeholder='Enter book name or DOI')
        b-button(type='submit' @click.stop.prevent='submit(query, 1, schema)') Search
      b-form-radio-group(
        v-model="schema"
        :options="schemas"
        class="radio-group"
        value-field="item"
        text-field="name")
    p.mt-5(v-if="scoredDocuments.length == 0") Nothing found
    b-pagination(v-if='scoredDocuments.length > 0' v-model='page' :total-rows='totalRows' :per-page='perPage' limit="2" :disabled="isLoading")
    .search_list
      search-list(:scored-documents='scoredDocuments')
    b-pagination(v-if='scoredDocuments.length > 0' v-model='page' :total-rows='totalRows' :per-page='perPage' limit="2" :disabled="isLoading")
</template>

<script>
import SearchList from '@/components/search-list'
export default {
  name: 'Index',
  components: { SearchList },
  loading: true,
  data () {
    return {
      query: '',
      scoredDocuments: [],
      defaultSchema: 'scitech',
      schema: 'scitech',
      schemas: [
        { item: 'scitech', name: 'Scitech' },
        // { item: 'scimag', name: 'Scimag' }
      ],
      page: 1,
      totalRows: 10,
      perPage: 1
    }
  },
  async fetch () {
    this.query = this.$route.query.query
    if (!this.query) {
      await this.$router.push({ path: '/' })
      this.scoredDocuments = []
      return
    }
    this.page = this.$route.query.page
    this.schema = this.$route.query.schema || this.defaultSchema

    if (!process.server) {
      this.$nuxt.$loading.start()
    }
    const response = await this.$meta_api.search(this.schema, this.query, this.page - 1, 5)
    if (response.hasNext) {
      this.totalRows = Number(this.page) + 1
    } else {
      this.totalRows = this.page
    }
    this.scoredDocuments = response.scoredDocumentsList

    if (!process.server) {
      this.$nuxt.$loading.finish()
    }
  },
  fetchOnServer: false,
  computed: {
    isLoading () {
      return this.$fetchState.pending || false
    }
  },
  watch: {
    '$route.query': '$fetch',
    schema () {
      if (this.query) {
        this.submit(this.query, this.page, this.schema)
      }
    },
    page () {
      this.submit(this.query, this.page, this.schema)
    }
  },
  methods: {
    submit (query, page, schema) {
      this.$router.push({ path: '/', query: { query: query, page: page, schema: schema } })
    }
  }
}
</script>

<style scoped>
  .search_list {
    padding-top: 15px;
    padding-bottom: 15px;
  }
  .radio-group {
    margin: 10px 0;
  }
</style>
