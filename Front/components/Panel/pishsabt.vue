<template>
  <div>
    <v-card class="signup-card blue2" @click="goToPishsabt">
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


<script>
    export default {
      methods: {
        goToPishsabt() {
          this.$router.push('/panel/pishsabt');
        },
      },
    };
</script>

<style scoped>
.signup-card {
  box-shadow: 0px 0px 20px 3px rgba(0, 0, 0, 0.3) !important;
  border-radius: 25px;
  width: 33%; 
  height: 280px; 
  margin: auto;
  position: relative; /* برای کنترل موقعیت فرزندان مطلق */
  overflow: visible; /* اجازه دهید تصویر از کارت بیرون بزند */
}

.image-wrapper {
  position: absolute;
  top: -4%; /* تصویر را از بالا بیرون بیاورید */
  right: 1%; /* تصویر را از سمت راست کمی خارج کنید */
  width: 100%;
  display: flex;
  justify-content: flex-end;
}

.rocket-image {
  width: 47%; /* تنظیم سایز تصویر */
}
.title{
  margin: 16px 14px auto auto;

}
.description {
  margin: 30px 14px auto auto;
  width: 100%; /* تنظیم سایز تصویر */
}

</style>
