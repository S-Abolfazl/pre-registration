<template>
    <div
      class="search-bar"
      :style="{ backgroundColor: bgColor, width: width }"
    >
      <v-icon class="search-icon">mdi-magnify</v-icon>
      <input
        class="search-input"
        type="text"
        placeholder="دنبال چی هستی دوست عزیز؟"
      />
    </div>
  </template>
  
  <script>
  export default {
    props: {
      bgColor: {
        type: String,
        default: "#ffffff", 
      },
      width: {
        type: String,
        default: "100%", 
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
  