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
    {
      let data = localStorage.getItem('isDark')
      if (Boolean(data)) {
        this.$vuetify.theme.dark = data;
      }
    }
    document.getElementById('loading').style.display = 'none'
  },
}
</script>
