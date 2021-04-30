<template lang="pug">
  nav.navbar.fixed-bottom.ml-auto
    ul.navbar-nav.ml-auto
      li.nav-item
        | Powered by&nbsp;
        a(href="https://github.com/nexus-stc/hyperboria") Nexus STC
        | , 2025
</template>

<script>
export default {
  name: 'VFooter',
  data () {
    return {
      query: ''
    }
  }
}
</script>

<style scoped lang="scss">

</style>
