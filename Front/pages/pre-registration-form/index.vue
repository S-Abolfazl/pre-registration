<template>
  <div>
    <!-- First row bar -->
    <v-row no-gutters class="px-5 mt-12 mb-6">
      <BaseButton
        text="ثبت کنم برات؟"
        width="16%"
        borderRadius="25px"
        @click="register()"
        textClass="mr-auto"
        non_box_shodow
        image="/image/pre-registration-form/Clip.png"
        imageStyle="height: 56px; width: 56px; margin-right: auto;"
        class="ml-2"
      />

      <BaseButton
        text="فیلتر کنم برات؟"
        width="14%"
        borderRadius="25px"
        @click="filter()"
        icon="mdi-filter-outline"
        textClass="black1--text"
        iconColor="black1"
        class="mx-2"
        outlined
      />

      <BaseInput
        class="mr-auto"
        placeholder="دنبال چی هستی دوست عزیز؟"
        prependInnerIcon="mdi-magnify"
        width="23%"
        borderRadius="25px"
      />

    </v-row>

    <v-row no-gutters class="w-max">
      <TimeTable :Datas="main_data" />
    </v-row>
  </div>
</template>

<script>
import TimeTable from "~/components/PreRegistrationForm/TimeTable.vue";
export default {
  head() {
    return {
      title: 'پیش ثبت نام',
    }
  },
  components: { TimeTable },
  data: () => ({
    search_data: '',
    main_data: [],
  }),
  beforeMount() {
    this.getDatas();
  },
  methods: {
    register() {},
    filter() {},
    getDatas() {
      this.$reqApi('/registration-form/courses-data/', {}, {}, true, 'get')
      .then((response) => {
          response.forEach(course => {
            this.main_data.push({
              ...course,
              name: course.course.courseName,
              start: `${this.getDate(course.class_time1)} ${String(course.class_start_time)}`,
              end: `${this.getDate(course.class_time1)} ${String(course.class_end_time)}`,
              selected: false,
              disabled: false,
            });

            if (course.class_time1 != course.class_time2) {
              this.main_data.push({
              ...course,
              name: course.course.courseName,
              start: `${this.getDate(course.class_time2)} ${String(course.class_start_time)}`,
              end: `${this.getDate(course.class_time2)} ${String(course.class_end_time)}`,
              selected: false,
              disabled: false,
            });
            }
          });
        })
      .catch((error) => {
        this.$toast.error(error);
      });
    },
    getDate(data) {
      switch (data) {
        case 'شنبه':
          return '2024-11-30';
        case 'یک‌شنبه':
          return '2024-12-1';
        case 'دوشنبه':
          return '2024-12-2';
        case 'سه‌شنبه':
          return '2024-12-3';
        case 'چهارشنبه':
          return '2024-12-4';
        case 'پنج‌شنبه':
          return '2024-12-5';
      }
    }
  }
};
</script>
