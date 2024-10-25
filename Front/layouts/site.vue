<template>
  <v-app>
    <div>
      <nuxt />
    </div>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    title: '',
  }),
  mounted() {
    setTimeout(() => {
      document.getElementById('loading-parent').style.display = 'none'
    }, 1000)
  },
}
</script>
