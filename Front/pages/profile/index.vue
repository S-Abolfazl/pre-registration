<template>
  <v-row no-gutters class="mtop pb-8">
    <v-col cols="6" class="d-flex flex-column justify-center align-center">
      <v-row no-gutters class="justify-center mb-12 w-max">
        <v-avatar color="primary" width="20%" height="100%">
          <img
            v-if="user.avatar"
            :src="user.avatar"
            alt="user"
          >
          <v-icon v-else dark class="font_112">
            mdi-account
          </v-icon>
        </v-avatar>

        <div class="mr-7">
          <b class="font_35">{{ user.first_name }}  {{ user.last_name }}</b>
          <br>
          <b class="font_30">{{ user.student_number }}</b>
          <p class="font_26">{{ user.role }}</p>
        </div>
      </v-row>

      <BaseInput
        text="نام و نام خانوادگی"
        placeholder="نام و نام خانوادگی خود را وارد کنید"
        width="65%"
        borderRadius="99px"
      />

      <BaseInput
        text="شماره موبایل"
        placeholder="شماره موبایل خود را وارد کنید"
        width="65%"
        borderRadius="99px"
        cClass="ltr-item"
        rules="phone"
      />

      <BaseInput
        text="ایمیل"
        placeholder="ایمیل خود را وارد کنید"
        width="65%"
        borderRadius="99px"
        cClass="ltr-item"
        rules="email"
      />

      <BaseInput
        text="رمز عبور"
        placeholder="رمز جدید خود را وارد کنید"
        width="65%"
        borderRadius="99px"
        cClass="ltr-item"
      />

      <BaseButton
        text="خروج از حساب کاربری"
        outlined
        width="65%"
        color="red1"
        textClass="red1--text"
        borderRadius="99px"
        class="mt-5"
      />

    </v-col>

    <v-col cols="6" class="d-flex justify-center align-center">
      <img src="/image/profile/setting.png" alt="progile" width="87%">
    </v-col>
  </v-row>
</template>

<script>
export default {
  layout: "profile",
  head(){
    return {
      title: 'پروفایل کاربری'
    }
  },
  data: () => ({
    user: {
      avatar: "",
      first_name: "حسین",
      last_name: "گرزین",
      student_number: "400243068",
      role: "دانشجو"
    }
  }),
  methods: {},
}
</script>
<style scoped>
p{
  margin: 0 !important;
}
.mtop {
  margin-top: -4%;
}
</style>
