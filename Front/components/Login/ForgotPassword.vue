<template>
  <v-dialog :value="dialog" width="500">
    <v-card width="100%" height="100%" color="white1">
      <v-form v-model="valid" class="d-flex flex-column justify-center align-center" @submit.prevent="handleSubmit">
        <img src="/image/login/resetpassword.png" alt="Lock Icon" width="30%" class="mt-5" />
        <h2 class="font_30" style="font-weight: bold;">فراموشی رمز عبور</h2>
        <p class="font_15" style="margin-top: 5%;">
          برای بازیابی رمزعبور، ایمیل خود را وارد کنید. کد ۴ رقمی ارسال شده را وارد کنید.
        </p>
        <BaseInput
          v-model="email"
          text="آدرس ايميل"
          type="email"
          :rules="emailRules"
          placeholder=" آدرس ايميل خود را وارد کنید"
          width="80%"
        />
        <BaseButton
          color="primary"
          text="ادامه"
          borderRadius="50px"
          width="50%"
          class="my-5"
          :disabled="!valid"
          @click="handleSubmit"
        />
      </v-form>
    </v-card>
  </v-dialog>
</template>

<script>
import BaseButton from "../Base/BaseButton.vue";
import BaseInput from "../Base/BaseInput.vue";

export default {
  name: "ForgotPassword",
  components: {
    BaseInput,
    BaseButton,
  },
  props: {
    dialog: Boolean, // Dialog state managed by the parent component
  },
  data() {
    return {
      email: "", // User email input
      valid: false, // Form validation state
      emailRules: [
        (v) => !!v || "ایمیل الزامی است.",
        (v) => /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/.test(v) || "ایمیل معتبر وارد کنید.",
      ],
    };
  },
  methods: {
    handleSubmit() {
      if (!this.valid) return; // Prevent invalid submissions
      console.log(`Reset link sent to ${this.email}`);
      // Emit the email to the parent or send an API request for password reset
      this.$emit("reset-password", this.email);
      this.$toast.success("لینک بازنشانی به ایمیل ارسال شد");
    },
  },
};
</script>

<style scoped>
/* Center content inside the dialog */
.v-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

/* Adjust styles for fonts and spacing */
.font_30 {
  font-size: 30px;
  margin: 10px 0;
}

.font_15 {
  font-size: 15px;
  color: #666;
  text-align: center;
}

.my-5 {
  margin: 20px 0;
}
</style>
