<template>
  <div>
    <v-chip
      :outlined="!isSelected"
      :color="isSelected ? 'purple' : 'white'"
      :dark="isSelected"
      :text-color="isSelected ? 'white' : 'purple'"
      @click="toggleSelection"
      class="outlined-chip large-chip"
      
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
.large-chip {
  height: 30px; /* Example height for large size */
  font-size: 16px; /* Adjust font size */
  padding: 0 16px; /* Adjust padding */}

.outlined-chip {
  border-color: #6938EF !important; 
}
</style>
