<template>

</template>

<script>
export default {
  props: {},
  data: () => ({
  }),
  mounted() {
    this.$store.dispatch('setPageTitle', this.title)
  },
  methods: {},
}
</script>
