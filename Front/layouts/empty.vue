<template>
  <v-app>
    <div class="fit h-max">
      <nuxt />
    </div>
  </v-app>
</template>

<script>
export default {
  mounted() {
    document.getElementById('loading').style.display = 'none';
    {
      let data = localStorage.getItem('isDark')
      if (Boolean(data)) {
        this.$vuetify.theme.dark = data;
      }
    }
  }
}
</script>
