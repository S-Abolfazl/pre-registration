<template>
  <v-card class="course-detail-card">
    <v-card-text>
      <h3 class="course-title">{{ course.title }}</h3>
      <div class="card-header">
        <span class="day">{{ course.day }}</span>
        <strong class="time">{{ course.time }}</strong>
      </div>
      <p class="instructor">{{ course.instructor }}</p>
      <div class="stats">
        <span class="registration-status" :class="registrationStatusClass">{{ registrationStatus }}</span>
        <div class="capacity">{{ course.registered }} / {{ course.capacity }} ظرفیت</div>
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  props: {
    course: {
      type: Object,
      required: true,
    },
  },
  computed: {
    registrationStatus() {
      const difference = this.course.capacity - this.course.registered;
      return difference < 0 ? `🔴 ${Math.abs(difference)}` : `🟢 ${difference}`;
    },
    registrationStatusClass() {
      return {
        'status-full': this.course.registered >= this.course.capacity,
        'status-open': this.course.registered < this.course.capacity,
      };
    },
  },
};
</script>

<style scoped>
.course-detail-card {
  border-radius: 8px;
  padding: 16px;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin: 10px;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.day {
  font-weight: bold;
  color: #333;
}

.time {
  font-size: 14px;
  color: #666;
}

.course-title {
  margin: 10px 0;
  font-size: 18px;
  color: #333;
}

.instructor {
  font-size: 14px;
  color: #666;
}

.stats {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.registration-status {
  font-weight: bold;
}

.capacity {
  font-size: 14px;
  color: #666;
}

.status-full {
  color: red;
}

.status-open {
  color: green;
}
</style>
