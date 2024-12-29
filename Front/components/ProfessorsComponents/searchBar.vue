<template>
    <div
      class="search-bar"
      :style="{ backgroundColor: bgColor, width: width }"
    >
    <v-icon class="search-icon" color="black" size="xx-large" style="margin-left: 2%;">mdi-magnify</v-icon>

      <input
        class="search-input"
        type="text"
        placeholder="دنبال كي هستی دوست عزیز؟"
        v-model="internalValue"
        @input="emitSearch"
      />
    </div>
  </template>
  
  <script>


  export default {
    
    props: {
      value: {
        type:String,
      },
      bgColor: {
        type: String,
        default: "#ffffff", 
      },
      width: {
        type: String,
        default: "100%", 
      },
    },
    data() {
    return {
      internalValue: this.value || "", // Local value for input
    };
  },
  watch: {
    // Keep internal value in sync with external prop
    value(newValue) {
      this.internalValue = newValue;
    },
  },
  methods: {
    emitSearch() {
      this.$emit("search", this.internalValue); // Emit the search event
    },
  },
};
  </script>
  
  <style scoped>
  .search-bar {
    display: flex;
    align-items: center;
    max-width: 100%; 
    padding: 8px 16px;
    border: 1px solid rgba(51, 51, 51, 0.6); 
    border-radius: 24px; 
    box-sizing: border-box;
  }
  
  .search-icon {
    color: rgba(51, 51, 51, 0.6); 
    margin-right: 8px;
    font-size: 20px;
  }
  
  .search-input {
    flex: 1;
    border: none;
    outline: none;
    background: transparent;
    color: rgba(51, 51, 51, 0.6); 
    font-size: 16px;
    padding: 0;
  }
  
  .search-input::placeholder {
    color: rgba(51, 51, 51, 0.6); 
  }
  </style>
  