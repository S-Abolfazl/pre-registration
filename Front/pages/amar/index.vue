<template>
  <div class="w-max h-max">
    <BarChart class="mb-10" />
    <v-row no-gutters>
      <v-col cols="6">
        <v-row no-gutters class="justify-center">
          <span class="font_20">
            دروس با تقاضای بیشتر از ظرفیت
          </span>
        </v-row>
        <!-- v-for="course in courses" -->
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
    },
    courses: [],
  }),
  mounted() {
    this.$reqApi('/academic-assistant/statistics/overflowed-courses', {}, {}, true, 'get')
    .then((response) => {
      this.courses = response;
    })
    .catch((error) => {
      this.$toast.error(error.message || 'Error fetching chart data.');
    });
  }
};
</script>
