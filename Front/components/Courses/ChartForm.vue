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
    <ChartSelect width="80%" height="40px" />
  </v-col>
</v-row>

    <v-row class="align-center no-gutters" :style="{  paddingTop: '5%', width: '100%' }">
      <!-- Header Section -->
        <header>
          <h1 class="font_20" style="text-align: left;">دوستان برای دیدن پیش نیاز و هم نیاز درس مورد نظر خودتون کافیه که اون درس رو انتخاب کنید.  </h1>
        </header>
    </v-row>
    <v-row class="align-center no-gutters mb-13" :style="{  paddingTop: '1%', width: '100%' }">
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
    <div v-for="(term, index) in courses" :key="term.term">
    <header>
      <h1 class="font_24" style="text-align: right; padding: 2%;">
        ترم {{ getPersianTermLabel(term.term) }}
        <span style="color: gray;">{{ sumCourseNumbers(term.courses) }} واحد</span>
      </h1>
    </header>
    <v-chip-group column multiple>
      <Course
        v-for="course in term.courses"
        :key="course.id"
        :text="course.name"
        :number="course.number"
        :kind="course.kind"
      />
    </v-chip-group>
    <hr
      v-if="index + 1 !== courses.length"
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
    sumCourseNumbers(courses) {
      return courses.reduce((sum, course) => sum + (course.number || 0), 0);
    }
  },
  data() {
      return {
        courses: [
      {
        term: 1,
        courses: [
          { id: 1, name: "فیزیک 1", kind: "پايه", number: 3 },
          { id: 2, name: "ریاضی 1", kind: "پايه", number: 3 },
          { id: 3, name: "مبانی کامپوتر و برنامه سازی", kind: "اختصاصي", number: 3 },
          { id: 4, name: "مهارت های کاربردی کامپیوتر", kind: "اختصاصي", number: 1 },
          { id: 5, name: "زبان خارجی", kind: "عمومي", number: 2 },
          { id: 6, name: "فارسی", kind: "عمومي", number: 2 },
        ],
      },
      {
        term: 2,
        courses: [
          { id: 7, name: "برنامه نویسی پیشرفته", kind: "اختصاصي", number: 3 },
          { id: 8, name: "ریاضی گسسته", kind: "اختصاصي", number: 3 },
          { id: 9, name: "مدار منطقی", kind: "اختصاصي", number: 3 },
          { id: 10, name: "معادلات دیفرانسیل", kind: "پايه", number: 3 },
          { id: 11, name: "فیزیک 2", kind: "پايه", number: 3 },
          { id: 12, name: "آز فیزیک 2", kind: "پايه", number: 1 },
        ],
      },
      {
        term: 3,
        courses: [
          { id: 13, name: "زبان تخصصی", kind: "اختصاصي", number: 2 },
          { id: 14, name: "ساختمان داده", kind: "اختصاصي", number: 3 },
          { id: 15, name: "نظریه زبان ها و ماشین ها", kind: "اختصاصي", number: 3 },
          { id: 16, name: "معماری کامپیوتر", kind: "اختصاصي", number: 3 },
          { id: 17, name: "مدارهای الکتریکی و الکترونیکی", kind: "اختصاصي", number: 3 },
          { id: 18, name: "آز منطقی معماری", kind: "اختياري", number: 1 },
          { id: 19, name: "ریاضی 2", kind: "پايه", number: 3 },
        ],
      }
    ],
  }
}

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
  }</style>
