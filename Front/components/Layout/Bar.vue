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
      <v-menu
      v-model="menuVisible"
      offset-y
      transition="slide-y-transition"
      content-class="menu-wrapper"
      top
      max-height="60%"
      max-width="25%"
      >
      <template v-slot:activator="{ on }">
      <v-avatar color="primary" class="pointer" @click="toggleMenu()">
        <img
          v-if="user.avatar"
          :src="$store.state.server_url + user.avatar"
          alt="user"
        >
        <v-icon v-else dark class="font_35">
          mdi-account
        </v-icon>
      </v-avatar>
    </template>
    <user_menu :width="'400px'"/>
  </v-menu>

      <div class="mr-2">
        <v-row no-gutters>
          <b class="font_20">{{ user.first_name }} {{ user.last_name }}</b>
        </v-row>
        <v-row no-gutters>
          <span class="font_20">{{ getRole(user.type) }}</span>
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
      <img
        :src="require('~/static/image/panel/sbulogo.png')"
        alt="sbulogo"
        width="4%"
        height="90%"
        style=" padding-left: 0.5%"
        class="pointer"
        @click="goToPanel()"
        >
    </v-app-bar>
  </v-layout>
</template>

<script lang="ts">
import user_menu from '../Panel/user_menu.vue';

export default {
  components: {
    user_menu,
  },
  data: () => ({
    menuVisible: false,
    user: {
      first_name: "",
      last_name: "",
      avatar: "",
      name: "",
      type: "",
    },
  }),
  mounted(){
    this.$reqApi('/user/detail/', {}, {}, true, 'get')
    .then((response) => {
      this.user = response;
      this.the_username = this.user.first_name + ' ' + this.user.last_name;
    })
    .catch((error) => {
      this.$toast.error(error);
    });
  },
  methods: {
    navigateToPreRegistration() {
      this.$router.push('/pre-registration-form'); // Adjust the route path as needed
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
    toggleMenu() {
      this.menuVisible = !this.menuVisible;
    },
    goToPanel() {
      this.$router.push('/panel');
    },
    getRole(data) {
      return this.$store.state.static.role_types[data]
    }
  },
};
</script>

<style scoped>
.bar {
  box-shadow: none !important;
}
.v-app-bar.v-toolbar.v-sheet {
  border-color: #D9D9D9 !important;
  margin-top: 12px !important;
}
.menu-wrapper {
  border-radius: 30px;
}
</style>
