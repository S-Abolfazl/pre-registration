<template>
  <v-app>
    <v-main v-if="show_body">
      <nuxt />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'default',
  head() {

  },
  data: () => ({
    show_body: true,
  }),
  watch: {},
  beforeMount() {
    this.checkAuth();
  },
  methods: {
    checkAuth() {
      let user = this.$store.state.auth.user
      // document.getElementById('loading-parent')?.style.display = 'flex'
      if (Boolean(user)) {
        this.show_body = true;
      } else {
        this.$store.dispatch('auth/nuxtServerInit').then(() => {
          this.show_body = true;
        })
      }
    },
  },
}
</script>
