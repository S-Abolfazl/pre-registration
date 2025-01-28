<template>
  <v-app>
    <Bar></Bar>
    <v-main v-if="show_body" class="w-max">
      <nuxt />
    </v-main>
  </v-app>
</template>

<script>
import Bar from '~/components/Layout/Bar.vue';
export default {
  components: { Bar },
  data: () => ({
    show_body: false,
  }),
  beforeMount() {
    document.getElementById('loading').style.display = 'none';

    setTimeout(() => {
      const isDark = localStorage.getItem('isDark');
      if (isDark !== null) {
        this.$vuetify.theme.dark = isDark === 'true';
      }
    }, 2);

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
