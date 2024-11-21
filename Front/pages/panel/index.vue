<template>

</template>

<script>
export default {
  components: {},
  data: () => ({
    title: 'پنل اصلی',
  }),
  computed: {},
  beforeMount() {
    this.$store.dispatch('setPageTitle', this.title);
  },
  methods: {},
}
</script>
