<template>
    <v-form v-model="valid">
      <v-row no-gutters class="d-flex">

        <v-col cols="2" />
        <!-- main form -->
        <v-col cols="4" class="d-flex flex-column align-center">
          <div class="mb-5">
            <b class="black1--text font_32">ثبت نام</b>
          </div>

          <BaseAutocomplete
            v-model="form.type"
            :items="userTypes"
            placeholder="نوع كاربري خود را مشخص كنيد"
            rules="require"
            width="75%"
            text="نوع كاربر"
          />


          <BaseInput
            v-model="form.username"
            text=" نام کاربری"
            rules="require"
            placeholder=" نام کابری خود را وارد کنید"
            width="75%"
            help_text="نام کاربری برای دانشجویان، همان شماره دانشجویی میباشد"
          />

          <BaseInput
            v-model="form.email"
            text="آدرس ايميل"
            rules="require"
            type="email"
            placeholder=" آدرس ايميل خود را وارد کنید"
            width="75%"
          />


          <BaseInput
            v-model="form.password"
            text="رمز عبور"
            rules="require"
            placeholder="رمز عبور خود را وارد کنید"
            type="password"
            width="75%"
            help_text="رمز عبور باید شامل حداقل 8 کاراکتر، حروف کوچک و بزرگ، عدد و کاراکتر های خاص باشد"
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
            svg="image/signup/google.png"
            width="75%"
            class="my-5"
            @click="Signup_with_google"
          />



          <BaseButton
            color="primary"
            text="ثبت نام"
            borderRadius="50px"
            width="75%"
            class="my-5"
            :disabled="!valid || loading"
            @click="signup"
          />

          <div class="d-flex flex-end w-75">
            <span class="font_16">
              حساب کاربری دارید؟
            </span>
            <span @click="login" class="primary--text underline pointer font_16 mr-1">
              وارد شويد
            </span>
          </div>
        </v-col>

        <!-- the img -->
        <v-col cols="5" class="d-flex justify-center align-center">
          <img
            :src="this.$vuetify.theme.dark ? '/image/signup/dark.png' : '/image/signup/light.png'"
            alt="png"
            width="90%"
          >
        </v-col>

        <v-col cols="1" />
      </v-row>
    </v-form>
  </template>

  <script>
import BaseAutocomplete from '../Base/BaseAutocomplete.vue';

  export default {
    data: () => ({
      valid: false,
      loading: false,
      form: {
        username: '',
        password: '',
        email: '',
        type: '',
      },
      userTypes: [],
    }),
    mounted() {
      this.userTypes = this.$store.state.static.user_types;
    },
    methods: {
      Signup_with_google() {},
      signup() {
        this.$reqApi('user/signup/', this.form)
          .then((response) => {
            this.$store.dispatch('auth/login', response)
            .then((_) => {
              this.$toast.success("با موفقیت وارد شدید")
              this.$router.push('/')
            })
          })
          .catch((error) => {
            this.loading = false
          })
      },
      login() {
        this.$router.push('/auth/login');
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
