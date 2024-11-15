<template>
  <div>
    <LoginForm />
  </div>
</template>

<script>
import LoginForm from "~/components/Auth/LoginForm.vue";
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
