<template>
  <div>
    <v-chip
      :color="computedColor"
      :class="['custom-chip', kind === 'اختياري' ? 'gradient-chip' : '']"
      :outlined="computedBorder"
    >
      <span :class="['font_16', computedBorder ? 'blue2--text' : 'white1--text']" v-html="text"> </span>
      <v-chip
        :color="computedBorder ? 'blue2' : 'white1'"
        class="inner-circle"
      >
        <div :class="['font_12', `${computedBorder ? 'white1' : computedColor}--text`, 'pa-n3']" >
          {{ number }}
        </div>
      </v-chip>
    </v-chip>
  </div>
</template>

<script>
export default {
  name: "Course",
  props: {
    text: {
      type: String,
      required: true,
    },
    number: {
      type: [String, Number],
      required: true,
      default: 0,
    },
    kind: {
      type: String,
      required: true,
      validator: (value) => ["اختياري", "اختصاصي", "عمومي", "پايه"].includes(value),
    },
  },
  computed: {
    computedColor() {
      switch (this.kind) {
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
      return this.kind === "عمومي";
    },
  },
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