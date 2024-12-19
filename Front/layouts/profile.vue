<template>
  <v-app>
    <v-main class="h-max w-max">
      <img src="image/profile/header.png" height="32%" width="100%" alt="img" class="pos">
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
<style scoped>
.pos {
  /* position: fixed !important; */
}
</style>
