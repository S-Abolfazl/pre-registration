<template>
  <v-form v-model="valid">
    <v-row no-gutters class="d-flex justify-center align-center">

      <v-col cols="1" />
      <!-- main form -->
      <v-col cols="4" class="d-flex flex-column align-center">
        <div class="mb-5">
          <b class="black1--text font_32">ورود به حساب کاربری</b>
        </div>
        <YearSelection>

        </YearSelection>
        <Course
      text="ریاضی گسسته"
      chip-color="purple"
      :is-outlined="true"
    />
    <ChartSelect></ChartSelect>
        <BaseButton text="here"/>


        <div class="div-line">
          <hr class="line" />
          <span class="mx-4"> یا </span>
          <hr class="line" />
        </div>


      </v-col>

 
      <v-col cols="1" />
    </v-row>
  </v-form>
</template>

<script>
import { Chart } from 'chart.js';
import BaseButton from '../Base/BaseButton.vue';
import ChartSelect from '../PassedCourses/ChartSelect.vue';
import Course from '../PassedCourses/Course.vue';
import YearSelection from '../PassedCourses/YearSelection.vue';

export default {
  data: () => ({
    valid: false,
    loading: false,
    form: {
      username: '',
      password: '',
    },
  }),
  components:{
    Course,
    ChartSelect,
    YearSelection,
  },
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
