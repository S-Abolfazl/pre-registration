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
              :class="[ 'custom-event', event.selected ? '' : 'primary--text', event.disabled ? 'd-none' : '' ]"
              @click.stop="openMenu($event, event)"
            >
              {{ event.name }}
              <br>
              <div class="d-flex justify-end ml-2">
                {{ event.end.slice(event.end.length - 5, event.end.length) }}
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

    <v-menu
      v-model="selectedOpen"
      :close-on-content-click="false"
      :activator="selectedElement"
      offset-x
    >
      <v-card color="grey lighten-4" min-width="350px" flat>
        <v-card-title>
          جزئیات درس

          <v-checkbox
            v-model="selectedEvent.selected"
            label="انتخاب"
            class="mr-auto"
          />
        </v-card-title>
        <v-card-text>
          <p><strong>نام درس : </strong> {{ selectedEvent?.name }}</p>
          <p><strong> شروع : </strong>
            {{ start_time(selectedEvent) }}
          </p>
          <p><strong>پایان : </strong>
            {{ end_time(selectedEvent) }}
          </p>
          <p><strong>نام استاد : </strong> {{ selectedEvent?.teacherName || '-'}}</p>
        </v-card-text>
        <v-card-actions>
          <v-btn text color="primary" @click="selectedOpen = false">بستن</v-btn>
        </v-card-actions>
      </v-card>
    </v-menu>
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
      selectedOpen: false,
      selectedEvent: {
        selected: false,
      },
      selectedElement: null,
    };
  },
  watch: {
    'Datas': {
      deep: true,
      handler(newValue) {
        if (newValue.length > 0){
          this.events = this.Datas.slice(0, 50);
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
      const selectedEvent = data.event;

      data.event.selected = !data.event.selected;

      this.events.forEach(event => {
        if (event != selectedEvent) {
          const overlap = this.checkOverlap(selectedEvent, event);
          event.disabled = selectedEvent.selected && overlap;
        }
      });
      console.log(this.events);

    },
    checkOverlap(event1, event2) {
      const start1 = new Date(event1.start).getTime();
      const end1 = new Date(event1.end).getTime();
      const start2 = new Date(event2.start).getTime();
      const end2 = new Date(event2.end).getTime();

      return (start1 < end2 && start2 < end1);
    },
    openMenu(event, eventData) {
      this.selectedEvent = eventData;
      this.selectedElement = event.currentTarget;
      this.selectedOpen = true;
    },
    start_time(data) {
      if ('start' in data)
        return data.start.slice(data.start.length - 5, data.start.length)
      },
    end_time(data) {
      if ('end' in data)
        return data.end.slice(data.end.length - 5, data.end.length)
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
