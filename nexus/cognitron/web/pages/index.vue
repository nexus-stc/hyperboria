<template lang="pug">
  div
    form
      .input-group
        b-form-input(v-model='query' placeholder='Enter book name or DOI')
        b-button(type='submit' @click.stop.prevent='submit(query, 1, schemas)') Search
      b-form-checkbox-group.checkbox-group(
        v-model="schemas"
        :options="availableSchemas"
        value-field="item"
        text-field="name")
    p.mt-5(v-if="nothingFound") Nothing found
    .search-list
      search-list(:documents='documents')
    b-pagination(v-if='documents.length > 0' v-model='page' :total-rows='totalRows' :per-page='perPage' limit="2" :disabled="isLoading")
</template>

<script>
import SearchList from '@/components/search-list'

export default {
  name: 'Index',
  components: { SearchList },
  loading: true,
  data () {
    return {
      availableSchemas: [
        { item: 'scitech', name: 'SciTech' },
        { item: 'scimag', name: 'SciMag' }
      ],
      documents: [],
      nothingFound: false,
      page: 1,
      perPage: 1,
      query: '',
      schemas: ['scimag', 'scitech'],
      totalRows: 10
    }
  },

  async fetch () {
    this.nothingFound = false
    this.query = this.$route.query.query
    if (!this.query) {
      this.documents = []
      return this.$router.push({ path: '/' })
    }
    this.schemas = this.$route.query.schemas.split(',')
    if (this.schemas.length === 0) {
      this.schemas = ['scimag', 'scitech']
    }

    this.page = this.$route.query.page
    await this.retrieveDocuments()
  },
  fetchOnServer: false,
  computed: {
    isLoading () {
      return this.$fetchState.pending || false
    }
  },
  watch: {
    '$route.query': '$fetch',
    async schemas () {
      if (this.query) {
        await this.submit(this.query, 1, this.schemas)
      }
    },
    async page () {
      await this.submit(this.query, this.page, this.schemas)
    }
  },
  methods: {
    async submit (query, page, schemas) {
      await this.$router.push({ path: '/', query: { query: query, page: page, schemas: schemas.join(',') } })
    },
    async retrieveDocuments () {
      const response = await this.$meta_api.search(this.schemas, this.query, this.page - 1, 5)
      if (response.hasNext) {
        this.totalRows = Number(this.page) + 1
      } else {
        this.totalRows = this.page
      }
      if (response.documents.length === 0) {
        this.nothingFound = true
      }
      this.documents = response.documents
    }
  }
}
</script>

<style scoped>
  .search-list {
    padding-top: 15px;
    padding-bottom: 15px;
  }
  .checkbox-group {
    margin: 10px 0;
  }
</style>
