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
    setTimeout(() => {
      const isDark = localStorage.getItem('isDark');
      if (isDark !== null) {
        this.$vuetify.theme.dark = isDark === 'true';
      }
    }, 2);
  }
}
</script>
