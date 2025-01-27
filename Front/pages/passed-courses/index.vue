<template>
    <div class="w-max">
      <PassedCourses />
    </div>
  </template>

  <script>
  import PassedCourses from "~/components/Chart/PassedCoursesForm.vue";
  export default {
    head() {
      return {
        title: 'واحد هاي پيشين',
      }
    },
    components: { PassedCourses, }
  };
  </script>
