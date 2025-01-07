<template>
    <!-- <div class="d-flex align-center"> -->
      <div class="d-flex flex-column align-start mr-4">
        <img :src="require('~/static/image/panel/term_courses.png')" alt="seed"  class="flex-end seed-picture mb-n2 ">
        <v-chip
          color="blue2"
          class="custom-chip ma-0 pa-2 align-start"
        >
          <span class="font_30" >{{ text }}</span>
        </v-chip>
      </div>
    
  </template>

  <script>
  export default {
    name: "Year",
    props: {
      text: {
        type: String,
        required: true,
        default: "1400",
      },
    },
  };
  </script>

  <style scoped>
  .custom-chip {
  height:3vw; /* Allow height to adjust automatically */
  /* justify-content: center; */
  /* align-items: center; */
  border-radius: 50px;
}
.seed-picture {
  width: 22%;
  z-index: 1;
  right: 55px;
  position: relative;
}
</style>
