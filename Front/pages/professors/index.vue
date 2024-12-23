<template>
    <div class="w-max">
      <ProfessorsForm />
    </div>
  </template>
  
  <script>
  import ProfessorsForm from "~/components/Professors/ProfessorsForm.vue";
  export default {
    layout: 'site',
    head() {
      return {
        title: 'اساتيد بهشتي',
      }
    },
    components: { ProfessorsForm, }
  };
  </script>
  