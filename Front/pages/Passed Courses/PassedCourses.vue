<template>
    <div class="w-max">
      <PassedCourses />
    </div>
  </template>
  
  <script>
  import PassedCourses from "~/components/Auth/PassedCoursesForm.vue";
  export default {
    layout: 'site',
    head() {
      return {
        title: 'واحد هاي پيشين',
      }
    },
    components: { PassedCourses, }
  };
  </script>
  