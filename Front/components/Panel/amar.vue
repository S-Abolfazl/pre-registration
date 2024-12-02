<template>
    <div>
      <v-card class="amar-card" elevation="3">
        <v-col no-gutters align="center">
          <!-- متن توضیحات -->
          <v-row rows="1" class="font_16">
            <div class="font_30 font_bold title" >آمار</div>
            
          </v-row>
          <v-row rows="2" class="font_18 description" >
          ببین کدوم درسا بیشترین دانشجو رو داره
          </v-row>
          <!-- تصویر موشک و مرد -->
          <v-row rows="3" class="d-flex justify-center">
            <img src="/image/panel/amar.png" alt="Rocket Man" class="rocket-image" />
          </v-row>
        </v-col>
      </v-card>
    </div>
  </template>
  
  <script>
  export default {
    name: "PreSignupCard",
  };
  </script>
  
  <style scoped>
  .amar-card {
    border-radius: 10%;
    border: 3px solid #FF8B37;
    background-color: #ffD7C7;
    width: 13%; 
    height: 250px; 
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
  .title{
    margin: 2px 10px 5px 5px;
    /* z-index: 2; تصویر بالاتر از کارت قرار بگیرد */
  }
  .description {
    margin: 10px 10px 10px 0px; /* تنظیم سایز تصویر */
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
  