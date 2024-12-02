<template>
  <div class="w-max">
    <LoginForm />
  </div>
</template>

<script>
import LoginForm from "~/components/Auth/test.vue";
export default {
  layout: 'site',
  head() {
    return {
      title: 'ورود به سامانه',
    }
  },
  components: { LoginForm, }
};
</script>
