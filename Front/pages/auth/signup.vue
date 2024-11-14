<template>
  <div>
    the login page
  </div>
</template>

<script>
export default {
  // layout: 'auth',
  data: () => ({
    title: 'ورود به سامانه',
  }),
  mounted() {
    console.log('hi from login page');
    this.$store.dispatch('setPageTitle', this.title);
  },
};
</script>
