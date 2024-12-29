<template>
  <div class="w-max h-max">
    <BarChart class="mb-10" />
    <v-row no-gutters>
      <v-col cols="6">
        <Boxes :course="course" />
      </v-col>
      <v-col cols="6">
        <PieChart />
      </v-col>
    </v-row>
  </div>
</template>

<script>
import PieChart from '~/components/Amar/PieChart.vue';
import BarChart from '~/components/Amar/BarChart.vue';
import Boxes from '~/components/Amar/Boxes.vue';
export default {
  head() {
    return {
      title: 'آمار',
    }
  },
  components: { PieChart, BarChart, Boxes },
  data: () => ({
    course: {
      title: 'تحلیل و طراحی سیستم‌ها',
      instructor: 'علیرضا شاملی سندی',
      time: '15:00-13:30',
      day: 'شنبه',
      registered: 88,
      capacity: 70,
    }
  }),
};
</script>
