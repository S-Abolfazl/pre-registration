<template>
    <div>
      <!-- Overlay -->
      <div class="overlay" v-if="showAddCourse" @click="closeModal"></div>
  
      <!-- Modal -->
      <div class="modal px-4 py-7 white1" v-if="showAddCourse">
        <v-form v-model="formValid">

          <!-- header -->
        
          <v-row class="mt-4">
            <h3 class="font_22 addCourse_header mx-5"> اطلاعات درس</h3>
          </v-row>
          <div class="gradient-divider my-4"></div>
          <v-col class="mx-4 my-6">
          <!-- Course and Teacher Name row -->
          <v-row>
            <v-col cols="6">
              <BaseInput
                v-model="newCourse.courseName"
                backgroundColor ="blue3"
                textClass="font_20 black1--text"
                text="نام درس"
                rules="require"
                borderRadius="15px"
                width="70%" 
                placeholder="نام درس را وارد کنید"
              />
            </v-col>
            <v-col cols="6">
              <BaseInput
                v-model="newCourse.teacherName"
                backgroundColor ="blue3"
                textClass="font_20 black1--text"
                text="نام استاد"
                rules="require"
                width="70%" 
                borderRadius="15px"
                placeholder="نام استاد را وارد کنید"
              />
            </v-col>
          </v-row >

          <!-- Capasity and entry years row -->
          <v-row class="d-flex align-center">
            <v-col cols="5">
              <BaseInput
                v-model="newCourse.capacity"
                backgroundColor ="blue3"
                textClass="font_20 black1--text"
                text="ظرفیت درس"
                rules="require"
                width="70%" 
                borderRadius="15px"
                type="number"
                placeholder="ظرفیت درس را وارد کنید"
              />
            </v-col>
            
            <v-col cols="7">
              <v-row>
                <div class="black1--text mx-4 font_20">ورودی</div>
              </v-row>
              <v-row>
                <v-col cols="12"  class="d-flex align-center">
                  <v-chip
                  v-for="year in availableYears"
                  :key="year"
                  :color="isSelectedYear(year) ? 'blue2' : 'blue2'"
                  :outlined="!isSelectedYear(year)"
                  class="mx-2"
                  text-color="black1"
                  style="font-weight: bold;"
                  @click="toggleYear(year)"
                  >
                  {{ year }}
                  </v-chip>
                </v-col>
              </v-row> 
            </v-col>
          </v-row>  
          <v-row>
            <v-checkbox
            v-model="newCourse.is_Experimental"
            :label="'درس آزمایشی است.'"
            color="blue2"
            hide-details
            class="font_20 mx-4 py-0"
            input-value="newCourse.is_Experimental"
            />
          </v-row>
        </v-col>

          <v-row class="mt-6">
            <h3 class="font_22 addCourse_header mx-5"> روز و ساعت ارائه</h3>
          </v-row>
          <div class="gradient-divider my-4"></div>
         
            <v-col class="mx-4 my-4">
              <v-row class="mt-4">
                <div class="black1--text mx-4 font_20">روزهای ارائه درس</div>
              </v-row>
              <v-row>
                <v-col  class="d-flex align-center">
                  <v-chip
                    v-for="day in availableDays"
                    :key="day"
                    :color="isSelectedDay(day) ? 'blue2' : 'blue2'"
                    :outlined="!isSelectedDay(day)"
                    class="mx-2 chip-custom"
                    text-color="black1"
                    style="font-weight: bold;"
                    @click="toggleDay(day)"
                  >
                    {{ day }}
                  </v-chip>
                </v-col> 
              </v-row>

              <v-row class="d-flex align-center mt-6">
                <v-col cols="2">
                  <BaseInput
                    v-model="newCourse.class_start_time"
                    backgroundColor ="blue3"
                    textClass="font_20 black1--text"
                    text="شروع"
                    rules="require"
                    width="100%" 
                    borderRadius="15px"
                    type="time"
                    placeholder="ساعت شروع"
                  />
                </v-col>
               
                <div class="mt-5 font_20" style="color: rgb(0, 0, 0,0.4);">تا</div>
                
                <v-col cols="2" >
                  <BaseInput
                    v-model="newCourse.class_end_time"
                    backgroundColor ="blue3"
                    textClass="font_20 black1--text"
                    rules="require"
                    text="ساعت پایان"
                    width="100%" 
                    borderRadius="15px"
                    type="time"
                  />
                </v-col>
              </v-row>
            </v-col>

            <v-row>
              <h3 class="font_22 addCourse_header mx-5"> تاریخ و ساعت امتحان</h3>
            </v-row>
            <div class="gradient-divider my-4"></div>
            <v-col>
              <v-col>
                <v-row>
                  <div class="black1--text mx-4 font_20"> تاریخ امتحان</div>
                </v-row>
                <v-row >
                <BaseJdate
                  v-model="newCourse.exam_date"
                  backgroundColor ="blue3" 
                ></BaseJdate>
              </v-row>
              </v-col>

              <v-row class="mt-4 d-flex align-center">
                <v-col cols="2">
                  <BaseInput
                    v-model="newCourse.exam_start_time"
                    backgroundColor ="blue3"
                    textClass="font_20 black1--text"
                    text="ساعت شروع"
                    width="100%" 
                    borderRadius="15px"
                    type="time"
                  />
                </v-col>

                <div class="mt-5 font_20" style="color: rgb(0, 0, 0,0.4);">تا</div>
                
                <v-col cols="2" >
                  <BaseInput
                    v-model="newCourse.exam_end_time"
                    backgroundColor ="blue3"
                    width="100%" 
                    textClass="font_20 black1--text"
                    text="ساعت پایان"
                    borderRadius="15px"
                    type="time"
                  />
                </v-col>
              </v-row>
            </v-col>
  
          <!-- Description -->
          <v-row class="mt-3" >
            <h3 class="font_22 addCourse_header mx-5">توضیحات</h3>
          </v-row>
          <div class="gradient-divider my-4"></div>
          <v-col class="mx-4">
            <v-row class="mt-4">
              <h3 class="font_20 ">توضیحات</h3>
            </v-row>
            <v-row class="addCourse_textarea ">
              <v-textarea
                v-model="newCourse.description"
                outlined
                label="توضیحات"
                backgroundColor ="blue3"
                textClass="font_20 black1--text"
              >
              </v-textarea>
            </v-row>
          </v-col>
  
          <!-- Buttons -->
          <v-row class="justify-start mt-6 mx-4">
            <v-col cols="3">
              <BaseButton
                text="اضافه کردن درس"
                color="blue2"
                textClass="white1--text"
                class="font_22"
                @click="addCourse"
                borderRadius="15px"

              />
            </v-col>
            <v-col cols="3">
              <BaseButton
                text="خروج"
                outlined
                color="blue2"
                class="font_22"
                textClass="blue2--text"
                @click="closeModal"
                borderRadius="15px"
              />
            </v-col>
          </v-row>
        </v-form>
      </div>
    </div>
  </template>
  
  <script>
