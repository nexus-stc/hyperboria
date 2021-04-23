<template lang="pug">
  tr(v-show="value")
    th {{ label }}
    td(:class="valueClasses")
      | {{ formattedValue }}
      cite
        a(href="javascript:void(null);" @click="showMore" v-if="shouldCollapseText")  show more...
</template>

<script>
export default {
  name: 'VTr',
  props: {
    label: {
      type: String,
      required: true,
      default: ''
    },
    valueClasses: {
      type: String,
      required: false,
      default: ''
    },
    value: {
      type: [String, Number]
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
    shouldCollapseText () {
      return this.value && this.value.length > this.maxLength && !this.showAll
    },
    formattedValue () {
      if (this.shouldCollapseText) {
        return this.value.substr(0, this.maxLength)
      } else {
        return this.value
      }
    }
  },
  methods: {
    showMore () {
      this.showAll = true
    }
  }
}
</script>
