<template>
  <v-row no-gutters>
    <v-col cols="6" class="d-flex justify-center">
      <v-row no-gutters class="justify-center">
        <v-avatar color="primary" width="20%" height="100%" class="">
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
    </v-col>

    <v-col cols="6" class="bg-success">

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
</style>
