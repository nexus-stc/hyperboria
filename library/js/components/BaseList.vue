<script>

export default {
  name: 'BaseList',
  props: {
    value: {
      type: Array,
      default: function () { return [] }
    },
    typeName: {
      type: String,
      default: 'element'
    },
    getDisplayName: {
      type: Function,
      default: function (x) {
        return x
      }
    },
    afterProcess: {
      type: Function,
      default: function (x) {
        return x
      }
    },
    mutable: {
      type: Boolean,
      default: true
    }
  },
  data () {
    return {
      newElement: null
    }
  },
  methods: {
    handleAddElementInit () {
      this.$refs.newElementModal.show()
    },
    handleAddElementOk () {
      let processed = this.afterProcess(this.newElement)
      this.value.push(processed)
      this.$emit('added', processed)
      this.newElement = null
    },
    handleAddElementCancel () {
      this.newElement = null
    },
    deleteElement (elementIndex) {
      let deleted = this.value[elementIndex]
      this.value.splice(elementIndex, 1)
      this.$emit('deleted', deleted)
    }
  }
}
</script>
