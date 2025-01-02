
<template>
  <div>
    <v-row no-gutters class="align-center mx-2 " :style="{  width: '100%'}">

      <h1 class="font_40 flex-end mt-6"> تقویم آموزشی سال تحصیلی</h1>

      <Year class="font_24" text="1403-1404" ></Year>

      <Semester height="60px" class="mr-auto mx-10 mt-7" @update="switchSemester" />
    </v-row>
    <v-row class="align-center no-gutters" :style="{  paddingTop: '1%', width: '100%' }">
        <header>
          <h1 class="font_28" style="text-align: left;">برای دیدن تاریخ، وضعیت مورد نظر خود را انتخاب کنید.</h1>
        </header>
    </v-row>
    <v-row no-gutters class="align-center my-6" :style="{  width: '100%'}">

      <breadcrumb class="ml-9 mr-6"/>
    </v-row>



    <v-row no-gutter class="align-center mx-4 my-5" >
    <b class="font_40 ">زمان انتخاب واحد</b>
    </v-row>
    <v-row class="mr-3 ml-7 my-2 schedule-table-wrapper">
      <table class="schedule-table">
        <thead>
          <tr class="blue2">
            <th class="font_20">زمان</th>
            <th class="font_20">دانشجویان دوره کارشناسی</th>
            <th class="font_20">دانشجویان دوره‌های تحصیلات تکمیلی</th>
          </tr>
        </thead>
        <tbody >
          <tr v-for="row in activeSchedule" :key="row.id">
            <td  class="font_30">{{ row.time }}</td>
            <td v-if="row.id === activeSchedule.length"
              :colspan="2"  class="font_30">{{ row.bachelor }} </td>
            <template v-else>
            <td  class="font_30">{{ row.bachelor }}</td>
            <td  class="font_30">{{ row.postgraduate }}</td>
             </template>
          </tr>
        </tbody>
      </table>
    </v-row>


    <v-col  no-gutters class="align-start my-10 mx-3"  >
      <b class=" font_40 ">یادآوری</b>
      <div class="mx-8">
        <ol>
          <li class="font_30 my-9"  v-for="note in notes" :key="note.id">{{ note.text }}</li>
        </ol>
      </div>
  </v-col>
  </div>
</template>

<script>
import Year from '@/components/Taghvim/year.vue';
import Semester from '@/components/Taghvim/semester_switch.vue';
import breadcrumb from '~/components/Taghvim/breadcrumb.vue';
export default {
  components:{
    Year,
    Semester,
    breadcrumb,
  },
  data() {
    return {
      selectedSemester: 'first',
      schedules: {
        first: [
          {
            id: 1,
            time: 'شنبه 24 شهریور ماه ، از 10صبح',
            bachelor: 'ورودی ۱۳۹۹ و ماقبل ساعت ۸ تا ۱۱ صبح',
            postgraduate: 'کلیه ورودی‌ها',
          },
          {
            id: 2,
            time: 'یکشنبه 25 شهریور ماه ، از 9 صبح',
            bachelor: 'ورودی ۱۴۰۰ ساعت ۸ تا ۱۱ صبح',
            postgraduate: 'کلیه ورودی‌ها',
          },
          {
            id: 3,
            time: 'دوشنبه 26 شهریوره ماه ،1403 از 9 صبح',
            bachelor: 'ورودی ۱۴۰۰ ساعت ۸ تا ۱۱ صبح',
            postgraduate: 'کلیه ورودی‌ها',
          }
        ],
        second: [
          {
            id: 1,
            time: 'شنبه ۱۵ بهمن ماه ۱۴۰۳',
            bachelor: 'ورودی ۱۳۹۹ و ماقبل ساعت ۸ تا ۱۱ صبح',
            postgraduate: 'کلیه ورودی‌ها',
          },
          {
            id: 2,
            time: 'دوشنبه 26 شهریوره ماه ،1403 از 9 صبح',
            bachelor: 'ورودی ۱۴۰۰ ساعت ۸ تا ۱۱ صبح',
            postgraduate: 'کلیه ورودی‌ها',
          },
        ],
      },
      notes: [
        { id: 1, text: 'کلیه دانشجویانی که در زمان حذف و اضافه اقدام به ثبت نام با تاخیر مینمایند مشمول اخذ حداقل واحد خواهند بود.' },
        { id: 2, text: 'آن دسته از دانشجویان مشمول پرداخت شهریه که دارای بدهی مالی هستند باید قبل از زمان انتخاب واحد نسبت به  تعیین تکلیف وضعیت شهریه خود با امور مالی دانشگاه هماهنگی لازم را انجام دهند. در غیر این صورت ثبت نـام و  انتخاب واحد برای ایشان میسر نیست.'},
        { id: 3, text: 'آن دسته از دانشجویانی که در مهلت مقرر اعلام شده، کاربرگ نظرسنجی اساتید را تکمیل ننموده اند، در آخرین روز  انتخاب واحد مجاز به اخذ واحد خواهند بود.' },
        { id: 4, text: 'آن دسته از دانشجویانی که در هر نیمسال تحصیلی در زمان مقرر تعیین شده، بدون کسب اجازه از دانشگاه ثبت نام و  انتخاب واحد ننمایند، منصرف از تحصیل محسوب میشوند و اجازه ادامه تحصیل ندارند.'},
        { id: 5, text: 'دانشجویان، مجاز به انتخاب واحد کمتر از حد نصاب تعیین در آیین نامه های آموزشی (بر حسب سال ورود و مقطع)  نیستند، (مگر به دلایل موجه و خارج از اراده دانشجو که باید به تایید گروه، واحد آموزشی و مدیریت خدمات  آموزشی دانشگاه برسد.)'},
      ],
    };
  },
  computed: {
    activeSchedule() {
      return this.schedules[this.selectedSemester];
    },
  },
  methods: {
    switchSemester(semester) {
      this.selectedSemester = semester;
    },
  },
};
</script>

<style scoped>
.schedule-table-wrapper {
  border-radius: 45px;
  overflow: hidden;
  box-shadow: 0px 0px 20px 3px rgba(0, 0, 0, 0.3) !important;
}

.schedule-table {
  width:100%;
  border-collapse: collapse;

}

.schedule-table th,
.schedule-table td {
  border: 4px solid #D9D9D9;
  padding: 10px;
  text-align: center;

}



.notes-section {
  background: #f9f9f9;
  padding: 15px;
  border-radius: 5px;
}

.notes-list {
  list-style: disc;
  padding-right: 20px;
}
</style>
