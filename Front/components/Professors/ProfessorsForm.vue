<template>
    <div>
   <v-row :style="{  padding: '2%' }">
  <!-- Header Section -->
  <v-col cols="8"  >
    <h1 class="font_40" style="text-align: right; margin-bottom: 2%;">اساتید دانشکده مهندسی کامپیوتر بهشتی</h1>
    <h2 class="font_24" style="text-align: right">برای انتخاب واحد بهتر و آشنایی بیشتر با اساتید میتونید در این صفحه نظرات دانشجویان ببینید </h2>
    <SearchBar style="margin-top: 8%;" width="70%"></SearchBar>
  </v-col>

  <!-- Chart Select -->
  <v-col  cols="4" >
    <img
          src='~/static/image/professors/Collaborate 1.png'
          alt="png"
          width="90%"
        >
  </v-col>
</v-row>

    <v-row class="align-center no-gutters mb-13" :style="{  paddingTop: '1%', width: '100%' }">
      <v-col cols="8">
        <div v-for="(term, index) in courses" :key="term.term">
    
        </div>
      </v-col>

      <v-cols cols="4">
        <profCard
    name="رامک قوامی زاده مبیدی"
    profileImage="https://example.com/profile.jpg"
    description="خوب کلا حضور غیاب نمیکنن و فکر نمیکنم خیلی براشون اهمیت داشته باشه ولی خیلی حساس به اینکه دانشجو وسط کلاس پاشه بره مخصوصا اگر دیر هم اومده باشه به دیر اومدن حساس خودشون میگن مشکلی ندارن با اینکه نیاید ولی میگن بیاید باید بشینین کلاس خشکی ندارن و گاها بین حرف شوخی میکنن با بچه ها ( نه شوخی آزار دهنده رو اعصاب و برعکس حال هوای کلاس عوض میکنه)  سوالات درس منطقی و همون چیزی پرسیدن جواب میدن بعد کلاس با حوصله جواب هر کی هر سوال باشه میدن  تمرین با نظرات استاد به دست میرسه یک کوچلو خلاقیتی و بازمه فکر کنید ولی خوب امتحانش راحته و زیادن و یکم جواب آخر براشون مهمه و یک شرط حداقل دارن اونم اینکه نصف نمره پایانترم بایدبیا ید ویلا حل تمرین کامل باشه  میندازن و تعارفی ندارن و یک صدم هم کمک نمیکنن اما اگر میانترم خراب کنید و پایانترم خوب بدید میانترم تاثیر صفر میشه حل تمرین امتیازی دارن و کلاسا حل تمرین خوبه و نمره مازاد  اگر شرکت کنید ،داره این پوینت خوبی بارم مثل اینکه ۵ نمره حل تمرین اما واقعیتا هنوز نمیدونم چقدر میانترم چقدر پایانترم ولی نمره هر امتحان میدن و زود تصحیح میکنن در کل استاد خوبی هستن ولی خوب سال بالایی میگن یکم دست به تصحیح سختی دارن خوش نمره نیستن ولی در کل بین تی ای هامون کسانی هستن که ۲۰ هم گرفتن 
هنوز نمرات نیومده ولی به شناختی ازشون پیدا کردم و تدریس خوبشون 
ولی خوب حل تمرینش واقعا دست به تصحیح خوبی ندارن و سختگیرانه تکلیف تصحیح میکنن 
"
    phone="29904183"
    email="R-Ghavami@sbu.ac.ir"
    :rating="4"
    role="استاديار"
    faculty="مهندسی و علوم کامپیوتر "
    field=" نرم افزار و سامانه های اطلاعاتي"
    degree="دكتري"
    degreeDiscreption="دانشگاه علم و صنعت ایران - تهران، مهندسی کامپیوتر - معماری كامپيوتر"
  />

      </v-cols>

 
    </v-row>
    </div>

</template>

<script>
import BaseButton from '../Base/BaseButton.vue';
import Year from '../Chart/year.vue';
import Courses from '../Chart/Courses.vue'
import ChartSelect from '../Chart/ChartSelect.vue';
import Course from '../Chart/Course.vue';
import SearchBar from '../ProfessorsComponents/searchBar.vue';
import profCard from '../ProfessorsComponents/profCard.vue';
import ProfCard from '../ProfessorsComponents/profCard.vue';
export default {
  components:{
    BaseButton,
    Year,
    Courses,
    ChartSelect,
    Course,
    SearchBar,
    ProfCard,
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
