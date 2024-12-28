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
      if (Boolean(localStorage.getItem('isDark')))
        this.$vuetify.theme.dark = Boolean(localStorage.getItem('isDark'));
    }, 2);
  }
}
</script>
