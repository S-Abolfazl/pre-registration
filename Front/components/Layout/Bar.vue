<template>
  <v-layout>
    <v-app-bar
      scroll-behavior="collapse"
      color="white1"
      width="90%"
      rounded="pill"
    >
      <template v-slot:prepend>
        <v-list-item
          lines="two"
          :avatar="user.avatar"
          :subtitle="user.role"
          :title="user.username"
        >
        </v-list-item>
      </template>
      <v-spacer></v-spacer>
      <BaseButton
        class="font_20 description" 
        text="پيش ثبت نام"
        color="primary"
        width="10%"
        @click="navigateToPreRegistration"
      ></BaseButton>
      <v-spacer></v-spacer>
      <v-btn icon @click="navigateToFeedback">
  <v-icon>mdi-forum</v-icon>
  <span class="font_20 description" >نظرات</span>
</v-btn>
<v-spacer></v-spacer>
<v-btn icon @click="navigateToNotifications">
  <v-icon>mdi-bell</v-icon>
  <span class="font_20 description" >اعلانات</span>
</v-btn>
<v-spacer></v-spacer>
<v-btn icon @click="navigateToSupport">
  <v-icon>mdi-headset</v-icon>
  <span class="font_20 description"  style="position: relative;">پشتیبانی</span>
</v-btn>
      <v-spacer></v-spacer>
      <img :src="require('~/static/image/panel/sbulogo.png')" alt="sbulogo"  width="4%" height="90%" style=" padding-left: 0.5%">
    </v-app-bar>
  </v-layout>
</template>

<script lang="ts">
import BaseButton from '../Base/BaseButton.vue';

export default {
  data: () => ({
    user: {
      username: 'حسين گرزين',
      avatar: '', // Add a valid avatar URL or leave empty for the fallback image
      role: 'ادمين',
    },
  }),
  methods: {
    navigateToPreRegistration() {
      this.$router.push('/pre-registration'); // Adjust the route path as needed
    },
    navigateToFeedback() {
      this.$router.push('/feedback');
    },
    navigateToNotifications() {
      this.$router.push('/notifications');
    },
    navigateToSupport() {
      this.$router.push('/support');
    },
  },
};
</script>


