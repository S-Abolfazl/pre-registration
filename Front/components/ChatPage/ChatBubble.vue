<template>
  <div style="padding: 10px;">
    <!-- Support Message -->
     <!-- Profile Image Outside the Bubble -->
      <div v-if="isSupport">
        <v-row>
  <!-- Message Bubble -->
  <v-col cols="10"  style="text-align: left;">
    <div style="text-align: left; padding-bottom: 5px;">
      <span class="font_18" style="font-weight: bold;">{{ senderName }}</span>
    </div>
    <div 
      class="black1--text font_16 gray4 "
      style="display: inline-block; word-wrap: break-word; padding: 10px; border-radius: 0 12px 12px 12px; "
    >
      {{ message }}
    </div>
  </v-col>
  <!-- Profile Image -->
  <v-col cols="2">
    <img
      class="w-10 h-10 rounded-full"
      :src="require('~/static/image/chatpage/support.png')"
      alt="Support Profile"
    />
  </v-col>
</v-row>



    </div>
    <!-- User Message -->
    <div
      v-else
      class=" white1--text font_32 blue2 "
      style="display: inline-block; word-wrap: break-word; padding: 10px; border-radius: 12px 0 12px 12px;"
    >
      <div >
        <div class="rounded-xl p-4 max-w-md bg-blue-400">
          {{ message }}
        </div>
      </div>
    </div>

    <div 
    :style="{
    paddingTop: '5px',
    textAlign: isSupport ? 'left' : 'right',
    paddingLeft:'55px'
  }"
    >
      <span class="gray5--text text-xs">{{ displayTime }}</span>
    </div>
  </div>
</template>

<script>
export default {
  name: "ChatBubble",
  props: {
    message: {
      type: String,
      required: true,
    },
    isSupport: {
      type: Boolean,
      required: true,
    },
    senderName: {
      type: String,
      default: "",
    },
    profileImage: {
      type: String,
      default: "~/static/image/chatpage/support.png",
    },
    time: {
      type: String,
      required: true, // Should be passed as a string in a parsable format, e.g., "2025-01-27T15:30:00Z"
    },
  },
  data() {
    return {
      currentTime: new Date(),
    };
  },
  
  methods: {
    formatTime(date) {
      // Format the time as 'HH:mm' in Iran Standard Time (IRST)
      return date.toLocaleString("fa-IR", {
        hour: "2-digit",
        minute: "2-digit",
        hour12: false, // 24-hour format
      });
    },
    updateTime() {
      this.currentTime = new Date();
    },
  },
  computed: {
    displayTime() {
  // Parse the message time and ensure it's treated as UTC
  const messageTimeUTC = new Date(this.time);

  // Convert UTC time to local time by creating a localized string
  const messageTimeLocal = new Date(messageTimeUTC.getTime() + messageTimeUTC.getTimezoneOffset() * 60000); // Apply local offset

  // Get the current time in UTC
  const currentTime = new Date(new Date()-messageTimeUTC.getTimezoneOffset()); // Current time in system local time

  // Calculate the difference in seconds
  const diffInSeconds = Math.floor((currentTime - messageTimeLocal) / 1000);

  // Debugging logs
  console.log("Raw Input Time (UTC):", this.time);
  console.log("Message Time (UTC):", messageTimeLocal); // Message time in UTC
  console.log("Current Time (UTC):", currentTime); // Current time in UTC
  console.log("Difference in Seconds:", diffInSeconds); // Time difference in seconds

  // Handle past and future messages
   if (diffInSeconds < 60) {
    return "همین الان"; // Just now
  } else {
    return this.formatTime(messageTimeLocal); // Format for past messages
  }
}

  // Cal


  },
  mounted() {
    this.timer = setInterval(this.updateTime, 1000); // Update time every second
  },
  beforeUnmount() {
    clearInterval(this.timer); // Clear the timer when the component is destroyed
  },
};
</script>

<style scoped>
/* Optional additional styling */
</style>


