<template>
  <div class="d-flex" width="14%">
    <!-- Main Menu -->
    <v-menu
      v-model="menuVisible"
      :close-on-content-click="false"
      offset-y
    >
      <template #activator="{ attrs, on }">
        <v-btn
          outlined
          v-bind="attrs"
          v-on="on"
          width="100%"
          height="40px"
          class="mx-2 rounded-pill"
        >
          <b>
            فیلتر کنم برات؟
            <v-icon right>mdi-filter-outline</v-icon>
          </b>
        </v-btn>
      </template>

      <v-list>
        <v-list-item-group>
          <!-- نوع درس -->
          <v-list-item @click="openSubmenu($event)">
            <v-list-item-content>
              <v-list-item-title>نوع درس</v-list-item-title>
            </v-list-item-content>
            <v-list-item-icon>
              <v-icon>mdi-chevron-left</v-icon>
            </v-list-item-icon>
          </v-list-item>

          <!-- پیش نیازهای پاس شده -->
          <v-list-item>
            <v-list-item-content>
              <v-checkbox
                class="ma-0"
                v-model="includePrerequisites"
                label="پیش نیازهای پاس شده"
                hide-details
              ></v-checkbox>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-menu>

    <!-- Submenu -->
    <v-menu
      :activator="submenuActivator"
      offset-y
    >
      <v-list>
        <v-list-item-group>
          <v-list-item
            v-for="type in courseTypes"
            :key="type"
            @click="selectCourseType(type)"
          >
            <v-list-item-content>
              <v-list-item-title>{{ type }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-menu>
  </div>
</template>

<script>
export default {
  data() {
    return {
      menuVisible: false, // Main menu visibility
      includePrerequisites: false, // Checkbox state for prerequisites
      selectedCourseType: null, // Selected course type
      courseTypes: ["اختصاصي", "عمومي", "پايه", "عملی", "اختياري"], // Submenu items
      submenuActivator: null, // Dynamically set the activator for the submenu
    };
  },
  watch: {
    includePrerequisites(newVal) {
      if (newVal) {
        this.$emit('passed_courses')
      }
    },
  },
  methods: {
    openSubmenu(event) {
      this.submenuActivator = event.currentTarget; // Set the activator dynamically
    },
    selectCourseType(type) {
      this.selectedCourseType = type; // Store the selected course type
      this.menuVisible = true; // Reopen main menu
      this.$emit("course_type", type);
    },
  },
};
</script>

<style scoped>
.v-menu {
  max-width: 300px;
}
.v-list-item-group {
  padding: 0;
}
</style>
