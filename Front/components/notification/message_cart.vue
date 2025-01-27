<template>
    <v-row class="mx-6">
      <v-col
        v-for="(announcement, index) in sortedAnnouncements"
        :key="index"
        cols="12"
      >
        <v-card :color="cardColor " class="mb-2" outlined :style="{ borderRadius: borderRadius + 'px' }">
          <v-card-title :class="textColor" class="mx-6 my-3 font_35 bold">{{ announcement.title }}</v-card-title>
          <v-card-subtitle class="mx-6">
            {{ formatDate(announcement.created_at) }}
          </v-card-subtitle>
          <v-card-text class="mx-6 mb-3 font_24" :class="textColor">
            {{ announcement.content }}
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
</template>
<script>
export default {
  props: {
    announcements: {
      type: Array,
      required: true,
    },
    cardColor: {
      type: String,
      default: "lightblue",
    },
    textColor: {
      type: String,
      default: "black", // رنگ پیش‌فرض متن
    },
    borderRadius: {
      type: Number,
      default: 12, // گوشه‌های کارت به صورت پیش‌فرض گرد
    },
  },
  computed: {
    sortedAnnouncements() {
      return [...this.announcements].sort(
        (a, b) => new Date(b.created_at) - new Date(a.created_at)
      );
    },
  },
  methods: {
    formatDate(date) {
      const options = { year: "numeric", month: "long", day: "numeric" };
      return new Date(date).toLocaleDateString("fa-IR", options);
    },
  },
};
</script>

