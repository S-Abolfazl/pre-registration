<template>
  <v-app>
    <v-main class="h-max w-max">
      <img
        :src="this.$vuetify.theme.dark ? 'image/profile/header-dark.png' : 'image/profile/header.png'"
        height="21%" width="100%" alt="img" class="pos">
      <nuxt />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'profile',
  beforeMount() {
    document.getElementById('loading').style.display = 'none';
  },
}
</script>
