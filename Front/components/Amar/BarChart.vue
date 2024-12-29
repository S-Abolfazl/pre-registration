<template>
  <v-container>
    <v-carousel hide-delimiters>
      <v-carousel-item v-for="(chunk, chunkIndex) in chunkedCourses" :key="chunkIndex">
        <apexchart
          type="bar"
          :options="getChartOptions(chunk)"
          :series="getSeriesData(chunk)">
        </apexchart>

      </v-carousel-item>
    </v-carousel>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      series: [
        {
          name: 'ظرفیت',
          data: [80, 90, 40, 70, 50, 60, 55, 30, 45, 50, 40, 60, 70, 85, 20],
        },
        {
          name: 'ثبت‌نام شده',
          data: [58, 35, 40, 50, 45, 30, 55, 20, 25, 30, 20, 40, 50, 60, 10],
        },
      ],
      courseData: [
        { name: 'زبان تخصصی', instructor: 'علی جهانبان', capacity: 50, registered: 58, time: '13:30-15:00', day: 'دوشنبه' },
        { name: 'هوش مصنوعی', instructor: 'محمد رضایی', capacity: 40, registered: 35, time: '10:00-12:00', day: 'شنبه' },
        { name: 'شبکه', instructor: 'محمد رضایی', capacity: 45, registered: 35, time: '10:00-12:00', day: 'شنبه' },
        { name: 'سیستم عامل', instructor: 'محمد رضایی', capacity: 40, registered: 70, time: '10:00-12:00', day: 'شنبه' },
        // More courses...
      ],
      chartOptions: {
        chart: {
          type: 'bar',
          height: 300,
        },
        colors: ['#6938ef', '#FF8B37'], // Different colors for each series
        plotOptions: {
          bar: {
            horizontal: false,
            columnWidth: '40%', // Adjust width
            endingShape: 'rounded',
          },
        },
        dataLabels: {
          enabled: false,
        },
        tooltip: {
          shared: true,
          intersect: false,
          formatter: function (seriesName, { series, dataPointIndex }) {
            return `
              <div style="text-align: right;">
                <strong>${series[0]}: ${series[0][dataPointIndex]}</strong><br>
                <strong>${series[1]}: ${series[1][dataPointIndex]}</strong>
              </div>
            `;
          },
        },
        xaxis: {
          categories: [
            'زبان تخصصی',
            'هوش مصنوعی',
            'شبکه',
            'سیستم عامل',
            'مهندسی نرم افزار',
            'سیستم های خبره',
            'پایگاه داده',
            'محاسبات عددی',
            'ریاضی مهندسی',
            'نظریه زبان ها و ماشین ها',
            'مدارهای منطقی',
            'الکترونیک',
            'ساختمان داده ها',
            'برنامه نویسی پیشرفته',
            'فیزیک 2',
          ],
        },
      },
    };
  },
  computed: {
    chunkedCourses() {
      const chunkSize = 20; // Adjust the chunk size as needed
      const courses = this.chartOptions.xaxis.categories;
      let chunks = [];
      for (let i = 0; i < courses.length; i += chunkSize) {
        chunks.push(courses.slice(i, i + chunkSize));
      }
      return chunks;
    },
  },
  methods: {
    getChartOptions(chunk) {
      return {
        ...this.chartOptions,
        xaxis: {
          categories: chunk,
        },
      };
    },
    getSeriesData(chunk) {
      return [
        {
          name: 'ظرفیت',
          data: chunk.map(course => this.getDemand(course)),
        },
        {
          name: 'ثبت‌نام شده',
          data: chunk.map(course => this.getRegistered(course)),
        },
      ];
    },
    getDemand(course) {
      const index = this.chartOptions.xaxis.categories.indexOf(course);
      return this.series[0].data[index];
    },
    getInstructor(course) {
      return this.courseData.find(c => c.name === course)?.instructor || '';
    },
    getCapacity(course) {
      return this.courseData.find(c => c.name === course)?.capacity || '';
    },
    getRegistered(course) {
      return this.courseData.find(c => c.name === course)?.registered || '';
    },
    getTime(course) {
      return this.courseData.find(c => c.name === course)?.time || '';
    },
    getDay(course) {
      return this.courseData.find(c => c.name === course)?.day || '';
    },
  },
};
</script>

<style scoped>
.v-container {
  background-color: #f5f5f5;
}
</style>
