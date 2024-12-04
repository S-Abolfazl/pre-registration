<template>
  <div>
    <v-card class="signup-card" >
      <v-row no-gutters align="center">
        <!-- متن توضیحات -->
        <v-col cols="6" >
          <div class="title" >
            <b class="font_43">پیش ثبت نام</b>
          </div>
          <div class="font_20 description" >
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


<style scoped>
.signup-card {
  box-shadow: 0px 0px 20px 3px rgba(0, 0, 0, 0.3) !important;
  border-radius: 25px;
  background-color: #7B5FF1;
  width: 30%; 
  height: 250px; 
  margin: auto;
  position: relative; /* برای کنترل موقعیت فرزندان مطلق */
  overflow: visible; /* اجازه دهید تصویر از کارت بیرون بزند */
}

.image-wrapper {
  position: absolute;
  top: -9%; /* تصویر را از بالا بیرون بیاورید */
  right: 3%; /* تصویر را از سمت راست کمی خارج کنید */
  width: 100%;
  display: flex;
  justify-content: flex-end;
}

.rocket-image {
  width: 50%; /* تنظیم سایز تصویر */
  /* z-index: 2; تصویر بالاتر از کارت قرار بگیرد */
}
.title{
  margin: 16px 14px auto auto;
  /* z-index: 2; تصویر بالاتر از کارت قرار بگیرد */
}
.description {
  margin: 20px 14px auto auto;
  width: 100%; /* تنظیم سایز تصویر */
  /* z-index: 2; تصویر بالاتر از کارت قرار بگیرد */
}

</style>
