<template lang="pug">
  b-container(v-if="visible")
    .loader
    .message {{text}}
</template>

<script>
export default {
  name: 'Loader',
  props: {
    text: {
      type: String,
      required: true
    },
    visible: {
      type: Boolean,
      required: true
    }
  }
}
</script>

<style lang="scss" scoped>
  .loader {
    width: 100%;
    height: 100%;
    position: fixed;
    z-index: 100;
    background-color: black;
    opacity: 0.3;
    top: 0;
    left: 0;
  }
  .message {
    padding: 50px 20px;
    background: white;
    width: 30%;
    text-align: center;
    position: fixed;
    left: 35%;
    top: 100px;
    z-index: 1000;
    font-size: 26px;
  }
</style>
