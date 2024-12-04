<template>
  <div >
    <v-card class="professors-card blue1"  @click="goToProfessor">
      <v-row no-gutters align="center">
        <!-- متن توضیحات -->
        <v-col cols="6" >
          <div class="title" >
            <b class="font_43">اساتید بهشتی</b>
          </div>
          <div class="font_20 description" >
            بهتر با اساتید و شیوه درس دادنشون آشنا بشید و نظراتتون رو درمورد اونها بگید.
          </div>
        </v-col>

        <!-- تصویر موشک و مرد -->
        <v-col cols="6" class="d-flex justify-center">
          <div class="image-wrapper">
            <img src="/image/panel/teachers.png" alt="teachers" class="teacher-image" />
          </div>
        </v-col>
      </v-row>
    </v-card>
  </div>
</template>

<script>
  export default {
    methods: {
      goToProfessor() {
        this.$router.push('/panel/Professor');
      },
    },
  };
</script>

<style scoped>
.professors-card {
  box-shadow: 0px 0px 20px 3px rgba(0, 0, 0, 0.3) !important;
  border-radius: 25px;
  /* background-color: var(blue1); */
  border: 3px solid #7B5FF1 !important;
  width: 33%; 
  height: 280px; 
  margin: auto;
  position: relative; /* برای کنترل موقعیت فرزندان مطلق */
  overflow: visible; /* اجازه دهید تصویر از کارت بیرون بزند */
}

.image-wrapper {
  position: absolute;
  top: -1%; /* تصویر را از بالا بیرون بیاورید */
  right: -3%; /* تصویر را از سمت راست کمی خارج کنید */
  width: 100%;
  display: flex;
  justify-content: flex-end;
}

.teacher-image {
  width: 53%; /* تنظیم سایز تصویر */
}
.title{
  margin: 16px 14px auto auto;
 
}
.description {
  margin: 30px 14px auto auto;
  width: 88%; /* تنظیم سایز تصویر */
  
}

</style>