import BaseCard from '../Base/BaseCard.vue';
import BaseDatePicker from '../Base/BaseDatePicker.vue';
import BaseInput from '../Base/BaseInput.vue';
import BaseJdate from '../Base/BaseJdate.vue';
import BaseLable from '../Base/BaseLable.vue';
import BaseSelect from '../Base/BaseSelect.vue';
import BaseTextarea from '../Base/BaseTextarea.vue';
import BaseTitle from '../Base/BaseTitle.vue';

  export default {
    props: {
      showAddCourse: {
        type: Boolean,
        required: true,
      },
    },
    data() {
      return {
        // showAddCourse: false,
        formValid: false,
        newCourse: {
          courseName: "",
          teacherName: "",
          capacity: null,
          unit: null,
          entry_years: [],
          is_Experimental:false,
          class_days: [],
          class_start_time: "",
          class_end_time: "",
          exam_date: "",
          exam_start_time: "",
          exam_end_time: "",
          description: "",
        },
        availableYears: [1399, 1400, 1401, 1402], 
        availableDays: ["شنبه", "یکشنبه", "دوشنبه", "سه شنبه", "چهارشنبه"],
      };
    },

    methods: {
      toggleYear(year) {
        const index = this.newCourse.entry_years.indexOf(year);
        if (index === -1) {
          this.newCourse.entry_years.push(year);
        } else {
          this.newCourse.entry_years.splice(index, 1);
        }
      },
      isSelectedYear(year) {
        return this.newCourse.entry_years.includes(year);
      },

      toggleDay(day) {
        const index = this.newCourse.class_days.indexOf(day);
        if (index === -1) {
          if (this.newCourse.class_days.length < 2) {
            this.newCourse.class_days.push(day);
          }
        } else {
          this.newCourse.class_days.splice(index, 1);
        }
      },
      isSelectedDay(day) {
        return this.newCourse.class_days.includes(day);
      },
      
      processCourseData(course) {
        const processedCourse = { ...course };

        // Format times
        processedCourse.class_start_time = this.formatTime(course.class_start_time);
        processedCourse.class_end_time = this.formatTime(course.class_end_time);
        processedCourse.exam_start_time = this.formatTime(course.exam_start_time);
        processedCourse.exam_end_time = this.formatTime(course.exam_end_time);

        // Split class_days into two variables
        const days = course.class_days;
        processedCourse.class_time1 = days[0] || null;
        processedCourse.class_time2 = days[1] || days[0] || null;

        // Remove original class_days array
        delete processedCourse.class_days;

        return processedCourse;
      },

      addCourse() {
        if (this.formValid) {
        
          const processedCourse = this.processCourseData(this.newCourse);

          this.$emit("course-added", processedCourse);
  
          this.newCourse = {
            courseName: "",
            teacherName: "",
            capacity: null,
            unit: null,
            entry_years: [],
            is_Experimental:false,
            class_days: [],
            class_start_time: "",
            class_end_time: "",
            exam_date: "",
            exam_start_time: "",
            exam_end_time: "",
            description: "",
          };
          this.closeModal();
        }
      },
      closeModal() {
        this.$emit("close-modal"); 
      },
    },
  };
  </script>
  
  <style scoped>
  .overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    z-index: 1000;
  }
  
  .modal {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width:65%;
    /* background: white; */
    border-radius: 20px;
    /* padding: 20px; */
    z-index: 1100;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
    max-height: 90%; /* ارتفاع حداکثر */
    overflow-y: auto;
  }
  .addCourse_textarea{
    width: 40%;
  }
  .addCourse_header {
    color: rgba(0, 0, 0, 0.48);
  }
  
  .gradient-divider {
  height: 3px; 
  background: linear-gradient(to right, #FF8B37, #7B5FF1); 
  border: none; 
  }

  /*.custom-checkbox .v-input__control {
  border-radius: 50%; /* دایره‌ای کردن 
  border: 2px solid #1e88e5; /* رنگ دور چک‌باکس 
  width: 24px; /* اندازه عرض 
  height: 24px; /* اندازه ارتفاع 
  }
  .custom-checkbox input:checked + .v-input__control {
  background-color: #1e88e5; /* رنگ داخل چک‌باکس 
  border-color: #1565c0; /* تغییر رنگ خط دور 
  }

  /* تغییر رنگ متن کنار چک‌باکس 
  .custom-checkbox .v-label {
    color: #424242; 
  }*/

  </style>
  