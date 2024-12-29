<template>
  <v-container>
    <v-card class="pa-5">
      <v-card-title class="text-center">مقایسه مشارکت ورودی ها</v-card-title>
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
import VueApexCharts from "vue-apexcharts";

export default {
  components: {
    apexchart: VueApexCharts,
  },
  data() {
    return {
      series: [5, 15, 30, 20, 30],
      chartOptions: {
        chart: {
          type: 'donut',
        },
        labels: ['ورودی 99', 'ورودی 400', 'ورودی 401', 'ورودی 402', 'ورودی 403'],
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
              width: 300
            },
          }
        }],
      },
      legendData: [
        { label: 'ورودی 99 - 5%', color: '#a6f157' },
        { label: 'ورودی 400 - 15%', color: '#69f0ae' },
        { label: 'ورودی 401 - 30%', color: '#ffa726' },
        { label: 'ورودی 402 - 20%', color: '#ff7043' },
        { label: 'ورودی 403 - 30%', color: '#7c4dff' },
      ],
    };
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
