<template>
    <v-card
      class="menu-container"
    >
      <v-list dense class="menu-list">
        <!-- آیتم‌های منو -->
        <v-list-item v-for="(item, index) in menuItems" :key="index" @click="item.action" class="v-list-item-custom">
          <v-icon class="menu-icon">{{ item.icon }}</v-icon>
          <span class="menu-text">{{ item.text }}</span>
        </v-list-item>
  
        <v-divider></v-divider>
  
        <!-- آیتم زبان -->
        <v-list-item class="v-list-item-custom">
          <v-icon class="menu-icon">mdi-earth</v-icon>
          <span class="menu-text">زبان</span>
          <span class="current-language">{{ currentLanguage }}</span>
        </v-list-item>
  
        <v-divider></v-divider>
  
        <!-- حالت شب -->
        <v-list-item class="v-list-item-custom">
          <span class="menu-text">حالت شب</span>
          <v-switch v-model="darkMode" class="ml-auto"></v-switch>
        </v-list-item>
  
        <v-divider></v-divider>
  
        <!-- خروج -->
        <v-list-item @click="logout" class="v-list-item-custom">
          <v-icon class="menu-icon" color="red">mdi-logout</v-icon>
          <span class="menu-text text-red">خروج از حساب کاربری</span>
        </v-list-item>
      </v-list>
    </v-card>
  </template>
  
  <script>
  export default {
    data() {
      return {
        darkMode: false,
        currentLanguage: 'فارسی',
        menuItems: [
          { text: 'حساب کاربری', icon: 'mdi-account', action: this.goToProfile },
          { text: 'دروس پاس شده', icon: 'mdi-book', action: this.goToLessons },
          { text: 'تنظیمات', icon: 'mdi-cog', action: this.goToSettings },
        ],
      };
    },
    methods: {
      goToProfile() {
        console.log('Navigate to profile');
      },
      goToLessons() {
        console.log('Navigate to lessons');
      },
      goToSettings() {
        console.log('Navigate to settings');
      },
      logout() {
        console.log('Logged out');
      },
    },
  };
  </script>
  
  <style scoped>
  .menu-container {
    width: 300px;
    height: 500px;
    display: flex;
    flex-direction: column; /* آیتم‌ها را عمودی بچین */
    border-radius: 30px;
    overflow: hidden;
    background-color: rgba(0, 0, 0, 0.8); /* پس‌زمینه شفاف */
    box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.3); /* سایه برای عمق */
  }
  
  .menu-list {
    flex: 1;
    display: flex;
    flex-direction: column;
    margin: 0;
    padding: 0;
  }
  
  .v-list-item-custom {
    display: flex;
    align-items: center;
    padding: 12px 16px;
    cursor: pointer;
    background-color: rgba(0, 0, 0, 0.29);
    flex-grow: 1; /* برای پر کردن فضا */
    min-height: 60px; /* حداقل ارتفاع */
    justify-content: space-between; /* فضای بین متن و آیکون را توزیع کن */
    transition: background 0.2s;
  }
  
  .v-list-item-custom:hover {
    background-color: rgba(255, 255, 255, 0.1); /* افکت هاور */
  }
  
  .menu-icon {
    font-size: 30px;
  }
  
  .menu-text {
    flex: 1;
    color: white;
    margin-right: 10px;
  }
  
  .current-language {
    color: white;
    font-size: 14px;
    margin-left: auto;
  }
  
  .text-red {
    color: red;
  }
  
  .v-switch {
    margin-right: auto;
  }
  </style>
  