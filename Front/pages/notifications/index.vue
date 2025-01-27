<template>
  <v-form v-model="valid">
    <v-col  class="my-4">
      
      <v-row class="my-10 mr-12">
        <h1 class="mb-8 font_45 ">پیام ها و اطلاعیه ها</h1>
      </v-row>

      <v-row class="justify-center">
        <v-col cols="12">
          <message_cart
            :announcements="announcements.data"
            card-color="blue2"
            text-color="white1--text  "
            :border-radius="20"
          />
        </v-col>
      </v-row>

    </v-col>
  </v-form>
</template>

<script>
import message_cart from '~/components/notification/message_cart.vue';  
export default {

  components: {
    message_cart,
  },
  data: () => ({
    announcements:{
    "msg": "ok",
    "data": [
      {
        "title": "افزودن درس",
        "content": "درس مدارهای مجتمع دیجیتال ارائه شده توسط استاد جهانیان علی در روز شنبه و دوشنبه و در ساعت  13 - 15 افزوده شد",
        "created_at": "2025-01-16T15:13:58.314007Z"
      },
      {
        "title": "افزودن درس",
        "content": "درس مبانی امنیت سایبری ارائه شده توسط استاد عباسپور مقصود در روز یک‌شنبه و سه‌شنبه و در ساعت  10 - 12 افزوده شد",
        "created_at": "2025-01-16T15:13:58.325008Z"
      },
      {
        "title": "افزودن درس",
        "content": "درس پروژه کارشناسی ارائه شده توسط استاد اساتید گروه آموزشی افزوده شد",
        "created_at": "2025-01-16T15:13:58.337038Z"
      },
      {
        "title": "افزودن درس",
        "content": "درس طراحی بازی های رایانه ای ارائه شده توسط استاد وحیدی اصل مجتبی در روز یک‌شنبه و سه‌شنبه و در ساعت  09 - 10 افزوده شد",
        "created_at": "2025-01-16T15:13:58.349103Z"
      },
      {
        "title": "افزودن درس",
        "content": "درس هوش مصنوعی مقدماتی ارائه شده توسط استاد متقی مریم السادات در روز یک‌شنبه و سه‌شنبه و در ساعت  15 - 17 افزوده شد",
        "created_at": "2025-01-16T15:13:58.360581Z"
      },
      {
        "title": "افزودن درس",
        "content": "درس هوش مصنوعی مقدماتی ارائه شده توسط استاد غفاری کرامت اله در روز شنبه و دوشنبه و در ساعت  15 - 17 افزوده شد",
        "created_at": "2025-01-16T15:13:58.371906Z"
      },
      {
        "title": "افزودن درس",
        "content": "درس کارآموزی ارائه شده توسط استاد اساتید گروه آموزشی افزوده شد",
        "created_at": "2025-01-16T15:13:58.383315Z"
      }
    ],
    "status": 200
    }
  }),
  head(){
    return {
      title: '  '
    }
  },
  computed: {
  },
  beforeMount() {
    //this.$store.dispatch('setPageTitle', this.title);
    // this.$store.dispatch('setTableData', this.TabeleData);
  },
  methods: {
  },
};
</script>

<style scoped>
.year-card {
  border-radius: 30px;
  width: auto;
  max-width: 250px;
  height: auto;
  padding: 10px;
  margin: 20px;
  position: relative;
  overflow: visible;
  display: flex;
  align-items: center;
  justify-content: center;
}

.table{
  margin-left: 10px;
}
.searchbar{
  margin-left: 40px;
}

.image-wrapper {
  position: absolute;
  top: -53%;
  left: 27%;
  transform: translateX(-50%);
  width: 35%;
}
.course-image {
  width: 100%;
}

.v-row {
  margin-bottom: 20px;
}



@media (max-width: 768px) {
  .year-card {
    max-width: 200px;
  }

  .image-wrapper {
    top: -40%;
    width: 40%;
  }
}
</style>
