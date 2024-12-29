<template>
  <div>
    <v-tooltip bottom>
      <template v-slot:activator="{ on, attrs }">
        <v-chip
          v-bind="attrs"
          v-on="on"
          :color="computedColor"
          :class="['custom-chip', $store.state.static.course_type[kind] == 'اختياري' ? 'gradient-chip' : '']"
          :outlined="computedBorder"
        >
          <span :class="['font_16', computedBorder ? 'blue2--text' : 'white1--text']" v-html="courseName"> </span>
          <v-chip
            :color="computedBorder ? 'blue2' : 'white1'"
            class="inner-circle"
          >
            <div :class="['font_12', `${computedBorder ? 'white1' : computedColor}--text`, 'pa-n3']">
              {{ unit }}
            </div>
          </v-chip>
        </v-chip>
      </template>
      <span>
        <strong>هم نیاز ها : </strong>
        {{ formattedCourseName(coreq) }}
        <br>
        <strong>پیش نیاز ها : </strong>
        {{ formattedCourseName(prereq) }}
      </span>
    </v-tooltip>
  </div>
</template>

<script>
export default {
  name: "Courses",
  props: {
    coreq: {
      type: Array,
    },
    prereq: {
      type: Array,
    },
    courseName: {
      type: String,
      required: true,
    },
    unit: {
      type: [String, Number],
      required: true,
      default: 0,
    },
    kind: {
      type: String,
      required: true,
    },
  },
  computed: {
    computedColor() {
      switch (this.$store.state.static.course_type[this.kind]) {
        case "اختصاصي":
          return "blue2";
        case "پايه":
          return "orange1";
        case "عمومي":
          return "white1";
        case "اختياري":
          return ""; // Color handled by gradient-chip class
        default:
          return "blue2";
      }
    },
    computedBorder() {
      return this.$store.state.static.course_type[this.kind] === "عمومي";
    },
  },
  methods: {
    formattedCourseName(data) {
      return data.join(', ');
    },
  }
};
</script>

<style scoped>
.custom-chip {
  display: flex;
  justify-content: center;
  align-items: center;
  padding-left: 2rem;
  padding-right: 2rem;
  border-radius: 50px;
  font-weight: bold;
  width: fit-content;
  height: 2.5vw !important;
  margin: 1vw;
  border-color: #ccc;
  border-style: solid;
  border-width: 2px;
}
.text {
  color: white1;
}

.inner-circle {
  margin: 0px 6px 0 6px !important;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 50%;
  width: 2.3vw; /* Ensure equal width and height */
  height: 1w;
  text-align: center;
  box-sizing: border-box; /* Prevent padding/margin issues */
  color: #7b5ff1 !important;
}
.v-chip.v-chip--outlined.v-chip.v-chip {
  border: 1px solid #7b5ff1 !important;
}
.v-chip .inner-circle {
  padding: 0 !important;
}
.gradient-chip {
  background: linear-gradient(0deg, #ff8b37, #7b5ff1) !important;
  color: white !important;
  border: none;
}
</style>
