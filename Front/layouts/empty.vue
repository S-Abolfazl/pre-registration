<template>
  <v-app>
    <div class="fit h-max">
      <nuxt />
    </div>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    title: '',
  }),
  head() {
    this.checkDomain()
    return {
      title: this.title,
    }
  },
  mounted() {
    setTimeout(() => {
      document.getElementById('loading-parent').style.display = 'none'
    }, 2000)
  },
  methods: {},
}
</script>
