<template>
  <v-form v-model="valid">
    <v-col  class="my-4">

      <v-row class="my-10 mr-12">
        <h1 class="mb-8 font_45 ">پیام ها و اطلاعیه ها</h1>
      </v-row>

      <v-row class="justify-center">
        <v-col cols="12">
          <message_cart
            :announcements="announcements"
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
    announcements:[],
  }),
  head(){
    return {
      title: 'پیام ها و اطلاعیه ها'
    }
  },
  mounted() {
    this.getDatas();
  },
  methods: {
    getDatas() {
      this.$reqApi('notification/', {}, {}, true, 'get')
      .then((response) => {
        this.announcements = response
      })
      .catch((error) => {
        this.$toast.error(error);
      });
    },
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
