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
          @click="login_with_google"
        />

        <div class="d-flex flex-end w-75">
          <span @click="passwordForgot" class="primary--text underline pointer font_16">
            رمز عبور خود را فراموش کردید؟
          </span>
        </div>

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
        <img src="/image/login/light.png" alt="png" width="90%">
      </v-col>

      <v-col cols="1" />
    </v-row>
  </v-form>
</template>

<script>
export default {
  data: () => ({
    valid: false,
    loading: false,
    form: {
      username: '',
      password: '',
    },
  }),
  methods: {
    login_with_google() {},
    passwordForgot() {},
    login() {
      this.$reqApi('user/login/', this.form)
        .then((response) => {
          console.log('the response : ', response);

          this.$store.dispatch('auth/login', response).then((data) => {
            this.$router.push('/')
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
  }
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
</style>
