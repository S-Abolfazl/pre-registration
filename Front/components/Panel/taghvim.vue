<template>
  <div>
    <v-card class="taghvim-card white1" elevation="3" @click="goToTaghvim">
      <v-row no-gutters align="center">
        <!-- متن توضیحات -->
        <v-col cols="6" >
          <div class="title">
            <b class="font_43">تقویم آموزشی</b>
          </div>
          <div class="font_20 description" >
          زمان انتخاب واحد، شروع کلاس ها و امتحاناتو اینجا ببینید.
          </div>
        </v-col>

        <!-- تصویر موشک و مرد -->
        <v-col cols="6" class="d-flex justify-center">
          <div class="image-wrapper">
            <img src="/image/panel/tagvim.png" alt="tagvim" class="taghvim-image" />
          </div>
        </v-col>
      </v-row>
    </v-card>
  </div>
</template>

<script>
    export default {
      methods: {
        goToTaghvim() {
          this.$router.push('/panel/Taghvim');
        },
      },
    };
</script>

<style scoped>
.taghvim-card {
  box-shadow: 0px 0px 20px 3px rgba(0, 0, 0, 0.3) !important;
  border-radius: 25px;
  border: 3px solid #7B5FF1;
  width: 25%; 
  height: 280px; 
  margin: auto;
  position: relative; /* برای کنترل موقعیت فرزندان مطلق */
  overflow: visible; /* اجازه دهید تصویر از کارت بیرون بزند */
  box-shadow: 200px 0px 20px rgba(0, 0, 0, 0.2);

}

.image-wrapper {
  position: absolute;
  top: 30%; 
  right: 5%; 
  width: 100%;
  display: flex;
  justify-content: flex-end;
}

.taghvim-image {
  width: 65%; /* تنظیم سایز تصویر */
}
.title{
  margin: 16px 14px auto auto;
  width: 150%;
}
.description {
  margin: 30px 14px auto auto;
  width: 100%; /* تنظیم سایز تصویر */
}
</style>
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
