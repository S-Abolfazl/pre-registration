<template>
    <div class="d-flex align-center">
      <div class="d-flex flex-column align-end">
        <img :src="require('~/static/image/chart/books.png')" alt="books"  class="books-picture mb-n1">
        <v-chip
          color="blue2"
          class="custom-chip ma-0 pa-2"
        >
          <span class="font_30" >{{ text }}</span>
        </v-chip>
      </div>
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
.books-picture {
  width: 52%;
  z-index: 1;
}
</style>
