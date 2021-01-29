<template lang="pug">
  tr(v-if="value")
    th {{ label }}
    td
      a(:href="url" download) {{ value }}
</template>

<script>
export default {
  name: 'VTrLink',

  props: {
    value: {
      default: null,
      required: true,
      type: String
    },
    url: {
      required: true,
      type: String
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
</style>
