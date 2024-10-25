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
  head() {},
  data: () => ({
    title: '',
    show_body: false,
  }),
  watch: {},
  beforeMount() {
    this.checkAuth();
  },
  mounted() {
    this.$store.dispatch('setPageTitle', this.title);
  },
  methods: {
    checkAuth() {
      let user = this.$store.state.auth.user
      document.getElementById('loading-parent').style.display = 'flex'
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
