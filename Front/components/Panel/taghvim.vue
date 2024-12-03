<template>
    <div>
      <v-card class="taghvim-card" elevation="3">
        <v-row no-gutters align="center">
          <!-- متن توضیحات -->
          <v-col cols="6" >
            <div class="font_35 font_bold titlee" >تقویم آموزشی</div>
            <div class="font_20 description" >
            زمان انتخاب واحد، شروع کلاس ها و امتحاناتو اینجا ببینید.
            </div>
          </v-col>
  
          <!-- تصویر موشک و مرد -->
          <v-col cols="6" class="d-flex justify-center">
            <div class="image-wrapper">
              <img src="/image/panel/tagvim.png" alt="tagvim" class="taghvim-image" />
            </div>
          </v-col>
        </v-row>
      </v-card>
    </div>
  </template>
  
  <style scoped>
  .taghvim-card {
    box-shadow: 0px 0px 20px 3px rgba(0, 0, 0, 0.3) !important;
    border-radius: 25px;
    border: 3px solid #7B5FF1;
    background-color: #FFFFFF;
    width: 20%; 
    height: 250px; 
    margin: auto;
    position: relative; /* برای کنترل موقعیت فرزندان مطلق */
    overflow: visible; /* اجازه دهید تصویر از کارت بیرون بزند */
    box-shadow: 200px 0px 20px rgba(0, 0, 0, 0.2);
  
  }
  
  .image-wrapper {
    position: absolute;
    top: 33%; 
    right: 6%; 
    width: 100%;
    display: flex;
    justify-content: flex-end;
  }
  
  .taghvim-image {
    width: 70%; /* تنظیم سایز تصویر */
    /* z-index: 2; تصویر بالاتر از کارت قرار بگیرد */
  }
  .titlee{
    margin: 8px 8px auto auto;
    width: 100%;
    /* z-index: 2; تصویر بالاتر از کارت قرار بگیرد */
  }
  .description {
    margin: 8px 8px auto auto;
    width: 100%; /* تنظیم سایز تصویر */
    /* z-index: 2; تصویر بالاتر از کارت قرار بگیرد */
  }
  
  /* .font_30 {
    font-size: 30px;
    font-weight: bold;
  }
  
  .font_20 {
    font-size: 20px;
  } */
  </style>
  