<template>
  <div>
    <v-chip
      :outlined="!isSelected"
      :color="isSelected ? 'blue2' : 'white'"
      :dark="isSelected"
      :text-color="isSelected ? 'white' : 'blue2'"
      @click="toggleSelection"
      @mouseover="showControls = true"
      @mouseleave="resetChip"
      class="outlined-chip large-chip"
      :style="{ width: expanded ? '200px' : auto }"
    >
      <div
        style="display: flex; align-items: center; justify-content: space-between; width: 100%;"
      >
        <v-icon
          v-if="expanded"
          @click.stop="prevItem"
          class="arrow-icon"
          style="margin-left: 40px;"
        >
          mdi-chevron-right
        </v-icon>
        <span style="flex-grow: 1; text-align: center;">{{ currentText }}</span>
        <v-icon
          v-if="expanded"
          @click.stop="nextItem"
          class="arrow-icon"
          style="margin-right: 40px;"
        >
          mdi-chevron-left
        </v-icon>
        <v-icon
          v-if="!expanded && text === 'اختیاری' && showControls"
          class="plus-icon"
          style="margin-right: 8px;"
        >
          mdi-plus-thick
        </v-icon>
      </div>
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
    options: {
      type: Array,
      required: false,
      default: () => ["Option 1", "Option 2", "Option 3"], // Example options
    },
  },
  data() {
    return {
      isSelected: false, // Track the selection state
      showControls: false, // Show/hide the controls on hover
      expanded: false, // Track if the chip is expanded
      currentText: "", // Current text displayed on the chip
      selectedText: "", // Selected text when returning to normal
      currentIndex: 0, // Index of the current option
    };
  },
  mounted() {
    this.currentText = this.text; // Initialize the chip with the default text
    this.selectedText = this.text;
  },
  methods: {
    toggleSelection() {
      this.isSelected = !this.isSelected;
      this.expanded = !this.expanded; // Expand the chip when selected
    },
    resetChip() {
      this.expanded = false; // Collapse the chip
      this.showControls=false;
      this.currentText = this.selectedText; // Reset to selected text
    },
    prevItem() {
      if (this.options.length > 0) {
        this.currentIndex =
          (this.currentIndex - 1 + this.options.length) % this.options.length;
        this.currentText = this.options[this.currentIndex];
        this.selectedText = this.currentText; // Update selected text
      }
    },
    nextItem() {
      if (this.options.length > 0) {
        this.currentIndex = (this.currentIndex + 1) % this.options.length;
        this.currentText = this.options[this.currentIndex];
        this.selectedText = this.currentText; // Update selected text
      }
    },
  },
};
</script>

<style scoped>
.large-chip {
  height: 30px; /* Example height for large size */
  font-size: 16px; /* Adjust font size */
  padding: 0 16px; /* Adjust padding */
  display: flex;
  align-items: center;
  justify-content: center;
  transition: width 0.3s ease; /* Smooth width transition */
}

.outlined-chip {
  border-color: #6938ef !important;
}



.arrow-icon {
  cursor: pointer;
  color: #6938ef;
}


</style>
