<template>
  <v-form v-model="valid">
    
    <v-col  class="my-4">
      
      <v-row class="align-center">
        <v-col cols="12" md="6" class="d-flex align-center">
          <span>
            <b class="black1--text font_43">دروس ارائه شده در نیم سال اول </b>
          </span>
          <v-card class="year-card blue2 ml-4">
            <v-row no-gutters>
              <span class="title">
                <b class="font_40 black1--text">1403-1404</b>
              </span>
              <span class="image-wrapper">
                <img src="/image/panel/term_courses.png" alt="course" class="course-image" />
              </span>
            </v-row>
          </v-card>
        </v-col>
      </v-row>

      <v-row class="mt-4">
        <v-col cols="12" class="d-flex justify-start">
          <SearchBar />
        </v-col>
      </v-row>

      <v-row class="mt-4">
        <BaseTable />
      </v-row>
    </v-col>
  </v-form>
</template>

<script>
import BaseTable from '~/components/nextTerm_courses/Table.vue';
import SearchBar from '~/components/nextTerm_courses/SearchBar.vue';
export default {
  components: {
    BaseTable,
    SearchBar,
  },
  data: () => ({
    title: 'پنل اصلی',
  }),
  computed: {},
  beforeMount() {
    this.$store.dispatch('setPageTitle', this.title);
  },
  methods: {},
};
</script>

<style scoped>
.year-card {
  border-radius: 30px;
  width: auto;
  max-width: 250px;
  height: auto;
  padding: 10px;
  margin: 10px;
  position: relative;
  overflow: visible;
  display: flex;
  align-items: center;
  justify-content: center;
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
.title {
  margin: 0;
  text-align: center;
}

.v-row {
  margin-bottom: 20px;
}

.search-bar {
  width: 100%;
}

.search-bar > div {
  justify-content: flex-start;
}

.ml-4 {
  margin-left: 16px;
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
