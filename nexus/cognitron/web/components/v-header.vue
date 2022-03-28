<template lang="pug">
nav.navbar.navbar-light.bg-light
  b-container
    nuxt-link(to="/" title="Go to search!").logo
      | > Nexus Cognitron
    a.nav-link(href="https://t.me/nexus_search" title="News")
      | News
</template>

<script>
export default {
  name: 'VHeader',
  data () {
    return {
      query: ''
    }
  }
}
</script>

<style scoped lang="scss">
  a {
    padding: 5px 0;
  }
</style>
