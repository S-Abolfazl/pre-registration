<template>
  <v-app>
    <div class="ma-3 h-max w-max d-flex align-center">
      <nuxt />
    </div>
  </v-app>
</template>

<script>
export default {
  mounted() {
    setTimeout(() => {
      const isDark = localStorage.getItem('isDark');
      if (isDark !== null) {
        this.$vuetify.theme.dark = isDark === 'true';
      }
    }, 2);
    document.getElementById('loading').style.display = 'none'
  },
}
</script>
