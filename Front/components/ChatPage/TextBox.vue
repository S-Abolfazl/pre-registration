<template>
    <div class="text-box">
      <button @click="sendText" class="send-button">
        <div class="circle">
          <v-icon class="icon">mdi-send</v-icon>
        </div>
      </button>
      <input
        type="text"
        v-model="inputText"
        placeholder="تایپ کن..."
        @keydown.enter="sendText"
        class="input-field"
      />
      <v-icon color="black">mdi-emoticon</v-icon>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        inputText: "",
      };
    },
    methods: {
      sendText() {
        if (this.inputText.trim()) {
          this.$emit("send", this.inputText); // Emit the message to the parent component
          this.inputText = ""; // Clear the input field after sending
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .text-box {
    display: flex;
    align-items: center;
    border-radius: 30px;
    padding: 5px 10px;
    width: 100%;
  }
  
  .input-field {
    flex: 1;
    border: none;
    outline: none;
    font-size: 16px;
    padding: 5px 10px;
    direction: rtl;
  }
  
  .send-button {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 40px;
    height: 40px;
    border: none;
    background: none;
    cursor: pointer;
    padding: 0;
  }
  
  .circle {
    width: 40px;
    height: 40px;
    background-color: #7b5ff1;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .icon {
    color: white;
    font-size: 20px;
  }
  </style>
  