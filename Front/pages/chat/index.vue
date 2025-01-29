<template>
    <div class="w-max">
      <chatForm />
    </div>
  </template>
  <script>
import chatForm from "~/components/Chat/chatForm.vue";
  export default {
    head() {
      return {
        title: 'پشتيباني',
      }
    },
    components: { chatForm, }
  };
  </script>
