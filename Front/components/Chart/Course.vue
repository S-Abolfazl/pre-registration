<template>
  <div>
    <v-chip
      :outlined="isOutlined()"
      :color="theColor()"
      :class="['custom-chip', Course.type == 'اختياري' ? 'gradient-chip' : '']"
    >
      <span :class="[ 'font_16', isOutlined() ? 'blue2--text' : 'white1--text']" v-html="Course.name"> </span>
      <v-chip
        :color="border ? color : 'white1'"
        class="inner-circle"
      >
        <div :class="['font_12', `${border ? 'white1' : color}--text`, 'pa-n3']" :color="border ? 'white1' : color">
          {{ number }}
        </div>
      </v-chip>
      <span :class="[ 'font_16', border ? 'blue2--text' : 'white1--text']"> واحد </span>
    </v-chip>
  </div>
</template>

<script>

export default {
  props: {
    Course: {
      type: Object,
      required: true,
      default: () => {},
    },
  },
  methods: {
    isOutlined() {
      if (this.Course.type == "پایه")
        return true;
      return false;
    },
    theColor() {
      if (this.Course.type == "تخصصی")
        return blue1;
      else if (this.Course.type == "پایه")
        return orange1;
    }
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
}
.v-chip.v-chip--outlined.v-chip.v-chip{
  border: 1px solid #7b5ff1 !important;
}
.v-chip .inner-circle{
  padding: 0 !important;
}
.gradient-chip {
  background: linear-gradient(0deg, #ff8b37 , #7b5ff1) !important;
  color: white !important;
  border: none;
}
</style>
