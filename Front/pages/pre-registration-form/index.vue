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

      <Filteration @passed_courses="passed_courses" @course_type="course_type" />

      <BaseInput
        class="mr-auto"
        placeholder="دنبال چی هستی دوست عزیز؟"
        prependInnerIcon="mdi-magnify"
        width="23%"
        borderRadius="25px"
        @input="search"
      />
    </v-row>

    <v-row no-gutters class="w-max">
      <TimeTable :Datas="detail_data" />
    </v-row>
  </div>
</template>

<script>
import TimeTable from "~/components/PreRegistrationForm/TimeTable.vue";
import Filteration from "~/components/PreRegistrationForm/Filteration.vue";
export default {
  head() {
    return {
      title: 'پیش ثبت نام',
    }
  },
  components: { TimeTable, Filteration },
  data: () => ({
    main_data: [],
    detail_data: [],
  }),
  beforeCreate() {
    this.$reqApi('/student/completed-courses/', {}, {}, true, 'get')
    .then((response) => {
      if (response.completed_courses.length == 0) {
        this.$toast.error("ابتدا دروسی که پاس کرده اید را مشحص کنید");
        this.$router.push('/passed-courses');
      }
      localStorage.setItem("passed_courses", response.completed_courses)
      })
    .catch((error) => {
      this.$toast.error(error);
    });
  },
  beforeMount() {
    this.getDatas();
    this.detail_data = this.main_data;
  },
  methods: {
    register() {},
    search(data) {
      this.detail_data = this.main_data.filter((course) =>
        course.name.toLowerCase().includes(data.toLowerCase())
      );
    },
    getDatas() {
      this.$reqApi('/registration-form/courses-data/', {}, {}, true, 'get')
      .then((response) => {
        let validate_courses = this.validCourses(response);

        validate_courses.forEach(course => {
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
    },
    validCourses(courses) {
      const timeRegex = /^([01]\d|2[0-3]):([0-5]\d)$/;

      return courses.filter(
        (course) =>
          course.class_start_time &&
          timeRegex.test(course.class_start_time)
      );
    },
    passed_courses() {
      this.$reqApi('/registration-form/courses-data/prereq-filter/', {}, {}, true, 'get')
      .then((response) => {
        let validate_courses = this.validCourses(response);

        validate_courses.forEach(course => {
          this.detail_data.push({
            ...course,
            name: course.course.courseName,
            start: `${this.getDate(course.class_time1)} ${String(course.class_start_time)}`,
            end: `${this.getDate(course.class_time1)} ${String(course.class_end_time)}`,
            selected: false,
            disabled: false,
          });

          if (course.class_time1 != course.class_time2) {
            this.detail_data.push({
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
    course_type(type) {
      if (!type) {
        this.detail_data = this.main_data;
      }
      this.detail_data = this.main_data.filter(
        (course) => course.course.type == this.get_type(type)
      );
    },
    get_type(type) {
      switch (type) {
        case "اختصاصي":
          return "theory_course";
        case "عمومي":
          return "public_course";
        case "پايه":
          return "basic_course";
        case "عملی":
          return "practical_course";
        case "اختياري":
          return "elective_course";
      }
    },
  }
};
</script>
