<template>
  <div>
    <v-row :style="{  padding: '2%' }">
    <!-- Header Section -->
      <v-col cols="9"  >
        <v-row>
        <header>
          <h1 class="font_40" style="text-align: right ">چارت درسی رشته مهندسی کامپیوتر</h1>
        </header>
        <Year text="1400"></Year>
      </v-row>
      </v-col>

      <!-- Chart Select -->
      <v-col  cols="3" class="align-left">
        <ChartSelect width="80%" height="40px" @select="getData" />
      </v-col>
    </v-row>

    <v-row class="align-center no-gutters mr-4" :style="{  paddingTop: '5%', width: '100%' }">
      <!-- Header Section -->
        <header>
          <h1 class="font_20" style="text-align: left;">دوستان برای دیدن پیش نیاز و هم نیاز درس مورد نظر خودتون کافیه که اون درس رو انتخاب کنید.  </h1>
        </header>
    </v-row>

    <v-row class="align-center no-gutters mb-13 mr-4" :style="{  paddingTop: '1%', width: '100%' }">
      <!-- Header Section -->

      <header>
        <h1 class="font_20" style="text-align: left;">دروس اختصاصی به صورت </h1>
      </header>

      <Courses text="  اختصاصي" number="83" color="blue2"></Courses>

      <header>
        <h1 class="font_20" style="text-align: left;">، دروس پایه به صورت  </h1>
      </header>

      <Courses text=" دروس پايه" number="20" color="orange1"></Courses>

      <header>
        <h1 class="font_20" style="text-align: left;">، دروس عمومی به صورت </h1>
      </header>
      <Courses text=" دروس عمومي" number="22" :border="true" color="blue2"></Courses>
      <header>
        <h1 class="font_20" style="text-align: left;">و دروس اختیاری به صورت  </h1>
      </header>
      <Courses text="دروس اختياري" number="15" color="orange1"></Courses>
      <header>
        <h1 class="font_20" style="text-align: left;">نمایش داده شده اند. جمع تمامی واحد ها</h1>
      </header>
        <span class="font_12 white1--text black1 mx-2 pa-2 rounded-circle">140</span>
      <header>
        <h1 class="font_20" style="text-align: left;">ميباشد.</h1>
      </header>
    </v-row>

    <div v-for="(value, key) in the_data.terms" :key="key + '-' + the_data.units[key]">
      <header>
        <h1 class="font_24" style="text-align: right; padding: 2%;">
          ترم {{ getPersianTermLabel(key) }}
          <span style="color: gray;">{{ the_data.units[key] }} واحد</span>
        </h1>
      </header>

      <v-chip-group column multiple>
        <Course
          v-for="course in value"

          :courseName="course.courseName"
          :unit="course.unit"
          :kind="course.kind"
          :coreq="course.coreq"
          :prereq="course.prereq"
        />
      </v-chip-group>

      <hr
        v-if="key != 8"
        style="border: 1px solid gray; margin: 20px 50px;"
      />
    </div>
  </div>
</template>

<script>
import BaseButton from '../Base/BaseButton.vue';
import Year from '../Chart/year.vue';
import Courses from '../Chart/Courses.vue'
import ChartSelect from '../Chart/ChartSelect.vue';
import Course from '../Chart/Course.vue';
export default {
  components:{
    BaseButton,
    Year,
    Courses,
    ChartSelect,
    Course,
  },
  data() {
    return {
      the_data: [],
    }
  },
  mounted() {
    this.getData("even");
  },
  methods: {
    getPersianTermLabel(termNumber) {
      const persianTerms = [
        "اول",
        "دوم",
        "سوم",
        "چهارم",
        "پنجم",
        "ششم",
        "هفتم",
        "هشتم",
      ];
      return persianTerms[termNumber - 1] || termNumber;
    },
    getData(data) {
      if (data == "odd") {
        console.log(data);
      }
      else{
        this.$reqApi("student/chart/", {}, {}, true, 'get')
        .then((response) => {
          this.the_data = response;
        })
        .catch((error) => {
          this.$toast.error(error);
        })
      }
    },
  },
}
</script>

<style>
.inner-circle {
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 50%;
    width: 2.3vw; /* Ensure equal width and height */
    height: 1w;
    margin-right: 1.5rem;
    text-align: center;
    box-sizing: border-box; /* Prevent padding/margin issues */
    margin-left: 0.2rem;
  }
</style>
