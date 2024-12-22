<template>
  <div class="w-max h-max">
    <BarChart />
  </div>
</template>

<script>
import PieChart from '~/components/Amar/PieChart.vue';
import BarChart from '~/components/Amar/BarChart.vue';
export default {
  head() {
    return {
      title: 'آمار',
    }
  },
  components: { PieChart, BarChart }
};
</script>
