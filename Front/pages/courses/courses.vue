<template>
  
  <v-form v-model="valid">
    <Navigationbar></Navigationbar>
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

      <v-row class="mt-4 justify-end ">
        <v-col cols="3" class="mr-auto searchbar">
          <SearchBar v-model:searchQuery="searchQuery"/>
        </v-col>
      </v-row>

      <v-row class="mt-4 table">
        <Table :TableDate="ComponentTabeleData"/>
      </v-row>
    </v-col>
  </v-form>
</template>

<script>
import Table from '~/components/nextTerm_courses/Table.vue';
import SearchBar from '~/components/nextTerm_courses/SearchBar.vue';
// import { filter } from 'core-js/core/array';
import Navigationbar from '~/layouts/navigationbar.vue';
export default {
  layouts:'Navigationbar',

  components: {
    Table,
    SearchBar,
  },
  data: () => ({
    title: 'پنل اصلی',
    searchQuery:'',
    ComponentTabeleData:[
  {
    "courseName": "آزمایشگاه شبکه های کامپیوتری",
    "unit": 1,
    "type": "عملی",
    "capacity": 15,
    "teacher": "دکتر وزین نژاد",
    "schedule": "سه‌شنبه‌ها 19:00-17:00",
    "description": "مدرس: دکتر وزین نژاد"
  },
  {
    "courseName": "مدارهای منطقی",
    "unit": 3,
    "type": "نظری",
    "capacity": 60,
    "teacher": "مهندس حمیدرضا",
    "schedule": "یک‌شنبه 09:00-12:00",
    "description": "امتحان: 13/03/1403"
  }
]
,
  }),
  watch:{
    searchQuery(newvalue){
      const query = newvalue.toLowerCase();
      this.ComponentTabeleData = this.tableItems.filter(
      (item) =>
        Object.values(item)
            .join(' ')
            .toLowerCase()
            .includes(query)
          )
    }
  },
  computed: {
  },
  beforeMount() {
    this.$store.dispatch('setPageTitle', this.title);
    // this.$store.dispatch('setTableData', this.TabeleData);
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
