<template>
    <v-form style="width: 100%;">
        <div >
          <img src="/image/login/resetpassword.png" alt="Lock Icon"  />
        </div>
        <h class="font_30" style="font-weight: bold;">فراموشی رمز عبور</h>
        <p class="font_15" style="margin-top: 5%;">
          برای بازیابی رمزعبور، ایمیل خود را وارد کنید. کد ۴ رقمی ارسال شده را وارد کنید.
        </p>
        <BaseInput
            v-model="email"
            text="آدرس ايميل"
            type="email"
            placeholder=" آدرس ايميل خود را وارد کنید"
            width="100%"
          />

          <BaseButton
            color="primary"
            text="ادامه"
            borderRadius="50px"
            width="50%"
            class="my-5"
          />
        </v-form> 
  </template>
  
  <script>
import BaseButton from '../Base/BaseButton.vue';
import BaseInput from '../Base/BaseInput.vue';

  export default {
    name:"ForgotPassword",
    components:{
        BaseInput,
        BaseButton,
    },
    data() {
      return {
        email: '',
      };
    },
    methods: {
      handleSubmit() {
        console.log(`Reset link sent to ${this.email}`);
        // Add logic for handling password reset request
      },
    },
  };
  </script>
  
  <style scoped>
  
  </style>
  