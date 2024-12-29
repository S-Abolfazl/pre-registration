<template>
  <v-app dark></v-app>
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
    this.$router.push('/error')
  },
}
</script>
