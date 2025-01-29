<template>
    <div class="slide-group-wrapper" >
      <!-- Slide Group Container -->
      <v-slide-group
        v-model="selected"
        class="custom-slide-group"
        center-active
        show-arrows
        :style="{ height: height }"
      >
        <!-- Left Arrow -->
        <template v-slot:prev>
          <v-btn icon @click="prevYear" :disabled="isFirst">
            <v-icon>mdi-chevron-right</v-icon>
          </v-btn>
        </template>

        <!-- Slide Items -->
        <v-slide-item
          v-for="(year, index) in years"
          :key="year"
          :value="year"
          class="slide-item"
        >
          <div class="entry-content">{{ year }}</div>
        </v-slide-item>

        <!-- Right Arrow -->
        <template v-slot:next>
          <v-btn icon @click="nextYear" :disabled="isLast">
            <v-icon>mdi-chevron-left</v-icon>
          </v-btn>
        </template>
      </v-slide-group>
    </div>
  </template>

  <script>
  export default {
    name:"YearSelection",
    props: {
      width: {
        type: String,
        default: '400px',
      },
      height: {
        type: String,
        default: '10px',
      },
    },
    data() {
      return {
        selected: 1400, // Default selected year
        years: Array.from({ length: 6 }, (_, i) => 1403 - i), // Generate years from 1300 to 1399
      };
    },
    computed: {
      isFirst() {
        return this.selected === this.years[0];
      },
      isLast() {
        return this.selected === this.years[this.years.length - 1];
      },
    },
    methods: {
      prevYear() {
        const currentIndex = this.years.indexOf(this.selected);
        if (currentIndex > 0) {
          this.selected = this.years[currentIndex - 1];
        }
      },
      nextYear() {
        const currentIndex = this.years.indexOf(this.selected);
        if (currentIndex < this.years.length - 1) {
          this.selected = this.years[currentIndex + 1];
        }
      },
    },
  };
  </script>

  <style scoped>
  /* Wrapper for alignment */
  .slide-group-wrapper {
    justify-content: center;
    align-items: center;
  }

  /* Slide Group Container */
  .custom-slide-group {
    width: v-bind('width');
    background-color: #FF8B37; /* Orange background */
    border-radius: 50px; /* Fully rounded container */
    position: relative;
    align-items: center;
  }

  /* Each Slide Item */
  .slide-item {
    justify-content: center !important;
    align-items: center !important;
    width: v-bind('width') !important;
  }

  .entry-content {
    font-size: 16px;
    font-weight: bold;
    color: white;
    text-align: center;
    align-items: center;
  }

  /* Arrow Button Styling */
  .v-btn {
    color: white;
  }

  .v-icon {
    font-size: 24px;
  }

  .v-btn[disabled] {
    color: gray;
    cursor: not-allowed;
  }
  </style>
