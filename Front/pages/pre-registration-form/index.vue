<template>
  <div class="w-max">

    <!-- First row bar -->
    <v-row no-gutters class="px-5 mt-12 mb-6">
      <BaseButton
        text="ثبت کنم برات؟"
        width="16%"
        borderRadius="25px"
        @click="register()"
        textClass="mr-auto"
        non_box_shodow
        image="/image/pre-registration-form/Clip.png"
        imageStyle="height: 56px; width: 56px; margin-right: auto;"
        class="ml-2"
      />

      <BaseButton
        text="فیلتر کنم برات؟"
        width="14%"
        borderRadius="25px"
        @click="filter()"
        icon="mdi-filter-outline"
        textClass="black1--text"
        iconColor="black1"
        class="mx-2"
        outlined
      />

      <BaseInput
        class="mr-auto"
        placeholder="دنبال چی هستی دوست عزیز؟"
        prependInnerIcon="mdi-magnify"
        width="23%"
        borderRadius="25px"
      />

      <!-- notif icon -->
      <div class="ml-7 mr-11">
        <v-icon class="font_45" @click="notif()" title="اطلاعات">
          mdi-alert-circle-outline
        </v-icon>
      </div>
    </v-row>

    <v-row no-gutters class="pl-10">
      <TimeTable />
    </v-row>

    <v-dialog
      v-model="dialog"
      width="70%"
    >
      <v-card width="100%" height="100%">
        داده الکی
      </v-card>
  </v-dialog>

  </div>
</template>

<script>
import TimeTable from "~/components/PreRegistrationForm/TimeTable.vue";
export default {
  head() {
    return {
      title: 'پیش ثبت نام',
    }
  },
  components: { TimeTable },
  data: () => ({
    dialog: false,
    search_data: '',
  }),
  mounted() {
    // API call for get courses

  },
  methods: {
    register() {
      console.log('رجیستر');
    },
    filter() {
      console.log('filter');
    },
    notif() {
      this.dialog = true;
    },
  }
};
</script>
