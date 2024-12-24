<template>
  <v-row no-gutters class="pb-8">
    <v-col cols="6" class="d-flex flex-column justify-center align-center">
      <v-row no-gutters class="my-8 w-65">
        <v-avatar color="primary" class="pointer" width="30%" height="120%" @click="triggerFileInput()">
          <img v-if="previewImage" :src="previewImage" alt="User Avatar" class="w-max h-max" />

          <v-icon v-else dark class="font_112">
            mdi-account
          </v-icon>

          <input type="file" accept="image/*" @change="onFileChange" style="display: none" ref="fileInput" />
        </v-avatar>

        <div class="mr-7">
          <b class="font_35">{{ the_username }}</b>
          <br>
          <b class="font_30">{{ user.student_number }}</b>
          <p class="font_26">{{ $store.state.static.role_types[user.type] }}</p>
        </div>
      </v-row>

      <BaseInput
        text="نام"
        placeholder="نام خود را وارد کنید"
        width="65%"
        borderRadius="99px"
        isPro
        @sabt="sabt($event)"
        v-model="user.first_name"
      />

      <BaseInput
        text="نام خانوادگی"
        placeholder="نام خانوادگی خود را وارد کنید"
        width="65%"
        borderRadius="99px"
        isPro
        @sabt="sabt($event)"
        v-model="user.last_name"
      />

      <BaseInput
        text="شماره موبایل"
        placeholder="شماره موبایل خود را وارد کنید"
        width="65%"
        borderRadius="99px"
        cClass="ltr-item"
        rules="phone"
        isPro
        @sabt="sabt($event)"
        v-model="user.mobile_number"
      />

      <BaseInput
        text="ایمیل"
        placeholder="ایمیل خود را وارد کنید"
        width="65%"
        borderRadius="99px"
        cClass="ltr-item"
        rules="email"
        isPro
        @sabt="sabt($event)"
        v-model="user.email"
      />

      <BaseInput
        text="رمز عبور"
        placeholder="رمز جدید خود را وارد کنید"
        width="65%"
        borderRadius="99px"
        cClass="ltr-item"
        isPro
        @sabt="sabt($event)"
        v-model="user.password"
      />

      <BaseButton
        text="خروج از حساب کاربری"
        outlined
        width="65%"
        color="red1"
        textClass="red1--text"
        borderRadius="99px"
        class="mt-5"
        @click="logout()"
      />

    </v-col>

    <v-col cols="6" class="d-flex justify-center align-center">
      <img src="/image/profile/setting.png" alt="profile" width="87%">
    </v-col>
  </v-row>
</template>

<script>
export default {
  head() {
    return {
      title: 'پروفایل کاربری',
    };
  },
  data: () => ({
    user: {},
    the_username: "",
    previewImage: "",
    selectedFile: null, // Store the selected file for upload
  }),
  mounted() {
    this.$reqApi('/user/detail/', {}, {}, true, 'get')
    .then((response) => {
      this.user = response;
      localStorage.setItem('user', JSON.stringify(this.user));
      this.user.password = '';
    })
    .catch((error) => {
      this.$toast.error(error);
    });
  },
  methods: {
    sabt() {
      this.$reqApi('/user/update/', this.user, {}, true, 'patch')
        .then((_) => {
          localStorage.setItem('user', JSON.stringify(this.user));
          this.user.password = '';
          this.$toast.success("با موفقیت ثبت شد");
        })
        .catch((error) => {
          this.$toast.error(error);
        });
    },
    logout() {
      this.$reqApi(`/user/logout/`)
        .then((_) => {
          localStorage.removeItem('user');
          this.$toast.success("با موفقیت حذف شد");
        })
        .catch((error) => {
          this.$toast.error(error);
        });
    },
    onFileChange(event) {
      const file = event.target.files[0];
      if (file) {
        this.previewImage = URL.createObjectURL(file);
        this.selectedFile = file;
        this.uploadAvatar();
      }
    },
    triggerFileInput() {
      this.$refs.fileInput.click();
    },
    async uploadAvatar() {
      if (!this.selectedFile) return;

      const formData = new FormData();
      formData.append('avatar', this.selectedFile);

      try {
        const response = await this.$reqApi('/user/update/', formData, {}, true, 'patch');
        console.log(response);

        if (response && response.avatar_url) {
          this.user.avatar = response.avatar_url; // Update user avatar URL
          localStorage.setItem('user', JSON.stringify(this.user));
          this.$toast.success("تصویر با موفقیت آپلود شد");
        }
      } catch (error) {
        this.$toast.error("آپلود تصویر با خطا مواجه شد");
      }
    },
  },
};
</script>

<style scoped>
p {
  margin: 0 !important;
}
.w-65 {
  width: 65%;
}
</style>
