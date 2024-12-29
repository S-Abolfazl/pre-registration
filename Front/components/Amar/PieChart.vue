<template>
  <v-container>
    <v-card class="pa-5">
      <v-card-title class="text-center font_20">مقایسه مشارکت ورودی ها</v-card-title>
      <apexchart
        type="donut"
        :options="chartOptions"
        :series="series">
      </apexchart>
      <div class="legend d-flex justify-center mt-4">
        <div v-for="(item, index) in legendData" :key="index" class="legend-item d-flex align-center mx-2">
          <v-icon :color="item.color" class="mr-1">mdi-circle</v-icon>
          {{ item.label }}
        </div>
      </div>
    </v-card>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      series: [],
      chartOptions: {
        chart: {
          type: 'donut',
        },
        labels: [],
        colors: ['#a6f157', '#69f0ae', '#ffa726', '#ff7043', '#7c4dff'],
        legend: {
          show: false,
        },
        plotOptions: {
          pie: {
            donut: {
              size: '65%',
            },
          },
        },
        responsive: [{
          breakpoint: 480,
          options: {
            chart: {
              width: 300,
            },
          },
        }],
      },
      legendData: [],
    };
  },
  mounted() {
    this.fetchChartData();
  },
  methods: {
    fetchChartData() {
      this.$reqApi('/academic-assistant/statistics/participation-percent', {}, {}, true, 'get')
        .then((response) => {
          const colors = ['#a6f157', '#69f0ae', '#ffa726', '#ff7043', '#7c4dff'];
          this.series = response.map(item => item.percent);
          this.chartOptions.labels = response.map(item => `ورودی ${item.entry_year}`);
          this.legendData = response.map((item, index) => ({
            label: `ورودی ${item.entry_year} - ${item.percent}%`,
            color: colors[index % colors.length],
          }));
        })
        .catch((error) => {
          this.$toast.error(error.message || 'Error fetching chart data.');
        });
    },
  },
};
</script>

<style scoped>
.v-container {
  background-color: #f5f5f5;
}
.legend-item {
  font-size: 14px;
}
.v-card-title {
  font-weight: bold;
  font-size: 20px;
}
</style>
