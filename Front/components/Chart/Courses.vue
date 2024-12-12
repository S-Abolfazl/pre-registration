<template>
    <div>
      <v-chip
        :color="border ? 'white1' : color"
        class="custom-chip"
        :outlined="border"
      >
        <span :class="[ 'font_16', border ? 'blue2--text' : 'white1--text']" v-html="text"> </span>
        <v-chip
          :color="border ?color :'white1' "
          class="inner-circle"
          :outlined="border"
        >
          <div :class="[ 'font_12']" :color="border ? 'white1' : color">  {{ number }}</div>
        </v-chip>
        <span :class="[ 'font_16', border ? 'blue2--text' : 'white1--text']"> واحد </span>
      </v-chip>
    </div>
  </template>
  
  <script>
  
  export default {
    name: "Courses",
    props: {
      text: {
        type: String,
        required: true,
        default: "اختصاصي",
      },
      number: {
        type: [String, Number],
        required: true,
        default: 83,
      },
      color: {
        type: String,
        default: "blue1",
      },
      border: {
        type: Boolean,
        default: false,
      }
    },
  };
  </script>
  
  <style >
.custom-chip {
    display: flex;
    justify-content: center;
    align-items: center;
    padding-left: 2rem;
    padding-right: 2rem;
    border-radius: 50px;
    font-weight: bold;
    width: fit-content;
    height: 2.5vw !important;
    margin: 1vw;
    border-color: blue1 ; 
    border-style: solid; 
    border-width: 2px;
  }
.text {
    color: white1;
  }
  
.inner-circle {
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 50%;
    width: 2.3vw; /* Ensure equal width and height */
    height: 1w;
    margin-right: 1.5rem;
    text-align: center;
    box-sizing: border-box; /* Prevent padding/margin issues */
    margin-left: 0.2rem;
    border-color: blue1 ; 
    border-style: solid; 
    border-width: 2px;
  }

  </style>
  