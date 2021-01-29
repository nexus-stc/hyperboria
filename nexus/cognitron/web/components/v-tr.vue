<template lang="pug">
  tr(v-if="value")
    th {{label}}
    td(:class="valueClasses")
      | {{formattedValue}}
      cite
        a(href="javascript:void(null);" @click="showMore" v-if="collapseText")  show more...
</template>

<script>
export default {
  name: 'VTr',

  props: {
    label: {
      type: String,
      required: true
    },
    valueClasses: {
      type: String,
      required: false
    },
    value: {
      required: true,
      default: null
    },
    maxLength: {
      type: Number,
      default: 300
    }
  },
  data () {
    return {
      showAll: false
    }
  },
  computed: {
    collapseText () {
      return this.value.length > this.maxLength && !this.showAll
    },
    formattedValue () {
      if (this.value) {
        if (this.collapseText) {
          return this.value.substr(0, this.maxLength)
        } else {
          return this.value
        }
      }
      return null
    }
  },
  methods: {
    showMore () {
      this.showAll = true
    }
  }
}
</script>

<style scoped lang="scss">

</style>
