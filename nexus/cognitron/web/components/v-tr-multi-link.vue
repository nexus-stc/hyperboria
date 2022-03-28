<template lang="pug">
tr
  th {{ label }}
  td
    a(v-for="link in links" :href="link.url" download) {{ link.value }}
</template>

<script>
export default {
  name: 'VTrMultiLink',

  props: {
    links: {
      required: true,
      type: Array
    },
    label: {
      required: true,
      type: String
    }
  },
  data () {
    return {
      showAll: false
    }
  }
}
</script>

<style scoped lang="scss">
  tr {
    word-break: break-all;
  }
  th {
    white-space: nowrap;
  }
  td > a {
    margin-right: 10px;
  }
</style>
