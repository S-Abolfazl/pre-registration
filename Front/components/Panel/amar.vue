<template>
  <div class="the-border">
    <v-card class="amar-card orange2" elevation="3" @click="goToAmar">
      <v-col no-gutters align="center">

        <v-row>
          <div class="title">
            <b class="font_43">
              آمار
            </b>
          </div>
          <div class="font_20 description" >
        ببین کدوم درسا بیشترین دانشجو رو داره.
        </div>
        </v-row>

        <v-row class="image-wrapper">
          <!-- {{ imgWidth() }} -->
          <img src="/image/panel/amar.png" alt="amar" :width="imgWidth()" />
        </v-row>
      </v-col>
    </v-card>
  </div>
</template>

<script>
export default {
  methods: {
    goToAmar() {
      this.$router.push('/amar');
    },
    imgWidth() {
      // if (window.innerWidth > 2300)
      //   return '30%'
      // else if (window.innerWidth > 2050)
      //   return '34%'
      // else if (window.innerWidth > 1900)
      //   return '38%'
      if (this.$vuetify.breakpoint.mdOnly){
        return '60%'
      }
      else if (this.$vuetify.breakpoint.lgOnly){
        if (window.innerWidth > 1700)
          return '56%'
        else if (window.innerWidth > 1520)
          return '65%'
        else if (window.innerWidth > 1280)
          return '70%'
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
.the-border {
  border-radius: 25px;
  border: 3px solid #ff6d05;
}
.amar-card {
  box-shadow: 0px 0px 20px 3px rgba(0, 0, 0, 0.3) !important;
  border-radius: 25px;
  background-color: #ff6d0542;
  height: auto;
  min-height: 280px;
  margin: auto;
  position: relative; /* برای کنترل موقعیت فرزندان مطلق */
  overflow: visible; /* اجازه دهید تصویر از کارت بیرون بزند */
}

.image-wrapper {
  position: absolute;
  top: 40%; /* تصویر را از بالا بیرون بیاورید */
  right: 3%; /* تصویر را از سمت راست کمی خارج کنید */
  width: 100%;
  display: flex;
  justify-content: center;
  align-content: flex-end;
}

.amar-image {
  width: 60%;
}
.title{
  text-align: right;
  margin: 16px 14px auto auto;
  width: 100%;

}
.description {
  width: 100%;
  text-align: right;
  margin: 30px 8px auto auto;

}

</style>
