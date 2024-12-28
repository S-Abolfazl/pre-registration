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
      if (Boolean(localStorage.getItem('isDark')))
        this.$vuetify.theme.dark = Boolean(localStorage.getItem('isDark'));
    }, 2);
    document.getElementById('loading').style.display = 'none'
  },
}
</script>
