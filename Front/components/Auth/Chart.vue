<template>
    <div>
    <Navigationbar :style="{  padding: '2%', position: 'fixed', top: '0', width: '100%', zIndex: '1000' }" ></Navigationbar>
    <v-row class="align-center no-gutters" :style="{  paddingTop: '10%', width: '100%'}">
  <!-- Header Section -->
  <v-col >
    <header>
      <h1 class="font_40" style="text-align: left; ">چارت درسی رشته مهندسی کامپیوتر</h1>
    </header>
  </v-col>

  <v-col >
    <Year text="1400"></Year>
  </v-col>

  <!-- Chart Select -->
  <v-col cols="3" :style="{ paddingLeft: '0' }">
    <ChartSelect width="80%" height="40px" />
  </v-col>
</v-row>

<v-row class="align-center no-gutters" :style="{  paddingTop: '5%', width: '100%' }">
  <!-- Header Section -->
    <header>
      <h1 class="font_20" style="text-align: left;">دوستان برای دیدن پیش نیاز و هم نیاز درس مورد نظر خودتون کافیه که اون درس رو انتخاب کنید.  </h1>
    </header>
</v-row>
<v-row class="align-center no-gutters" :style="{  paddingTop: '1%', width: '100%' }">
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
    <Courses text=" دروس عمومي" number="22" :border=true color="blue2"></Courses>
    <header>
      <h1 class="font_20" style="text-align: left;">و دروس اختیاری به صورت  </h1>
    </header>
    <Courses text=" دروس اختياري" number="15" color="orange1"></Courses>
    <header>
      <h1 class="font_20" style="text-align: left;">نمایش داده شده اند. جمع تمامی واحد ها</h1>
    </header>
    <v-chip
          color="black1"
          class="inner-circle"
        >
        <span class="[ 'font_12', 'white1--text']"  v-html="140">  </span>
    </v-chip>
    <header>
      <h1 class="font_20" style="text-align: left;">ميباشد.</h1>
    </header>

</v-row>


      <div>
      <hr style="border: 1px solid 'gray1'; margin: 20px 50px;" />
      </div>

    <div style="padding-right: 22.5%;">
      <template >
        <div>
          <div v-for="term in courses" :key="term.term" class="courses">
            <v-chip-group
              v-model="selectedCourses"
              column
              multiple
              class="courses-group"
            >
              <Course v-for="course in term.courses" :key="course.id" :text="course.name" />
            </v-chip-group>
          </div>
        </div>
      </template>
    </div>

    <div>
      <hr style="border: 1px solid 'gray1'; margin: 20px 50px;" />
      </div>

      <v-row  class="align-center " style="padding-top: '40px';">


        <v-col cols="2" class="d-flex justify-center" >
          <BaseButton text="ثبت دروس" />
        </v-col>


        <v-col cols="2" class="d-flex justify-center" >
          <BaseButton text="رد کردن" color="gray2" />
        </v-col>
      </v-row>

        <div class="action-buttons">


        </div>



      </div>
    </template>

    <script>
      import BaseButton from '../Base/BaseButton.vue';
      import ChartSelect from '../PassedCourses/ChartSelect.vue';
      import Course from '../PassedCourses/Course.vue';
      import YearSelection from '../PassedCourses/YearSelection.vue';
      import Year from '../Chart/year.vue';
      import Courses from '../Chart/Courses.vue'
      export default {
      components:{
      Course,
      ChartSelect,
      YearSelection,
      BaseButton,
      Year,
      Courses,
      },
      data() {
        return {
          years: ["ورودی 1400", "ورودی 1401", "ورودی 1402"],
          selectedYear: "ورودی 1400",
          courses: [
            {
              "term": 1,
              "courses": [
                { "id": 1, "name": "فیزیک 1" },
                { "id": 2, "name": "ریاضی 1" },
                { "id": 3, "name": "مبانی کامپوتر و برنامه سازی" },
                { "id": 4, "name": "مهارت های کاربردی کامپیوتر" },
                { "id": 5, "name": "زبان خارجی" },
                { "id": 6, "name": "فارسی" }
              ]
            },
            {
              "term": 2,
              "courses": [
                { "id": 7, "name": "برنامه نویسی پیشرفته" },
                { "id": 8, "name": "ریاضی گسسته" },
                { "id": 9, "name": "مدار منطقی" },
                { "id": 10, "name": "معادلات دیفرانسیل" },
                { "id": 11, "name": "فیزیک 2" },
                { "id": 12, "name": "آز فیزیک 2" }
              ]
            },
            {
              "term": 3,
              "courses": [
                { "id": 13, "name": "زبان تخصصی" },
                { "id": 14, "name": "ساختمان داده" },
                { "id": 15, "name": "نظریه زبان ها و ماشین ها" },
                { "id": 16, "name": "معماری کامپیوتر" },
                { "id": 17, "name": "مدارهای الکتریکی و الکترونیکی" },
                { "id": 18, "name": "آز منطقی معماری" },
                { "id": 19, "name": "ریاضی 2" }
              ]
            },
            {
              "term": 4,
              "courses": [
                { "id": 20, "name": "هوش و سیستم خبره" },
                { "id": 21, "name": "سیستم های عامل" },
                { "id": 22, "name": "جبر خطی" },
                { "id": 23, "name": "سیگنال ها و سیستم ها" },
                { "id": 24, "name": "مدار مجتمع دیجیتال" },
                { "id": 25, "name": "روش پژوهش" }
              ]
            },
            {
              "term": 5,
              "courses": [
                { "id": 26, "name": "پایگاه داده" },
                { "id": 27, "name": "ریزپردازنده" },
                { "id": 28, "name": "آز ریزپردازنده" },
                { "id": 29, "name": "آز سیستم عامل" },
                { "id": 30, "name": "شبکه" },
                { "id": 31, "name": "آمار و احتمال" }
              ]
            },
            {
              "term": 6,
              "courses": [
                { "id": 32, "name": "مدرسه تکمیلی" },
                { "id": 33, "name": "الگوریتم" },
                { "id": 34, "name": "تحلیل طراحی سیستم" },
                { "id": 35, "name": "کامپایلر" },
                { "id": 36, "name": "آز شبکه" },
                { "id": 37, "name": "اختیاری" }
              ]
            },
            {
              "term": 7,
              "courses": [
                { "id": 38, "name": "مدرسه تکمیلی" },
                { "id": 39, "name": "الگوریتم" },
                { "id": 40, "name": "تحلیل طراحی سیستم" },
                { "id": 41, "name": "کامپایلر" },
                { "id": 42, "name": "آز شبکه" },
                { "id": 43, "name": "اختیاری" },
                { "id": 44, "name": "اختیاری" }
              ]
            },
            {
              "term": 8,
              "courses": [
                { "id": 45, "name": "مدرسه تکمیلی" },
                { "id": 46, "name": "الگوریتم" },
                { "id": 47, "name": "تحلیل طراحی سیستم" },
                { "id": 48, "name": "کامپایلر" },
                { "id": 49, "name": "آز شبکه" },
                { "id": 50, "name": "اختیاری" },
                { "id": 51, "name": "اختیاری" }
              ]
            }
          ],
          selectedCourses: [],
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
