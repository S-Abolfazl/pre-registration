<template>
  <div>
    <v-card class="taghvim-card bg-white1" elevation="3" @click="goToTaghvim">
      <v-row no-gutters align="center">
        <!-- متن توضیحات -->
        <v-col cols="6" >
          <div class="title">
            <b class="font_43">تقویم آموزشی</b>
          </div>
          <div class="font_20 description" >
          زمان انتخاب واحد، شروع کلاس ها و امتحاناتو اینجا ببینید.
          </div>
        </v-col>

        <!-- تصویر موشک و مرد -->
        <v-col cols="6" class="d-flex justify-center">
          <div class="image-wrapper">
            <!-- {{ imgWidth() }} -->
            <img src="/image/panel/tagvim.png" alt="tagvim" :width=" imgWidth() " />
          </div>
        </v-col>
      </v-row>
    </v-card>
  </div>
</template>

<script>
    export default {
      methods: {
        goToTaghvim() {
          this.$router.push('/Taghvim/taghvim');
        },
        imgWidth() {
          // if (window.innerWidth > 2300)
          //   return '30%'
          // else if (window.innerWidth > 2050)
          //   return '34%'
          // else if (window.innerWidth > 1900)
          //   return '38%'

          if (this.$vuetify.breakpoint.mdOnly){
            if (window.innerWidth > 1080){
            return '55%'
            }

          }
          else if (this.$vuetify.breakpoint.lgOnly){
            if (window.innerWidth > 1700)
              return '55%'
            else if (window.innerWidth > 1520)
              return '63%'
            else if (window.innerWidth > 1280)
              return '68%'
          }
          else if (this.$vuetify.breakpoint.xlOnly) {
            if (window.innerWidth > 2300)
              return '30%'
            else if (window.innerWidth > 2050)
              return '34%'
            else if (window.innerWidth > 1900)
              return '55%'
          }

        }
      },
    };
</script>

<style scoped>
.taghvim-card {
  box-shadow: 0px 0px 20px 3px rgba(0, 0, 0, 0.3) !important;
  border-radius: 25px;
  border: 3px solid #7B5FF1;
  /* width: 25%;  */
  height: auto;
  min-height: 280px;
  margin: auto;
  position: relative; /* برای کنترل موقعیت فرزندان مطلق */
  overflow: visible; /* اجازه دهید تصویر از کارت بیرون بزند */
}

.image-wrapper {
  position: absolute;
  top: 27%;
  right: 4%;
  width: 100%;
  display: flex;
  justify-content: flex-end;
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
