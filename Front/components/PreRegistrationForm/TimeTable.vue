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
      <v-card min-width="10%" flat color="gray4" elevation="0" class="card">
        <v-card-title class="pa-2">
          <b class="font_19 pr-4">
            جزئیات درس
          </b>
        </v-card-title>

        <hr
          style="border: 1px solid gray; margin: 0 50px; border-radius: 99px;"
        />

        <v-card-text>
          <p class="font_16">{{ selectedEvent?.name }}</p>
          <p class="font_16">استاد {{ selectedEvent?.teacherName }}</p>
          <p class="font_16">{{ end_time(selectedEvent) }} - {{ start_time(selectedEvent) }}</p>
        </v-card-text>
        <v-card-actions class="justify-center">
          <BaseButton
            color="primary"
            :outlined="!selectedEvent?.selected"
            @click="select2(selectedEvent)"
            text="انتخاب"
            textClass="font_18"
            width="80%"
            height="33px"
            borderRadius="99px"
          />
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
        this.events = this.Datas;
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
      this.selectedOpen = !this.selectedOpen;
    },
    start_time(data) {
      if ('start' in data)
        return data.start.slice(data.start.length - 5, data.start.length)
    },
    end_time(data) {
      if ('end' in data)
        return data.end.slice(data.end.length - 5, data.end.length)
    },
    select2(event) {
      if ('selected' in event) {
        event.selected = !event.selected;
        this.events.forEach(the_event => {
          if (event.name == the_event.name && event.end != the_event.end) {
            the_event.selected = !the_event.selected;
          }
        });
      }
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
.v-menu__content {
  box-shadow: none !important;
  border: 2px solid #7B5FF1 !important;
  border-radius: 33px;
}
.custom-chip {
  width: 80% !important; /* Set width to 80% */
}
</style>
