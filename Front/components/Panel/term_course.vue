<template>
  <div>
    <v-card class="term-course-card bg-white1" elevation="3" @click="goToTermcourse">
      <v-row no-gutters align="center">
        <!-- متن توضیحات -->
        <v-col cols="6" >
          <div class="title">
            <b class="font_43">دروس ارائه شده در ترم</b>
          </div>
          <div class="font_20 description" >
          دروس ارائه شده در دانشکده، اساتید و ظرفیت اونارو ببینید.
          </div>
        </v-col>

        <!-- تصویر موشک و مرد -->
        <v-col cols="6" class="d-flex justify-center">
          <div class="image-wrapper">
            <!-- {{ imgWidth() }} -->
            <img src="/image/panel/term_courses.png" alt="course" :width="imgWidth()" />
          </div>
        </v-col>
      </v-row>
    </v-card>
  </div>
</template>

<script>
    export default {
      methods: {
        goToTermcourse() {
          this.$router.push('/term-courses');
        },
        imgWidth() {

          if (this.$vuetify.breakpoint.mdOnly){
            if (window.innerWidth > 1080){
            return '55%'
            }

          }
          else if (this.$vuetify.breakpoint.lgOnly){
            if (window.innerWidth > 1700)
              return '62%'
            else if (window.innerWidth > 1520)
              return '66%'
            else if (window.innerWidth > 1280)
              return '60%'
          }
          else if (this.$vuetify.breakpoint.xlOnly) {
            if (window.innerWidth > 2300)
              return '30%'
            else if (window.innerWidth > 2050)
              return '34%'
            else if (window.innerWidth > 1900)
              return '57%'
          }

        }
      },
    };
</script>

<style scoped>
.term-course-card {
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
  top: 23%;
  right: -2%;
  width: 100%;
  display: flex;
  justify-content: flex-end;
}

.course-image {
  width: 60%; /* تنظیم سایز تصویر */
}
.title{
  margin: 16px 14px auto auto;
  width: 170%;
}
.description {
  margin: 30px 14px auto auto;
  width: 90%; /* تنظیم سایز تصویر */
}
</style>
