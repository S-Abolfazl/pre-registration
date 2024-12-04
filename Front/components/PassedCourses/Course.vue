<template>
  <div>
    <v-chip
      :outlined="!isSelected"
      :color="isSelected ? 'purple' : 'white'"
      :dark="isSelected"
      :text-color="isSelected ? 'white' : 'purple'"
      @click="toggleSelection"
      class="outlined-chip "
    >
      {{ text }}
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
      default: "Course",
    },
  },
  data() {
    return {
      isSelected: false, // Track the selection state
    };
  },
  methods: {
    toggleSelection() {
      this.isSelected = !this.isSelected; // Toggle the selection state
    },
  },
};
</script>

<style scoped>
.outlined-chip {
  border-color: #6938EF !important; 
}
</style>
