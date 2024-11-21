<template>
  <v-container>
  </v-container>
</template>

<script>
export default {
  components: {},
  data: () => {},
  beforeMount() {
    this.$store.dispatch('setPageTitle', this.title)
  },
  methods: {
    loadData() {},
  },
}
</script>
