<template>
    <div>
      <v-chip
        color="blue2"
        class="custom-chip "
      >
      <span class="font_30" >{{ text }}</span>
    </v-chip>
    <img :src="require('~/static/image/chart/books.png')" alt="books"  class="books-picture" >
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
  width: 12vw; /* Set width as a percentage of the container */
  height:3vw; /* Allow height to adjust automatically */
  justify-content: center;
  align-items: center;
  border-radius: 50px;
}
  .books-picture {
    width: 13%; 
    transform: translateX(-140%) translateY(-190%);
}
  </style>
  