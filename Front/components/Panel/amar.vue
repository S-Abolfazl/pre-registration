<template>
  <div>
    <v-card class="amar-card" elevation="3">
      <v-col no-gutters align="center">
        <!-- متن توضیحات -->
        <v-row rows="1" >
          <div class="font_35 font_bold title" >آمار</div>
          <v-div class="font_16 description" >
        ببین کدوم درسا بیشترین دانشجو رو داره
        </v-div>
        </v-row>
        
        <!-- تصویر موشک و مرد -->
        <v-row rows="2" class="d-flex justify-center image-wrapper">
          <img src="/image/panel/amar.png" alt="amar" class="amar-image" />
        </v-row>
      </v-col>
    </v-card>
  </div>
</template>


<style scoped>
.amar-card {
  box-shadow: 0px 0px 20px 3px rgba(0, 0, 0, 0.3) !important;
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
  top: 48%; /* تصویر را از بالا بیرون بیاورید */
  right: 4%; /* تصویر را از سمت راست کمی خارج کنید */
  width: 100%;
}

.amar-image {
  width: 75%; /* تنظیم سایز تصویر */
  /* z-index: 2; تصویر بالاتر از کارت قرار بگیرد */
}
.title{
  text-align: right;
  margin: 8px 8px auto auto;
  width: 100%;
  /* z-index: 2; تصویر بالاتر از کارت قرار بگیرد */
}
.description {
  width: 100%;
  text-align: right;
  margin: 8px 8px auto auto;
  /* z-index: 2; تصویر بالاتر از کارت قرار بگیرد */
}

</style>
