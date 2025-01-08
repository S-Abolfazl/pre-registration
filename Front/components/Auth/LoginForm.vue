<template>
  <v-form v-model="valid">
    <v-row no-gutters class="d-flex justify-center align-center">

      <v-col cols="1" />
      <!-- main form -->
      <v-col cols="4" class="d-flex flex-column align-center">
        <div class="mb-5">
          <b class="black1--text font_32">ورود به حساب کاربری</b>
        </div>

        <BaseInput
          v-model="form.username"
          text="ایمیل یا نام کاربری"
          rules="require"
          placeholder="آدرس ایمیل یا نام کابری خود را وارد کنید"
          width="75%"
          cClass="ltr-item"
          help_text="نام کاربری برای دانشجویان، همان شماره دانشجویی میباشد"
        />

        <BaseInput
          v-model="form.password"
          text="رمز عبور"
          rules="require, passwoed"
          placeholder="رمز عبور خود را وارد کنید"
          type="password"
          width="75%"
          cClass="ltr-item"
        />

        <div class="div-line">
          <hr class="line" />
          <span class="mx-4"> یا </span>
          <hr class="line" />
        </div>

        <BaseButton
          color="white1"
          text="ورود با گوگل"
          textClass="black1--text"
          outlined
          svg="image/login/google.png"
          width="75%"
          class="my-5"
          @click="loginWithGoogle"
        />

        <div class="d-flex flex-end w-75">
          <span @click="toggleForgotPassword" class="primary--text underline pointer font_16">
            رمز عبور خود را فراموش کردید؟
          </span>
        </div>

        <ForgotPassword @reset-password="handleResetPassword" :dialog="dialog" />

        <BaseButton
          color="primary"
          text="وارد شوید"
          borderRadius="50px"
          width="75%"
          class="my-5"
          :disabled="!valid || loading"
          @click="login"
        />

        <div class="d-flex flex-end w-75">
          <span class="font_16">
            حساب کاربری ندارید؟
          </span>
          <span @click="signup" class="primary--text underline pointer font_16 mr-1">
            ثبت نام کنید
          </span>
        </div>
      </v-col>

      <!-- the img -->
      <v-col cols="5" class="d-flex justify-center align-center">
        <img
          :src="this.$vuetify.theme.dark ? '/image/login/dark.png' : '/image/login/light.png'"
          alt="png"
          width="90%"
        >
      </v-col>

      <v-col cols="1" />
    </v-row>
  </v-form>
</template>


<script>
import ForgotPassword from '../Login/ForgotPassword.vue';

export default {
  components:{
    ForgotPassword,
  },
  data: () => ({
    dialog: false,
    valid: false,
    loading: false,
    form: {
      username: '',
      password: '',
    },
    showForgotPassword: false,
  }),
  methods: {
    toggleForgotPassword() {
      this.dialog = !this.dialog;
    },
    handleResetPassword(email) {
      this.$reqApi("/api/reset-password", { email })
      .then((response) => {
        console.log(response);
      })
      .catch((error) => {
        this.$toast.error(error);
      })
    },
    login() {
      this.$reqApi('user/login/', this.form)
        .then((response) => {
          this.$store.dispatch('auth/login', response).then((data) => {
            this.$toast.success("با موفقیت وارد شدید")
            this.$router.push('/')
            localStorage.setItem('isDark', false);
          })
        })
        .catch((error) => {
          console.log('the error : ', error);
          this.loading = false
        })
    },
    signup() {
      this.$router.push('/auth/signup');
    },
    loginWithGoogle() {
      const clientId = '854888124710-lr4quh2biu4dk5pe87gboq8pusfv1225.apps.googleusercontent.com';
      const redirectUri = `${this.$store.state.server_url}/user/login-google`;
      const scope = 'https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile';
      const responseType = 'code';

      // Construct the Google OAuth URL
      const authUrl = `https://accounts.google.com/o/oauth2/v2/auth?client_id=${clientId}&redirect_uri=${redirectUri}&response_type=${responseType}&scope=${scope}`;

      // Redirect the user to Google for authentication
      window.location.href = authUrl;
    },
  },
}
</script>
<style scoped>
  .line {
    width: 45%;
    color: #CBCAD7 !important;
  }
  .div-line {
    width: 75%;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .underline {
    text-decoration: underline;
  }
  .w-75 {
    width: 75%;
  }
  .overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
  }
  .modal {
    background: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    z-index: 1001;
  }
</style>
