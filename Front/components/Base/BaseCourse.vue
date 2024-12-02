<template>
  <div class="chip-container">
    <!-- Outlined Chip -->
    <v-chip
      :outlined="isOutlined"
      :color="chipColor"
      class="mx-2"
    >
      {{ outlinedText }}
    </v-chip>

    <!-- Filled Chip -->
    <v-chip
      :color="chipColor"
      :dark="!isOutlined"
      class="mx-2"
    >
      {{ filledText }}
    </v-chip>
  </div>
</template>

<script>
export default {
  name: " BaseCourse",
  props: {
    outlinedText: {
      type: String,
      required: true,
      default: "Outlined Chip",
    },
    filledText: {
      type: String,
      required: true,
      default: "Filled Chip",
    },
    chipColor: {
      type: String,
      required: true,
      default: "purple",
    },
    isOutlined: {
      type: Boolean,
      default: true,
    },
  },
};
</script>

<style scoped>
.chip-container {
  display: flex;
  justify-content: start;
  align-items: center;
}
</style>
