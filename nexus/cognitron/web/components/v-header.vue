<template lang="pug">
  nav.navbar.navbar-light.bg-light
    b-container
      nuxt-link(to="/" title="Go to search!").logo
        | > Nexus Search
</template>

<script>
export default {
  name: 'VHeader',
  data () {
    return {
      search: ''
    }
  }
}
</script>

<style scoped lang="scss">
  a {
    padding: 5px 0;
  }
</style>
