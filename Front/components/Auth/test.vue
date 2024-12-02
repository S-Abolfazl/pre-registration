<template>
  <v-form v-model="valid">
    <v-row no-gutters class="d-flex justify-center align-center">

      <v-col cols="1" />
      <!-- main form -->
      <v-col cols="4" class="d-flex flex-column align-center">
        <div class="mb-5">
          <b class="black1--text font_32">ورود به حساب کاربری</b>
        </div>
        <BaseCourse
      outlined-text="ریاضی گسسته"
      filled-text="مدار منطقی"
      chip-color="purple"
      :is-outlined="true"
    />
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
import BaseButton from '../Base/BaseButton.vue';
import BaseCourse from '../Base/BaseCourse.vue';

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
    BaseCourse,
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
