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
      start="2024-12-3T10:00:00"
      :weekdays="[6, 0, 1, 2, 3]"
      :events="filterDates(courses[0])"
      event-color="getEventColor"
      locale="fa"
      :first-interval="6"
      :interval-count="14"
      :interval-minutes="60"
      interval-height="50"
      show-interval-label
      color="primary"
      :interval-format="formatInterval"
    >
      <template #event="{ event }">
        <v-tooltip bottom>
          <template #activator="{ on, attrs }">
            <div v-bind="attrs" v-on="on" class="custom-event">
              {{ event.course.courseName }}
              <br>
              <div class="d-flex justify-end ml-2">
                {{ event.class_start_time.substr(event.class_start_time.length - 5, event.class_start_time.length) }}
                -
                {{ event.class_end_time.substr(event.class_end_time.length - 5, event.class_end_time.length) }}
              </div>
            </div>
          </template>
          <div>
            {{ event.course.courseName }}
          </div>
        </v-tooltip>
      </template>
    </v-calendar>
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
    filterDates(data) {
      switch (data.class_time1) {
        case "شنبه":
          data.class_start_time = `2024-11-30T${data.class_start_time}`;
          data.class_end_time = `2024-11-30T${data.class_end_time}`;
          break;
        case "یک‌شنبه":
          data.class_start_time = `2024-12-01T${data.class_start_time}`;
          data.class_end_time = `2024-12-01T${data.class_end_time}`;
          break;
        case "دوشنبه":
          data.class_start_time = `2024-12-02T${data.class_start_time}`;
          data.class_end_time = `2024-12-02T${data.class_end_time}`;
          break;
        case "سه‌شنبه":
          data.class_start_time = `2024-12-03T${data.class_start_time}`;
          data.class_end_time = `2024-12-03T${data.class_end_time}`;
          break;
        case "چهارشنبه":
          data.class_start_time = `2024-12-04T${data.class_start_time}`;
          data.class_end_time = `2024-12-04T${data.class_end_time}`;
          break;
        default:
          break;
      }
      console.log(data);
      return data
    },
  },
};
</script>
<style scoped>
.custom-event{
  padding: 4px 8px 0 0 !important;
}
</style>
