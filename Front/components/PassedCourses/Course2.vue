<template>
  <div>
    <v-chip
      :outlined="!course.passed"
      :color="course.passed ? 'purple' : 'white'"
      :dark="course.passed"
      :text-color="course.passed ? 'white' : 'purple'"
      @click="toggleSelection(course)"
      class="outlined-chip large-chip"
    >
      {{ course.courseName }}
    </v-chip>
  </div>
</template>

<script>
export default {
  name: "Course",
  props: {
    course: {
      type: Object,
      required: true,
    },
  },
  methods: {
    toggleSelection(data) {
      data.passed = !data.passed;
    }
  }
};
</script>

<style scoped>
.large-chip {
  height: 30px; /* Example height for large size */
  font-size: 16px; /* Adjust font size */
  padding: 0 16px; /* Adjust padding */}

.outlined-chip {
  border-color: #6938EF !important;
}
</style>
