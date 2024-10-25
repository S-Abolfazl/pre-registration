<template>
  <v-app>
    <v-main v-if="show_body">
      <nuxt />
    </v-main>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    title: '',
    show_body: false,
  }),
  beforeMount() {
    this.checkAuth()
  },
  head() {
    this.checkDomain()
    return {
      title: this.title,
    }
  },
  methods: {
    showBody() {
      this.show_body = true
      setTimeout(() => {
        document.getElementById('loading-parent').style.display = 'none'
      }, 1000)
    },
    checkAuth() {
      let user = this.$store.state.auth.user
      document.getElementById('landing-parent').style.display = 'flex'
      if (Boolean(user)) {
        this.showBody()
      } else {
        this.$store.dispatch('auth/nuxtServerInit').then(() => {
          this.showBody()
        })
      }
    },
  },
}
</script>
