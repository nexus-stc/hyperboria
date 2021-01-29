<template lang="pug">
  div
    form
      .input-group
        b-form-input(v-model='search' placeholder='Enter book name or DOI')
        b-button(type='submit' @click.stop.prevent='submit(search, 1, schema)') Search
      b-form-radio-group(
        v-model="schema"
        :options="schemas"
        class="radio-group"
        value-field="item"
        text-field="name")
    p.mt-5(v-if="nothingFound") Nothing found
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
      search: '',
      scoredDocuments: [],
      defaultSchema: 'scitech',
      schema: 'scitech',
      schemas: [
        { item: 'scitech', name: 'Scitech' }
        // { item: 'scimag', name: 'Scimag' }
      ],
      page: 1,
      totalRows: 10,
      perPage: 1,
      nothingFound: false
    }
  },
  async fetch () {
    this.search = this.$route.query.search
    if (!this.search) {
      await this.$router.push({ path: '/' })
      this.scoredDocuments = []
      this.nothingFound = false
      return
    }
    this.page = this.$route.query.page
    this.schema = this.$route.query.schema || this.defaultSchema
    let scoredDocuments = []

    if (!process.server) {
      this.$nuxt.$loading.start()
    }
    await this.$search_api.search(this.schema, this.search, this.page, 5).then(response => {
      if (!response.hasNext) {
        this.totalRows = this.page
      } else {
        this.totalRows = Number(this.page) + 1
      }
      scoredDocuments = response.scoredDocuments
    }).catch(e => {
      console.error(e)
      this.$nuxt.error(500)
    })
    this.scoredDocuments = scoredDocuments
    this.nothingFound = (!scoredDocuments.length > 0)
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
      if (this.search) {
        this.submit(this.search, this.page, this.schema)
      }
    },
    page () {
      this.submit(this.search, this.page, this.schema)
    }
  },
  methods: {
    submit (search, page, schema) {
      this.$router.push({ path: '/', query: { search: search, page: page, schema: schema } })
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
