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
  }
}
</script>
