<template>
  <div>
    <apexchart type="bar" :options="chartOptions" :series="series" />
  </div>
</template>

<script>
export default {
  data() {
    return {
      series: [
        {
          name: 'Course 1',
          data: [50, 70, 90, 60, 80],
        },
        {
          name: 'Course 2',
          data: [40, 60, 80, 70, 90],
        },
      ],
      chartOptions: {
        chart: {
          type: 'bar',
          toolbar: { show: false },
        },
        xaxis: {
          categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
        },
        colors: ['#FF5722', '#673AB7'],
      },
    };
  },
};
</script>
