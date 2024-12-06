<template>
  <div>
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


        <v-row class="d-flex justify-center image-wrapper">
          <img src="/image/panel/amar.png" alt="amar" class="amar-image" />
        </v-row>
      </v-col>
    </v-card>
  </div>
</template>

<script>
export default {
  methods: {
    goToAmar() {
      this.$router.push('/panel/Amar');
    },
  },
};
</script>


<style scoped>
.amar-card {
  box-shadow: 0px 0px 20px 3px rgba(0, 0, 0, 0.3) !important;
  border-radius: 25px;
  border: 3px solid #FF8B37;
  /* background-color: #ffD7C7; */
  /* width: 13%; */
  height: 280px;
  margin: auto;
  position: relative; /* برای کنترل موقعیت فرزندان مطلق */
  overflow: visible; /* اجازه دهید تصویر از کارت بیرون بزند */
}

.image-wrapper {
  position: absolute;
  top: 53%; /* تصویر را از بالا بیرون بیاورید */
  right: 5%; /* تصویر را از سمت راست کمی خارج کنید */
  width: 100%;
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
