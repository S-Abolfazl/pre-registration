<template>
    <div>
      <v-card class="pre-signup-card" elevation="3">
        <v-row no-gutters align="center">
          <!-- متن توضیحات -->
          <v-col cols="6" class="font_16">
            <div class="font_30 font_bold titlee" >پیش ثبت نام</div>
            <div class="font_18" >
              شما اینجا میتوانید به صورت آزمایشی انتخاب واحد کنید تا دانشگاه بهتر بتونه برنامه و ظرفیت کلاس ها رو مشخص کنه.
            </div>
          </v-col>
  
          <!-- تصویر موشک و مرد -->
          <v-col cols="6" class="d-flex justify-center">
            <div class="image-wrapper">
              <img src="/image/panel/pishsabt.png" alt="Rocket Man" class="rocket-image" />
            </div>
          </v-col>
        </v-row>
      </v-card>
    </div>
  </template>
  
  <script>
  export default {
    name: "PreSignupCard",
  };
  </script>
  
  <style scoped>
  .pre-signup-card {
    border-radius: 16px;
    background-color: #7B5FF1;
    width: 30%; 
    height: 300px; 
    margin: auto;
    position: relative; /* برای کنترل موقعیت فرزندان مطلق */
    overflow: visible; /* اجازه دهید تصویر از کارت بیرون بزند */
  }
  
  .image-wrapper {
    position: absolute;
    top: -6%; /* تصویر را از بالا بیرون بیاورید */
    right: 4%; /* تصویر را از سمت راست کمی خارج کنید */
    width: 100%;
    display: flex;
    justify-content: flex-end;
  }
  
  .rocket-image {
    width: 57%; /* تنظیم سایز تصویر */
    /* z-index: 2; تصویر بالاتر از کارت قرار بگیرد */
  }
  .titlee{
    margin: 2px 10px 0px 0px;
    /* z-index: 2; تصویر بالاتر از کارت قرار بگیرد */
  }
  .description {
    width: 57%; /* تنظیم سایز تصویر */
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
  