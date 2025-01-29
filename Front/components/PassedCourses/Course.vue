<template>
  <div>
    <v-chip
      :outlined="!isSelected"
      :color="isSelected ? 'blue2' : 'white'"
      :dark="isSelected"
      :text-color="isSelected ? 'white' : 'blue2'"
      @click="toggleSelection"
      @mouseover="func()"
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
          style="margin-left: 4%;"
        >
          mdi-chevron-right
        </v-icon>
        <span style="flex-grow: 1; text-align: center;">{{ currentText }}</span>
        <v-icon
          v-if="expanded"
          @click.stop="nextItem"
          class="arrow-icon"
          style="margin-right: 4%;"
        >
          mdi-chevron-left
        </v-icon>
        <v-icon
          v-if="!expanded && course.courseName === 'اختیاری' && showControls"
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
    course: {
      type: Object,
    },
    options: {
      type: Array,
      required: false,
    },
  },
  data() {
    return {
      isSelected: false, // Track the selection state
      showControls: false, // Show/hide the controls on hover
      expanded: false, // Track if the chip is expanded
      currentText: "اختیاری", // Current text displayed on the chip
      selectedText: "اختیاری", // Selected text when returning to normal
      currentIndex: 0, // Index of the current option
    };
  },
  methods: {
    toggleSelection() {
      this.isSelected = !this.isSelected;
      this.expanded = !this.expanded; // Expand the chip when selected
      this.options[this.currentIndex].passed = !this.options[this.currentIndex].passed;
    },
    resetChip() {
      this.expanded = false; // Collapse the chip
      this.showControls=false;
      this.currentText = this.selectedText; // Reset to selected text
    },
    prevItem() {
      console.log('asd2', typeof(this.options));
      if (this.options.length > 0) {
        this.currentIndex =
          (this.currentIndex - 1 + this.options.length) % this.options.length;
        this.currentText = this.options[this.currentIndex].courseName;
        this.selectedText = this.currentText; // Update selected text
      }
    },
    nextItem() {
      if (this.options.length > 0) {
        this.currentIndex = (this.currentIndex + 1) % this.options.length;
        this.currentText = this.options[this.currentIndex].courseName;
        this.selectedText = this.currentText; // Update selected text
      }
    },
    func() {
      this.showControls = true;
      this.$emit('selectedCourse', this.options[this.currentIndex]);
    }
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
