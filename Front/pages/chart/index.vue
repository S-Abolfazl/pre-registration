<template>
    <div class="w-max">
      <Chart />
    </div>
  </template>

  <script>
  import Chart from "~/components/Courses/ChartForm.vue";
  export default {
    // layout: 'site',
    head() {
      return {
        title: 'چارت دروس',
      }
    },
    components: { Chart, }
  };
  </script>
