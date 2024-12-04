
  <template>
    <div class="course-selection">
        <v-row no-gutters class="d-flex justify-end" >
    <v-col cols="8" class="d-flex flex-column" >
        <header>
            <h1>سلام دوستان</h1>
            <h2>برای شروع، دروس پیش ترم های پیش کرده اید را انتخاب کنید.</h2>
        </header>
    </v-col>

    <v-col cols="2" class="d-flex flex-column">
        <YearSelection :years="years" v-model="selectedYear" />
    </v-col>
    
    <v-col cols="2" class="d-flex flex-column">
        <ChartSelect width="100%"></ChartSelect>
    </v-col>
    
    
</v-row>

      <div class="top-row">
        
        <div class="column year-column">
          
        </div>
        <div class="column text-column">
          <p>برای شروع، دروس پیش ترم های پیش کرده اید را انتخاب کنید.</p>
        </div>
      </div>
  
      <div class="courses">
        <v-chip-group
          v-model="selectedCourses"
          column
          multiple
          class="courses-group"
        >
          <Course v-for="course in courses" :key="course.id" :text="course.name" />
        </v-chip-group>
      </div>
  
      <div class="action-buttons">
        <BaseButton text="ثبت دروس" />
        <BaseButton text="رد کردن" color="secondary" />
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
          { id: 1, name: "فیزیک 1" },
          { id: 2, name: "ریاضی 1" },
          { id: 3, name: "مدار منطقی" },
          { id: 4, name: "معادلات دیفرانسیل" },
          { id: 5, name: "هوش و سیستم خبره" },
          { id: 6, name: "سیستم عامل" },
          { id: 7, name: "آمار و احتمال" },
          { id: 8, name: "فیزیک 2" },
          { id: 9, name: "ریاضی 2" },
          { id: 10, name: "زبان خارجی" },
          { id: 11, name: "برنامه نویسی پیشرفته" },
          { id: 12, name: "ساختمان داده" },
          { id: 13, name: "طراحی الگوریتم" },
          { id: 14, name: "مدارهای الکتریکی و الکترونیکی" },
          { id: 15, name: "شبکه های کامپیوتری" },
          { id: 16, name: "سیگنال ها و سیستم ها" },
          { id: 17, name: "مدار مجتمع دیجیتال" },
          { id: 18, name: "روش پژوهش" },
          { id: 19, name: "نظریه زبان ها و ماشین ها" },
          { id: 20, name: "معماری کامپیوتر" },
          { id: 21, name: "پایگاه داده" },
          { id: 22, name: "آزمایشگاه مدار منطقی" },
          { id: 23, name: "مهارت های کاربردی کامپیوتر" },
          { id: 24, name: "زبان تخصصی" },
          { id: 25, name: "مدیریت پروژه" },
          { id: 26, name: "مهندسی نرم افزار" },
          { id: 27, name: "تحلیل داده ها" },
          { id: 28, name: "آمار پیشرفته" },
          { id: 29, name: "هوش مصنوعی" },
          { id: 30, name: "سیستم های اطلاعاتی" },
          { id: 31, name: "مدلسازی ریاضی" },
          { id: 32, name: "نظریه گراف" },
          { id: 33, name: "امنیت اطلاعات" },
          { id: 34, name: "سیستم های توزیع شده" },
          { id: 35, name: "مبانی پردازش تصویر" },
          { id: 36, name: "یادگیری ماشین" },
          { id: 37, name: "طراحی دیجیتال" },
          { id: 38, name: "پردازش زبان طبیعی" },
          { id: 39, name: "الگوریتم های پیشرفته" },
          { id: 40, name: "مدارهای پیشرفته" },
          { id: 41, name: "مدلسازی سیستم ها" },
          { id: 42, name: "تحلیل سیستم ها" },
          { id: 43, name: "فناوری ابری" },
          { id: 44, name: "محاسبات کوانتومی" },
          { id: 45, name: "ریاضی گسسته" },
          { id: 46, name: "رایانش موازی" },
          { id: 47, name: "شبکه های عصبی" },
          { id: 48, name: "مدارهای منطقی پیشرفته" },
          { id: 49, name: "برنامه نویسی وب" },
          { id: 50, name: "تحلیل داده های بزرگ" },
          { id: 51, name: "مهندسی کامپیوتر" },
        ],
        selectedCourses: [],
      };
    },
  };
  </script>
  
  <style scoped>
  .course-selection {
    padding: 20px;
  }
  
  
  .top-row {
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
  }
  
  .column {
    flex: 1;
    padding: 10px;
  }
  
  .chart-column {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  
  .courses {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    justify-content: center;
    margin-bottom: 20px;
  }
  
  .action-buttons {
    display: flex;
    justify-content: flex-end;
    gap: 10px;
  }
  
  .v-chip-group {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
  }
  </style>