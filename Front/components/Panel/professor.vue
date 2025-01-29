<template>
  <div class="the-border">
    <v-card class="professors-card"  @click="goToProfessor">
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
            <!-- {{ imgWidth() }} -->
            <img src="/image/panel/teachers.png" alt="teachers" :width="imgWidth()" />
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
        this.$router.push('/professors');
      },
      imgWidth() {
          // if (window.innerWidth > 2300)
          //   return '30%'
          // else if (window.innerWidth > 2050)
          //   return '34%'
          // else if (window.innerWidth > 1900)
          //   return '38%'

          if (this.$vuetify.breakpoint.mdOnly){
            return '50%'
          }
          else if (this.$vuetify.breakpoint.lgOnly){
            if (window.innerWidth > 1700)
              return '45%'
            else if (window.innerWidth > 1520)
              return '50%'
            else if (window.innerWidth > 1280)
              return '57%'
          }
          else if (this.$vuetify.breakpoint.xlOnly) {
            if (window.innerWidth > 2300)
              return '30%'
            else if (window.innerWidth > 2050)
              return '34%'
            else if (window.innerWidth > 1900)
              return '45%'
          }

        }
    },

  };
</script>

<style scoped>
.the-border {
  border-radius: 25px;
  border: 3px solid #7B5FF1 !important;
}
.professors-card {
  box-shadow: 0px 0px 20px 3px rgba(0, 0, 0, 0.3) !important;
  border-radius: 25px;
  background-color: #7c5ff12a;
  /* border: 3px solid #7B5FF1 !important; */
  /* width: 33%;  */
  height: auto;
  min-height: 280px;
  margin: auto;
  position: relative; /* برای کنترل موقعیت فرزندان مطلق */
  overflow: visible; /* اجازه دهید تصویر از کارت بیرون بزند */
}

.image-wrapper {
  position: absolute;
  top: 0%; /* تصویر را از بالا بیرون بیاورید */
  right: -3%; /* تصویر را از سمت راست کمی خارج کنید */
  width: 100%;
  display: flex;
  justify-content: flex-end;
}


.title{
  margin: 16px 14px auto auto;

}
.description {
  margin: 30px 14px auto auto;
  width: 88%; /* تنظیم سایز تصویر */

}

</style>
