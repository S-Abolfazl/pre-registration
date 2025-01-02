<template>
  <v-row no-gutters class="mt-10">
    <v-carousel hide-delimiters height="100%">
      <v-carousel-item v-for="(chunk, chunkIndex) in chunkedCourses" :key="chunkIndex">
        <apexchart
          v-if="chunk.length > 0"
          type="bar"
          :options="getChartOptions(chunk)"
          :series="getSeriesData(chunk)">
        </apexchart>
      </v-carousel-item>
    </v-carousel>
  </v-row>
</template>

<script>
export default {
  data() {
    return {
      series: [
        {
          name: 'ظرفیت',
          data: [],
        },
        {
          name: 'ثبت‌نام شده',
          data: [],
        },
      ],
      courseData: [],
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
          categories: [],
        },
      },
    };
  },
  mounted() {
    this.getDatas();
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
      return index !== -1 ? this.series[0].data[index] : 0;
    },
    getRegistered(course) {
      const index = this.chartOptions.xaxis.categories.indexOf(course);
      return index !== -1 ? this.series[1].data[index] : 0;
    },
    getDatas() {
      this.$reqApi('/academic-assistant/statistics/bar-chart', {}, {}, true, 'get')
        .then((response) => {
          // Reset series data before updating
          this.series[0].data = [];
          this.series[1].data = [];

          this.courseData = response;
          response.forEach(element => {
            this.series[0].data.push(element.capacity || 0); // Fallback to 0 if no data
            this.series[1].data.push(element.registered || 0); // Fallback to 0 if no data
          });

          // Update chart categories
          this.chartOptions.xaxis.categories = response.map(item => item.name || ''); // Fallback to empty string
        })
        .catch((error) => {
          this.$toast.error(error.message || 'Error fetching data.');
        });
    },
  },
};
</script>

<style scoped>
.v-container {
  background-color: #f5f5f5;
}
</style>
