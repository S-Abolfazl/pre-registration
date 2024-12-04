<template>
  <div>
    <v-card class="term-course-card white1" elevation="3" @click="goToTermcourse">
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
            <img src="/image/panel/term_courses.png" alt="course" class="course-image" />
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
          this.$router.push('/panel/termcourse');
        },
      },
    };
</script>

<style scoped>
.term-course-card {
  box-shadow: 0px 0px 20px 3px rgba(0, 0, 0, 0.3) !important;
  border-radius: 25px;
  border: 3px solid #7B5FF1;
  width: 25%; 
  height: 280px; 
  margin: auto;
  position: relative; /* برای کنترل موقعیت فرزندان مطلق */
  overflow: visible; /* اجازه دهید تصویر از کارت بیرون بزند */
  box-shadow: 200px 0px 20px rgba(0, 0, 0, 0.2);

}

.image-wrapper {
  position: absolute;
  top: 36%; 
  right: -5%; 
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
