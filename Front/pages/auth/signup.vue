<template>
  <div class="w-max">
    <SignupForm />
  </div>
</template>

<script>
import SignupForm from '~/components/Auth/SignupForm.vue';
export default {
  layout: 'site',
  head() {
    return {
      title: 'ثبت نام در سامانه',
    }
  },
  components: { SignupForm, }
};
</script>
