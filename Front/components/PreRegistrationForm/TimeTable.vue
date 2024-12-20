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
      start="2024-12-3"
      :events="events"
      :weekdays="[6, 0, 1, 2, 3]"
      :event-color="getEventColor"
      locale="fa"
      :first-interval="6"
      :interval-count="14"
      :interval-minutes="60"
      interval-height="45"
      show-interval-label
      :color="getEventColor"
      :interval-format="formatInterval"
      category-show-all
    >
      <template #event="{ event }">
        <v-tooltip bottom color="orange1">
          <template #activator="{ on, attrs }">
            <div v-bind="attrs" v-on="on" class="custom-event">
              {{ event.name }}
              <br>
              <div class="d-flex justify-end ml-2">
                {{ event.end.slice(event.end.length  - 5, event.end.length) }}
                  -
                {{ event.start.slice(event.start.length - 5, event.start.length) }}
              </div>
            </div>
          </template>
          <div>
            تاریخ امتحان :
            <span dir="ltr">
              {{ event.exam_date ? `  ${event.exam_start_time} - ${event.exam_end_time} , ${event.exam_date}` : "" }}
            </span>
            <br>
            <span>
              نام استاد :
              {{ event.teacherName }}
            </span>
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
      events: [
      {
        name: "یادگیری ماشین",
        start: "2024-12-3 07:30",
        end: "2024-12-3 09:00",
        exam_date: "1403-10-24",
        exam_start_time: "09:00",
        exam_end_time: "12:00",
        teacherName: "حامد ملک",
        selected: false,
      },
      {
        name: "Workout",
        start: "2024-12-21 18:00",
        end: "2024-12-21 19:00",
        selected: false,
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
  },
};
</script>
<style scoped>
.custom-event{
  padding: 9px 14px 0px 9px !important;
}
</style>
