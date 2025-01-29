<template>
    <div v-if="visible" class="chat-container" style="width: 25%;">
      <!-- Support Header -->
      <div class="support-header">
        <v-row class="flex-column">
          <div class="d-flex align-center" style="padding-right: 15px;">
            <img class="support-image" :src="support.profileImage" alt="Support">
            <div>
              <h2 class="font_16">{{ support.name }}</h2>
              <p class="gray2--text font_10">پشتیبان شماره {{ support.number }}</p>
            </div>
            <button @click="close" style="padding-right: 140px;">
              <div class="circle">
                <v-icon class="icon">mdi-close</v-icon>
              </div>
            </button>
          </div>
          <div class="mt-1" style="padding-right: 50px; padding-left: 50px;">
            <p class="font_30" style="font-weight: bold;">پشتیبانی</p>
            <p class="font_16">هر سوالی که داری بپرس ولی من فک نمیکنم سوالی برات پیش اومده باشه</p>
          </div>
        </v-row>
      </div>
  
      <div class="chat-container">
        <div class="chat-messages">
          <ChatBubble
            v-for="(message, index) in messages"
            :key="index"
            :message="message.text"
            :isSupport="message.isSupport"
            :senderName="message.senderName"
            :time="message.time"
          />
        </div>
      </div>
  
      <!-- Input Area -->
      <div class="text-box-wrapper">
        <TextBox
  v-model="inputText"
  placeholder="تایپ کن..."
  @send="sendMessage"
/>

      </div>
    </div>
  </template>
  
  <script>
  import ChatBubble from '../ChatPage/ChatBubble.vue';
  import TextBox from '../ChatPage/TextBox.vue';
  
  export default {
    components: { ChatBubble, TextBox },
    data() {
      return {
        visible: true, // Controls the visibility of the template
        support: {
          name: "رامک خارجی",
          number: 63,
          profileImage: require("~/static/image/chatpage/support.png"),
        },
        messages: [
          {
            text: "سلام خوبی پشتیبان جان",
            isSupport: false,
            senderName: "کاربر",
            time: "2025-01-26T17:30:00.000Z",
          },
          {
            text: "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است",
            isSupport: true,
            senderName: "پشتیبان",
            time: "2025-01-26T17:30:00.000Z",
          },
          {
            text: "سلام خوبی پشتیبان جان",
            isSupport: false,
            senderName: "کاربر",
            time: "2025-01-26T17:30:00.000Z",
          },
          {
            text: "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است",
            isSupport: true,
            senderName: "پشتیبان",
            time: "2025-01-26T17:30:00.000Z",
          },
        ],
        inputText: "",
      };
    },
methods: {
  sendMessage(message) {
    if (message.trim()) {
        const messageTimeUTC = new Date();
      // Append new user message to the chat
      this.messages.push({
        text: message,
        isSupport: false,
        senderName: "کاربر",
        time: new Date(new Date()+messageTimeUTC.getTimezoneOffset()),
    });

      // Simulate a response from the backend
      setTimeout(() => {
        this.messages.push({
          text: "ممنون بابت پیام شما، در اولین فرصت پاسخ می‌دهیم.",
          isSupport: true,
          senderName: "پشتیبان",
          time: new Date(new Date()+messageTimeUTC.getTimezoneOffset())
        });
      }, 1000);

      // Clear the input field
      this.inputText = "";
    }
  },
  close() {
    this.visible = false; // Hides the entire template
  },
},

  };
  </script>
  
  <style scoped>
  .chat-container {
    height: 500px;
    display: flex;
    flex-direction: column;
    border-radius: 8px;
    overflow: hidden;
  }
  
  .circle {
    width: 40px;
    height: 40px;
    background-color: #ffffff33;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .support-header {
    display: flex;
    align-items: center;
    background: linear-gradient(100deg, #ff8b37, #7b5ff1) !important;
    color: white;
    padding: 10px;
    border-radius: 4% 4% 0 0;
  }
  
  .support-image {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    margin: 20px;
  }
  
  .chat-messages {
    overflow-y: auto;
    padding: 10px;
    box-sizing: border-box;
    border-radius: 8px;
  }
  
  .text-box-wrapper {
    padding: 10px;
    background: white;
  }
  </style>
  