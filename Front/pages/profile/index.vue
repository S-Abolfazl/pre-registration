<template>
  <v-row no-gutters class="pb-8">
    <v-col cols="6" class="d-flex flex-column justify-center align-center">
      <v-row no-gutters class="my-8 w-65">
        <v-avatar
          class="pointer hover-avatar"
          width="30%"
          height="100%"
          color="primary"
          @click="triggerFileInput()"
        >
        <div class="hover-content">
          <v-icon dark class="hover-icon">mdi-camera</v-icon>
          <span class="hover-text">تغییر تصویر</span>
        </div>
          <img v-if="previewImage" :src="$store.state.server_url + previewImage" alt="User Avatar" class="w-max h-max icon-dakheli" />

          <v-icon v-else dark class="font_112 icon-dakheli">
            mdi-account
          </v-icon>

          <input type="file" accept="image/*" @change="onFileChange" style="display: none" ref="fileInput" />
        </v-avatar>

        <div class="mr-7">
          <b class="font_35">{{ the_username }}</b>
          <br>
          <b class="font_30">{{ user.username }}</b>
          <p class="font_26">{{ $store.state.static.role_types[user.type] }}</p>
        </div>
      </v-row>

      <BaseInput
        text="نام"
        placeholder="نام خود را وارد کنید"
        width="65%"
        borderRadius="99px"
        isPro
        @sabt="sabt('first_name')"
        v-model="user.first_name"
      />

      <BaseInput
        text="نام خانوادگی"
        placeholder="نام خانوادگی خود را وارد کنید"
        width="65%"
        borderRadius="99px"
        isPro
        @sabt="sabt('last_name')"
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
        @sabt="sabt('mobile_number')"
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
        @sabt="sabt('email')"
        v-model="user.email"
      />

      <BaseInput
        text="رمز عبور"
        placeholder="رمز جدید خود را وارد کنید"
        width="65%"
        borderRadius="99px"
        cClass="ltr-item"
        isPro
        @sabt="sabt('password')"
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
    hover: false,
    selectedFile: null,
  }),
  mounted() {
    this.$reqApi('/user/detail/', {}, {}, true, 'get')
    .then((response) => {
      this.user = response;
      localStorage.setItem('user', JSON.stringify(this.user));
      this.user.password = '';
      this.previewImage = this.user.avatar;
      this.the_username = this.user?.first_name + ' ' + this?.user.last_name;
      if (this.user.first_name == null || this.user.last_name == null){
        this.the_username = "";
      }
    })
    .catch((error) => {
      this.$toast.error(error);
    });
  },
  methods: {
    sabt(data) {
      let form = {
        [data]: this.user[data],
      }

      this.$reqApi('user/update/', form, {}, true, 'patch')
        .then((response) => {
          localStorage.setItem('user', JSON.stringify(this.user));
          this.user.password = '';
          this.$toast.success(response);
        })
        .catch((error) => {
          this.$toast.error(error);
        });
    },
    logout() {
      this.$reqApi(`/user/logout/`, {
        "refresh_token" : localStorage.getItem("refresh_token")
      })
        .then((response) => {
          this.$store.dispatch('auth/error401');
          this.$toast.success(response);
        })
        .catch((error) => {
          console.error(error);
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
    uploadAvatar() {
      if (!this.selectedFile) return;
      const formData = new FormData();
      formData.append('avatar', this.selectedFile);
      try {
        this.$reqApi('/user/update/', formData, {}, true, 'patch')
        .then((_) => {
          this.$toast.success("تصویر با موفقیت آپلود شد");
          window.location.reload();
        })
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

.avatar-image {
  display: block;
  width: 100%;
  height: 100%;
  transition: opacity 0.3s ease;
}

.hover-content {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.hover-icon {
  font-size: 24px;
  margin-bottom: 8px;
}

.hover-text {
  font-size: 14px;
  color: #000;
  background: #E8E8E9;
  padding: 4px 8px;
  border-radius: 8px;
  font-weight: bold;
}

.hover-avatar:hover .hover-content {
  opacity: 1;
}

.hover-avatar:hover .icon-dakheli {
  opacity: 0.2;
}

.hover-avatar:hover .avatar-image {
  opacity: 0.3;
}
</style>
