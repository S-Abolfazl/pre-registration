<template>
  <v-container>
    <!--
    6 : شنبه
    0 : یکشنبه
    1 : دوشنبه
    2 : سه شنبه
    3 : چهارشنبه
    -->

    <v-calendar
      ref="calendar"
      type="week"
      start="1403-01-01"
      :events="events"
      :categories="categories"
      :event-color="getEventColor"
      locale="fa"
      :first-interval="6"
      :interval-count="14"
      :interval-minutes="60"
      interval-height="45"
      show-interval-label
      color="primary"
      :interval-format="formatInterval"
      category-show-all
    ></v-calendar>
  </v-container>
</template>

<script>

export default {
  data() {
    return {
      courses: [
        {
          "c_id": "accb296d-13d4-4689-9f6c-488e5360c063",
          "teacherName": "احمدزاده راجی مهرداد",
          "isExperimental": false,
          "class_time1": "چهارشنبه",
          "class_time2": "چهارشنبه",
          "class_start_time": "15:00",
          "class_end_time": "17:00",
          "exam_date": null,
          "exam_start_time": null,
          "exam_end_time": null,
          "capacity": 48,
          "registered": 0,
          "description": null,
          "course": {
            "course_id": "ab7390cd-28cd-49c1-92e3-08b831efd251",
            "courseName": "آزمایشگاه سیستم های عامل",
            "unit": 1,
            "type": "practical_course"
          },
          "selected": false
        },
      ],
      events: [
      {
        name: "یادگیری ماشین",
        start: "1403-01-05 07:30",
        end: "1403-01-05 09:00",
        selected: true,
      },
      {
        name: "Workout",
        start: "2024-12-21 18:00",
        end: "2024-12-21 19:00",
        selected: false,
      },
      ],
      categories: [
        { name: "saturday", text: "شنبه" },
        { name: "sunday", text: "یک‌شنبه" },
        { name: "monday", text: "دو‌شنبه" },
        { name: "tuesday", text: "سه‌شنبه" },
        { name: "wednesday", text: "چهار‌شنبه" },
      ],
    };
  },
  methods: {
    formatInterval(interval) {
      const hours = interval.hour.toString().padStart(2, '0');
      const minutes = interval.minute.toString().padStart(2, '0');
      return `${hours}:${minutes}`;
    },
    getEventColor(event) {
      return event.color || "primary";
    },
  },
};
</script>
<style scoped>
.custom-event{
  padding: 4px 8px 0 0 !important;
}
</style>
