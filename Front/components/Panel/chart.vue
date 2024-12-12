<template>
    <div>
      <v-card class="chart-card orange1" elevation="3" @click="goToChart">
        <v-row no-gutters align="center">

          <v-col cols="6" >
            <div class="title">
              <b class="font_43">چارت درسی</b>
            </div>
            <div class="font_20 description" >
              اینجا میتونید چارت خودتون رو شخصی سازی کنید و طبق اون انتخاب واحد کنید.
            </div>
          </v-col>

          <v-col cols="6" class="d-flex justify-center">
            <div class="image-wrapper">
              <img src="/image/panel/chart.png" alt="chart" class="chart-image" />
            </div>
          </v-col>
        </v-row>
      </v-card>
    </div>
  </template>

  <script>
      export default {
        methods: {
          goToChart() {
            this.$router.push('/panel/Chart');
          },
        },
      };
  </script>

  <style scoped>
  .chart-card {
    box-shadow: 0px 0px 20px 3px rgba(0, 0, 0, 0.3) !important;
    border-radius: 25px;
    /* width: 15%;  */
    height: 280px;
    margin: auto;
    position: relative; /* برای کنترل موقعیت فرزندان مطلق */
    overflow: visible; /* اجازه دهید تصویر از کارت بیرون بزند */
    box-shadow: 200px 0px 20px rgba(0, 0, 0, 0.2);

  }

  .image-wrapper {
    position: absolute;
    top: 3%;
    right: 5%;
    width: 100%;
    display: flex;
    justify-content: flex-end;
  }

  .chart-image {
    width: 52%; /* تنظیم سایز تصویر */
  }
  .title{
    margin: 16px 14px auto auto;
    width: 150%;
  }
  .description {
    margin: 30px 14px auto auto;
    width: 100%; /* تنظیم سایز تصویر */
  }
  </style>
