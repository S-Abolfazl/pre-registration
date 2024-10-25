<template>

</template>

<script>
export default {
  data: () => ({
    title: 'ورود به سامانه',
  }),
  mounted() {
    this.$store.dispatch('setPageTitle', this.title)
  },
  methods: {
  }
}
</script>
