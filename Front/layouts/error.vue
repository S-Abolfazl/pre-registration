<template>
  <v-app dark></v-app>
</template>

<script>
export default {
  mounted() {
    setTimeout(() => {
      if (Boolean(localStorage.getItem('isDark')))
        this.$vuetify.theme.dark = Boolean(localStorage.getItem('isDark'));
    }, 2);
    this.$router.push('/error')
  },
}
</script>
