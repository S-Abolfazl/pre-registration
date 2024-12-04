<template>
  <div>
    <v-card class="taghvim-card" elevation="3" @click="goToTaghvim">
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
            <img src="/image/panel/tagvim.png" alt="tagvim" class="taghvim-image" />
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
          this.$router.push('/panel/Taghvim');
        },
      },
    };
</script>

<style scoped>
.taghvim-card {
  box-shadow: 0px 0px 20px 3px rgba(0, 0, 0, 0.3) !important;
  border-radius: 25px;
  border: 3px solid #7B5FF1;
  background-color: #FFFFFF;
  width: 20%; 
  height: 250px; 
  margin: auto;
  position: relative; /* برای کنترل موقعیت فرزندان مطلق */
  overflow: visible; /* اجازه دهید تصویر از کارت بیرون بزند */
  box-shadow: 200px 0px 20px rgba(0, 0, 0, 0.2);

}

.image-wrapper {
  position: absolute;
  top: 38%; 
  right: 5%; 
  width: 100%;
  display: flex;
  justify-content: flex-end;
}

.taghvim-image {
  width: 65%; /* تنظیم سایز تصویر */
}
.title{
  margin: 16px 14px auto auto;
  width: 150%;
}
.description {
  margin: 20px 14px auto auto;
  width: 100%; /* تنظیم سایز تصویر */
}
</style>
