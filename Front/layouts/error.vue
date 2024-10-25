<template>
  <v-app dark></v-app>
</template>

<script>
export default {
  props: {},
  data: () => ({
    title: '',
  }),
  mounted() {
    this.$router.push('/error')
    setTimeout(() => {
      document.getElementById('loading-parent').style.display = 'none'
    }, 1000)
  },
}
</script>
