<template>
    <div class="w-max">
      <PassedCourses />
    </div>
  </template>
  
  <script>
  import PassedCourses from "~/components/Courses/PassedCoursesForm.vue";
  export default {
    layout: 'default',
    head() {
      return {
        title: 'واحد هاي پيشين',
      }
    },
    components: { PassedCourses, }
  };
  </script>
  