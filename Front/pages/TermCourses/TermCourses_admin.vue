<template>
  <v-form >
    <v-col  class="my-4">
      
      <v-row class="align-center mb-6">
        <h1 class="font_43 flex-end mt-6 black1--text">دروس ارائه شده در نیم سال اول</h1>

        <year_card class="font_24" text="1403-1404" ></year_card>
      </v-row>

      <addCourse
      :showAddCourse="showAddCourseModal"
      @course-added="sendNewCourse"
      @close-modal="showAddCourseModal = false"
      />

      <v-row class="mt-14 mr-6 justify-end ">
          <v-col cols="2" >
              <BaseButton 
              text="اضافه کردن درس" 
              color="blue2" 
              border-radius="15px"
              textClass="white1--text"
              class="font_40"
              width="85%"
              @click="show_AddCourse"
              />
              
          </v-col>
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
import BaseButton from '~/components/Base/BaseButton.vue';
import addCourse from '~/components/nextTerm_courses/addCourse.vue';

export default {

  components: {
    Tabledata,
    SearchBar,
    year_card,
    BaseButton,
    addCourse,
  },
  data: () => ({
    
    searchQuery:'',
    showAddCourseModal: false,
    ComponentTabeleData:[
  {
    "courseName": "آزمایشگاه شبکه های کامپیوتری",
    "unit": 1,
    "type": "عملی",
    "capacity": 15,
    "teacherName": "دکتر وزین نژاد",
    
    "schedule": "سه‌شنبه‌ها 19:00-17:00",
    "description": "مدرس: دکتر وزین نژاد"
  },
  {
    "courseName": "مدارهای منطقی",
    "unit": 3,
    "type": "نظری",
    "capacity": 60,
    "teacherName": "مهندس حمیدرضا",
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

    show_AddCourse() {
    this.showAddCourseModal = true;
    },

    sendNewCourse(course){
      axios.post('/api/courses', course)
      .then(response => {
        console.log('Course added successfully:', response.data);
      })
      .catch(error => {
        console.error('Error adding course:', error);
      });
    },
  

    // addCourseToTable(newCourse) {
    
    // this.ComponentTabeleData.push(newCourse);
    // console.log('درس جدید به جدول اضافه شد:', newCourse);
    // },
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
