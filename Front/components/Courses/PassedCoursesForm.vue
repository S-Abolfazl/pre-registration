<template>
  <div class="course-selection" >
    <v-row no-gutters class="align-center ma-5">
      <!-- Header Section -->
      <v-col cols="8">
        <header>
          <h1 style="font-size: x-large;">سلام دوستان</h1>
          <h2 style="font-size: x-large;">
            برای شروع، دروسی که در ترم های پیش پاس کرده اید را انتخاب کنید.</h2>
        </header>
      </v-col>
      <!-- Year Selection -->
      <v-col cols="2" class="d-flex justify-center">
        <!-- <YearSelection
          years="years"
          v-model="selectedYear"
          height="40px"
          width="200px"

        /> -->
      </v-col>
      <!-- Chart Select -->
      <v-col cols="2" class="d-flex justify-center" >
        <!-- <ChartSelect
          width="200px"
          height="40px"
        /> -->
      </v-col>
    </v-row>

    <div>
    <hr style="border: 1px solid 'gray1'; margin: 20px 50px;" />
    </div>

  <div style="padding-right: 22.5%;">
    <template >
      <div v-for="(courses, termNumber) in terms" :key="termNumber" class="courses">
      <v-chip-group
        column
        multiple
        class="courses-group"
      >
        <template v-for="(course, courseIndex) in courses">
          <Course2
            v-if="course.courseName != 'اختیاری'"
            :key="courseIndex"
            :course="course"
          />
          <Course
            v-else

          />
        </template>
      </v-chip-group>
    </div>
    </template>
  </div>

  <div>
    <hr style="border: 1px solid 'gray1'; margin: 20px 50px;" />
    </div>

    <v-row  class="align-center " style="padding-top: '40px';">
      <v-col cols="2" class="d-flex justify-center" >
        <BaseButton text="ثبت دروس" @click="sabt" />
      </v-col>

      <v-col cols="2" class="d-flex justify-center" >
        <BaseButton text="رد کردن" color="gray2" />
      </v-col>
    </v-row>
    <div class="action-buttons"></div>
  </div>
</template>

<script>
import BaseButton from '../Base/BaseButton.vue';
import ChartSelect from '../PassedCourses/ChartSelect.vue';
import Course from '../PassedCourses/Course.vue';
import Course2 from '../PassedCourses/Course2.vue';
import YearSelection from '../PassedCourses/YearSelection.vue';
export default {
  components:{
    Course,
    Course2,
    ChartSelect,
    YearSelection,
    BaseButton,
  },
  data() {
    return {
      years: ["ورودی 1400", "ورودی 1401", "ورودی 1402"],
      selectedYear: "ورودی 1400",
      terms: [],
      elective_course: [],
    }
  },
  mounted() {
    this.$reqApi("/student/courses/", {}, {}, true, 'get')
    .then((response) => {
      this.terms = response.terms;
      this.elective_course = response.elective_course;
    })
    .catch((error) => {
      this.$toast.error(error);
    })
  },
  methods: {
    sabt() {
      const passedCourseIds = [];
      for (const levelKey in this.terms) {
        const level = this.terms[levelKey];

        for (const courseKey in level) {
          const course = level[courseKey];
          if (course.passed) {
            passedCourseIds.push(course.id);
          }
        }
      }

      this.$reqApi("/student/selecet-passed-course/", {"course_ids" : passedCourseIds})
      .then((response) => {
        this.$toast.success("درس های انتخاب شده با موفقیت به لیست دروس گذارنده شده اضافه شدند");
      })
      .catch((error) => {
        this.$toast.error(error);
      });
    },
  },
}
</script>

