
<template>
  <div class="course-selection" >
    <v-row no-gutters class="align-center ">
      <!-- Header Section -->
      <v-col cols="8">
        <header>
          <h1 style="font-size: x-large;">سلام دوستان</h1>
          <h2 style="font-size: x-large;">برای شروع، دروس پیش ترم های پیش کرده اید را انتخاب کنید.</h2>
        </header>
      </v-col>
      <!-- Year Selection -->
      <v-col cols="2" class="d-flex justify-center">
        <YearSelection
          years="years"
          v-model="selectedYear"
          height="40px"
          width="200px"

        />
      </v-col>
      <!-- Chart Select -->
      <v-col cols="2" class="d-flex justify-center" >
        <ChartSelect
          width="200px"
          height="40px"
        />
      </v-col>
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
    export default {
    components:{
    Course,
    ChartSelect,
    YearSelection,
    BaseButton,
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

