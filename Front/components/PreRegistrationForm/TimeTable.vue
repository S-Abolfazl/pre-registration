<template>
  <div class="mx-0 mb-5 w-max2">
    <!--
      6 : شنبه
      0 : یکشنبه
      1 : دوشنبه
      2 : سه شنبه
      3 : چهارشنبه
      4 : پنج‌شنبه
    -->

    <v-calendar
      ref="calendar"
      type="week"
      start="2024-12-3"
      :events="events"
      :weekdays="[6, 0, 1, 2, 3, 4]"
      :event-color="getEventColor"
      locale="fa"
      :first-interval="7"
      :interval-count="14"
      :interval-minutes="60"
      interval-height="60"
      show-interval-label
      :interval-format="formatInterval"
      @click:event="select"
    >
      <template #event="{ event }">
        <v-tooltip bottom>
          <template #activator="{ on, attrs }">
            <div
              v-bind="attrs"
              v-on="on"
              :class="['custom-event', event.selected ? '' : 'primary--text']"
            >
              {{ event.name }}
              <br>
              <div class="d-flex justify-end ml-2">
                {{ event.end.slice(event.end.length  - 5, event.end.length) }}
                  -
                {{ event.start.slice(event.start.length - 5, event.start.length) }}
              </div>
            </div>
          </template>
          <div >
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
  </div>
</template>

<script>

export default {
  props: {
    Datas: {
      type: Array,
      default: () => [],
      required: true,
    }
  },
  data() {
    return {
      events: [],
    };
  },
  watch: {
    'Datas': {
      deep: true,
      handler(newValue) {
        if (newValue.length > 0){
          this.events = this.Datas.slice(0, 50);
          // console.log(this.events);

          // this.events = [this.Datas[9]];
        }
      },
    },
  },
  methods: {
    formatInterval(interval) {
      const hours = interval.hour.toString().padStart(2, '0');
      const minutes = interval.minute.toString().padStart(2, '0');
      return `${hours}:${minutes}`;
    },
    getEventColor(event) {
      if (event.selected)
        return "primary";
      return "white1";
    },
    select(data) {
      console.log(data.event);

      data.event.selected = !data.event.selected;
    },
  },
};
</script>
<style scoped>
.custom-event{
  border-radius: 4px;
  padding: 9px 14px 0px 9px !important;
  height: 100%;
  border: 2px solid #7B5FF1 !important;
  overflow: hidden;
}
.w-max2 {
  width: 100%;
  overflow-x: scroll;
}
</style>
