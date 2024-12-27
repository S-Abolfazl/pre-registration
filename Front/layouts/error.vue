<template>
  <v-app dark></v-app>
</template>

<script>
export default {
  mounted() {
    {
      let data = localStorage.getItem('isDark')
      if (Boolean(data)) {
        this.$vuetify.theme.dark = data;
      }
    }
    this.$router.push('/error')
  },
}
</script>
