<template>
  <v-form v-model="valid">
    <v-col  class="my-4">
      
      <v-row class="align-center">
        <h1 class="font_43 flex-end mt-6 black1--text"> تقویم آموزشی سال تحصیلی</h1>

        <year_card class="font_24" text="1403-1404" ></year_card>
      </v-row>

      <v-row class="mt-4 justify-end ">
        <v-col cols="3" class="mr-auto searchbar">
          <SearchBar @search-updated="handleSearchUpdate" />
        </v-col>
      </v-row>

      <v-row class="mt-4 table">
        <Tabledata :TableData="ComponentTabeleData"/>
      </v-row>
    </v-col>
  </v-form>
</template>

<script>
import Tabledata from '~/components/nextTerm_courses/Table.vue';
import SearchBar from '~/components/nextTerm_courses/SearchBar.vue';
import year_card from '~/components/nextTerm_courses/year_card.vue';

export default {

  components: {
    Tabledata,
    SearchBar,
    year_card,
  },
  data: () => ({
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
],
  DataSearch:[],
}),
  watch:{
    searchQuery(newvalue){
      const query = newvalue.toLowerCase();
      this.ComponentTabeleData = this.ComponentTabeleData.filter(
      (item) =>
        Object.values(item)
            .join(' ')
            .toLowerCase()
            .includes(query)
          )
    }
  },
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
    handleSearchUpdate(newSearch) {
      this.searchQuery = newSearch;   
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
