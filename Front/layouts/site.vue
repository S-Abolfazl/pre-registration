<template>
  <v-app>
    <div>
      <nuxt />
    </div>
  </v-app>
</template>

<script>
export default {
  mounted() {
    document.getElementById('loading').style.display = 'none'
  },
}
</script>
