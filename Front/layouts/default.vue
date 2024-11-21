<template>
  <v-app>
    <v-main v-if="show_body" class="ma-3 h-max w-max">
      <nuxt />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'default',
  data: () => ({
    show_body: false,
  }),
  beforeMount() {
    this.checkAuth();
  },
  methods: {
    checkAuth() {
      let user = this.$store.state.auth.user

      document.getElementById('loading').style.display = 'none';

      if (Boolean(user)) {
        this.show_body = true;
      }
      else {
        this.$store.dispatch('auth/nuxtServerInit').then(() => {
          document.getElementById('loading').style.display = 'none';
          this.show_body = true;
        })
      }
    },
  },
}
</script>
