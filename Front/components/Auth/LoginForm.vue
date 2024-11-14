<template>
  <div>
    <BaseInput
      text="ایمیل یا نام کاربری"
      placeholder="آدرس ایمیل یا نام کابری خود را وارد کنید"
      width="50%"
    />

    <BaseInput
      text="رمز عبور"
      placeholder="رمز عبور خود را وارد کنید"
      type="password"
      width="50%"
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
      icon="google"
      width="300px"
    />

    <div>
      <span @click="passwordForgot" class="primary--text underline pointer">
        رمز عبور خود را فراموش کردید؟
      </span>
    </div>

    <BaseButton
      color="primary"
      text="وارد شوید"
      borderRadius="50px"
      width="300px"
    />

    <div>
      <span class="">
        حساب کاربری ندارید؟
      </span>
      <span @click="signup" class="primary--text underline pointer">
        ثبت نام کنید
      </span>
    </div>
  </div>
</template>

<script>
export default {
  data: () => ({
    username: '',
    password: '',
  }),
  methods: {
    passwordForgot() {},
    signup() {},
  }
}
</script>
