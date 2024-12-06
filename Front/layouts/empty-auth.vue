<template>
  <v-app>
    <v-main>
      <nuxt />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "auth",
  data() {
    return {
      title: 'Loading...',
    };
  },
  async mounted() {
    // Hide the loading element after the component is mounted
    const loadingElement = document.getElementById('loading');
    if (loadingElement) loadingElement.style.display = 'none';

    // should set
    // await this.checkAuth();
  },
  head() {
    return {
      title: this.title,
    };
  },
  methods: {
    async checkAuth() {
      let user = this.$store.state.auth.user;

      const landingElement = document.getElementById('landing');
      if (landingElement) landingElement.style.display = 'flex';

      if (user) {
        this.showBody();
      } else {
        // Wait for the store action to complete before showing the body
        await this.$store.dispatch('auth/nuxtServerInit');
        this.showBody();
      }
    },
    showBody() {
      this.show_body = true;

      // Hide loading after a short delay
      setTimeout(() => {
        const loadingElement = document.getElementById('loading');
        if (loadingElement) loadingElement.style.display = 'none';
      }, 1000);
    },
  },
};
</script>
