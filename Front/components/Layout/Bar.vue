<template>
  <v-layout>
    <v-app-bar
      scroll-behavior="collapse"
      color="white1"
      width="90%"
      outlined
      rounded="pill"
      class="bar mx-4"
    >
      <v-avatar color="primary" class="pointer" @click="user_menu()">
        <img
          v-if="user.avatar"
          :src="user.avatar"
          alt="user"
        >
        <v-icon v-else dark class="font_35">
          mdi-account
        </v-icon>
      </v-avatar>

      <div class="mr-2">
        <v-row no-gutters>
          <b>{{ user.role }}</b>
        </v-row>
        <v-row no-gutters>
          <span>{{ user.username }}</span>
        </v-row>
      </div>
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
    user_menu(){
      console.log('user menu');
    }
  },
};
</script>

<style scoped>
.bar {
  box-shadow: none !important;
}
.theme--light.v-app-bar.v-toolbar.v-sheet {
  border-color: #D9D9D9 !important;
  margin-top: 12px !important;
}
</style>
