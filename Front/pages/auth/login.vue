<template>
  <div class="w-max">
    <LoginForm />
  </div>
</template>

<script>
import LoginForm from "~/components/Auth/PassedCoursesForm.vue";
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
