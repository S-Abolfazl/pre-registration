<template>
    <!-- <div class="d-flex align-center"> -->
      <div class="d-flex flex-column align-center">
        <img :src="require('~/static/image/panel/tagvim.png')" alt="taghvim"  class="taghvim-picture mb-n3 ">
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
  justify-content: center;
  align-items: center;
  border-radius: 50px;
}
.taghvim-picture {
  width: 20%;
  z-index: 1;
  right: 32px;
  position: relative;
}
</style>
