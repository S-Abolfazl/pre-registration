<template>
  <div v-if="active_chart">
    <div class="my-2">
      <v-row dense>
        <v-col cols="auto" class="mx-3 center-div">
          <span class="font_black">امکانات : </span>
        </v-col>
        <v-col cols="auto">
          <v-chip
            label
            color="success"
            class="mx-2 mb-1"
            :outlined="show_chart"
            @click="show_chart = false"
          >
            نمایش جدول
          </v-chip>
          <v-chip
            label
            color="success"
            class="mx-2 mb-1"
            :outlined="!show_chart"
            @click="show_chart = true"
          >
            نمایش نمودار
          </v-chip>
          <v-chip label color="warning" class="mx-2 mb-1" @click="exportCSV()">
            خروجی اکسل
          </v-chip>
        </v-col>
      </v-row>
    </div>
    <div v-if="loading" class="center-div py-6">
      <v-progress-circular
        :size="70"
        :width="7"
        indeterminate
        color="success"
      />
    </div>
    <div v-show="!loading">
      <div class="py-4" v-show="show_chart">
        <v-row dense>
          <v-col cols="12" md="2"></v-col>
          <v-col cols="12" md="8">
            <canvas :id="chart_id"></canvas>
          </v-col>
          <v-col cols="12" md="2"></v-col>
        </v-row>
      </div>
      <div v-show="!show_chart" v-if="!loading">
        <TableReport :response="response" ref="TableReportAction" />
      </div>
    </div>
  </div>
</template>

<script>
import Chart from 'chart.js'
import TableReport from '@/components/Inspection/TableReport'
export default {
  components: { TableReport },
  props: {
    url: { require: true },
  },
  data: () => ({
    chart: null,
    loading: true,
    chart_id: null,
    response: null,
    show_chart: false,
    active_chart: false,
  }),
  methods: {
    loadChart(response) {
      this.loading = true
      let network_ids = []
      let labels = response.XAxis.map((x) => {
        network_ids.push(x)
        return x.name
      })
      let datasets = response.YAxis.map((x, i) => {
        let data = []
        response.data.forEach((element) => {
          if (typeof element[i] != 'undefined') {
            data.push(parseInt(element[i]))
          } else {
            data.push(0)
          }
        })
        return {
          data,
          fill: true,
          label: x.name,
          backgroundColor: x.color,
        }
      })
      this.chart = new Chart(document.getElementById(this.chart_id), {
        type: 'bar',
        data: {
          labels,
          datasets,
        },
        options: {
          responsive: true,
          datasetFill: true,
          onClick: (event) => {
            let point = Chart.helpers.getRelativePosition(
              event,
              this.chart.chart
            )
            let xIndex = this.chart.scales['x-axis-0'].getValueForPixel(point.x)
            if (network_ids[xIndex]) {
              this.$emit('selectItem', network_ids[xIndex])
            }
          },
          scales: {
            yAxes: [
              {
                ticks: {
                  beginAtZero: true,
                },
              },
            ],
            xAxes: [
              {
                ticks: {
                  autoSkip: false,
                  maxRotation: 90,
                  minRotation: 90,
                },
              },
            ],
          },
          plugins: {
            legend: {
              position: 'right',
              labels: {
                font: {
                  size: 14,
                  family: 'font_medium',
                },
              },
            },
          },
        },
      })
      setTimeout(() => {
        this.loading = false
      }, 100)
    },
    submit(form) {
      if (this.chart) {
        this.chart.destroy()
      }
      this.chart_id = `chart_${Math.floor(Math.random() * 1000)}`
      this.loadData(form)
        .then((response) => {
          this.loadChart(response)
        })
        .catch((error) => {
          this.loading = false
        })
    },
    loadData(form) {
      return new Promise((res, rej) => {
        this.loading = true
        this.active_chart = true
        this.$reqApi(this.url, form)
          .then((response) => {
            this.response = response
            if (response.data.length == 0) {
              this.$toast.error('اطلاعاتی یافت نشد')
            }
            setTimeout(() => {
              res(response)
            }, 200)
          })
          .catch((error) => {
            rej()
          })
      })
    },
    exportCSV() {
      try {
        let table = this.$refs.TableReportAction
        if (Array.isArray(table)) {
          table[0].exportCSV()
        } else {
          table.exportCSV()
        }
      } catch (error) {}
    },
  },
}
</script>
