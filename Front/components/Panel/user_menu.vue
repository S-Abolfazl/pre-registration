<template>
  <v-card
    class="menu-container" :width="width"
  >
    <list dense class="menu-list">
      <!-- profile item-->
      <v-list-item @click="goToProfile" class="v-list-item-custom">
        <img src="image/panel/profile.png" class="menu-icon" alt="profile" />
        <span class="menu-text font_24">حساب کاربری</span>
      </v-list-item>
      <!-- course item -->
      <v-list-item @click="goToLessons" class="v-list-item-custom">
        <img src="image/panel/course.png" class="menu-icon" alt="courses" />
        <span class="menu-text font_24">دروس پاس شده</span>
      </v-list-item>
      <!-- settings item -->
      <v-list-item @click="goToSettings" class="v-list-item-custom">
        <img src="image/panel/setting.png" class="menu-icon" alt="settings" />
        <span class="menu-text font_24">تنظیمات</span>
      </v-list-item>


      <v-divider></v-divider>

      <!-- آیتم زبان -->
      <v-list-item class="v-list-item-custom">
        <img src="image/panel/world.png" class="menu-icon" alt="languge" />
        <span class="menu-text font_24">زبان</span>
        <span class="current-language font_20">{{ currentLanguage }}</span>
      </v-list-item>

      <v-divider></v-divider>

      <!-- حالت شب -->
      <v-list-item class="v-list-item-custom">
        <img src="image/panel/moon.png" class="menu-icon" alt="Night" />
        <span class="menu-text font_24">حالت شب</span>
        <v-switch v-model="darkMode" class="ml-auto"></v-switch>
      </v-list-item>

      <v-divider></v-divider>

      <!-- خروج -->
      <v-list-item @click="logout" class="v-list-item-custom">
        <v-icon class="menu-icon" color="red">mdi-logout</v-icon>
        <span class="menu-text text-red font_24">خروج از حساب کاربری</span>
      </v-list-item>
    </list>
  </v-card>
</template>

<script>
export default {
  props:{
      width: {
      type: String,
      default: '100%',
    },
    },
    data() {
    return {
      darkMode: false,
      currentLanguage: 'فارسی',
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
  width: 50px;
  height: 600px;
  display: flex;
  flex-direction: column; 
  border-radius: 30px;
  overflow: hidden;
  background-color: rgba(0, 0, 0, 0.61);
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
}

.v-list-item-custom:hover {
  background-color: rgba(255, 255, 255, 0.1);  
}

.menu-icon {
  width: 15%; /* اندازه آیکون */
  height: 32px;
  margin-right: 16px; /* فاصله بین آیکون و متن */
  object-fit: contain; /* حفظ نسبت ابعاد تصویر */
  border-radius: 4px; /* در صورت نیاز به گوشه‌های گرد */
}

.menu-text {
  flex: 1;
  color: white;
  margin-right: 10px;
}

.current-language {
  color: white;
  margin-left: auto;
}

.text-red {
  color: red;
}

</style>
