<template>
    <div class="btn-toggle-wrapper" width="100%" :style="{ height: height }">
      <v-btn-toggle
        v-model="selected"
        :rounded='true'
        class="custom-btn-toggle"
        mandatory
        :width="width"
        :style="{ height: height }"
        color="blue2"
        @change="updateSelect"
      >
        <v-btn
          v-for="(option, index) in options"
          :key="index"
          :value="option.value"
          class="toggle-btn"
          :class="{ 'selected-btn': selected === option.value }"
          :text="selected !== option.value"
          :style="{ height: height }"
          color="blue2"
          @change="updateSelect"
        >
          {{ option.text }}
        </v-btn>
      </v-btn-toggle>
    </div>
  </template>

  <script>
  export default {
    name:"Semester",
    data() {
      return {
        selected: "first",
        options: [
          { value: "first", text: "نیم سال اول" },
          { value: "second", text: "نیم سال دوم" },
        ],
      };
    },
    props: {
      width: {
        type: String,
        default: '300px'
      },
      height: {
        type: String,
        default: '100px',
      },
    },
    methods: {
      updateSelect() {
        this.$emit("update", this.selected); // مقدار انتخاب‌شده را به والد ارسال می‌کند.
      },
   },
};
  </script>

  <style scoped>
  /* Wrapper for alignment */
  .btn-toggle-wrapper {
    display: flex;
    justify-content: center !important;
    align-items: center !important;
  }

  /* Custom style for the toggle container */
  .custom-btn-toggle {
    border: 2px solid ;
    border-radius: 50px; /* Fully rounded container */
    overflow: hidden; /* Ensure selected button stays rounded */
  }

  /* Base button styles */
  .toggle-btn {
  font-weight: bold;
  font-size: 14px;
  background-color: white;
  border: none;
  width: 50%;
  text-align: center; /* Horizontal centering */

  display: flex;           /* Enable Flexbox */
  justify-content: center; /* Center horizontally */
  align-items: center;     /* Center vertically */
}


  /* Selected button styling */
  .selected-btn {
    color: white !important;
    border-radius: 50px !important;
    border:none !important;
  }
  </style>
