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
            <!-- {{ imgWidth() }} -->
            <img src="/image/panel/pishsabt.png" alt="Rocket Man" :width="imgWidth()" />
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
        imgWidth() {
          // if (window.innerWidth > 2300)
          //   return '30%'
          // else if (window.innerWidth > 2050)
          //   return '34%'
          // else if (window.innerWidth > 1900)
          //   return '38%'

          if (this.$vuetify.breakpoint.mdOnly){
            return '51%'
          }
          else if (this.$vuetify.breakpoint.lgOnly){
            if (window.innerWidth > 1700)
              return '42%'
            else if (window.innerWidth > 1520)
              return '47%'
            else if (window.innerWidth > 1280)
              return '50%'
          }
          else if (this.$vuetify.breakpoint.xlOnly) {
            if (window.innerWidth > 2300)
              return '30%'
            else if (window.innerWidth > 2050)
              return '34%'
            else if (window.innerWidth > 1900)
              return '38%'
          }

        }
      },
    };
</script>

<style scoped>
.signup-card {
  box-shadow: 0px 0px 20px 3px rgba(0, 0, 0, 0.3) !important;
  border-radius: 25px;
  /* width: 33%;  */
  height: auto;
  min-height: 280px;
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


.title{
  margin: 16px 14px auto auto;

}
.description {
  margin: 30px 14px auto auto;
  width: 100%; /* تنظیم سایز تصویر */
}

</style>