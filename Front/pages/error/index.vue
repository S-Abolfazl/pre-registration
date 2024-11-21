<template>

</template>

<script>
export default {
  layout: 'empty',
  data: () => ({
    page_title: 'خطا',
  }),

  mounted() {
    this.$store.dispatch('setPageTitle', this.page_title)
  },
}
</script>
