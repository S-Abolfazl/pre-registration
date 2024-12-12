<template>
  <div class="w-max">

    <!-- First row bar -->
    <v-row no-gutters>
      <BaseButton
        text="ثبت نام کنم برات؟"
        width="16%"
        borderRadius="25px"
        @click="register()"
        textClass="mr-auto"
        non_box_shodow
        image="/image/pre-registration-form/Clip.png"
        imageStyle="height: 56px; width: 56px; margin-right: auto;"
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
        placeholder="دنبال چی هستی دوست عزیز؟"
        prependInnerIcon="mdi-magnify"
        width="23%"
        borderRadius="25px"
      />


    </v-row>
  </div>
</template>

<script>

export default {
  head() {
    return {
      title: 'فرم پیش ثبت نام',
    }
  },

  methods: {
    register() {
      console.log('رجیستر');
    },
    filter() {
      console.log('filter');
    },
  }
};
</script>
