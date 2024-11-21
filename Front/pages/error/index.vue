<template>
  <v-col class="w-max h-max pa-0">
    <v-row no-gutters class="d-flex flex-column justify-center align-center w-max">
      <img src="/image/error/404.png" alt="png" width="40%">
      <b class="font_30 mt-15">
        متاسفانه صفحه مورد نظر یافت نشد
      </b>
    </v-row>
  </v-col>
</template>

<script>
export default {
  layout: 'empty',
  data: () => ({
    img_size: '40%',
  }),
  head() {
    return {
      title: 'خطا',
    }
  },
  methods: {
    // for responsive converting
    getPageSize() {
      const width = window.innerWidth;
      if (width < 576) return "sm";
      else if (width >= 576 && width < 768) return "md";
      else if (width >= 768 && width < 992) return "lg";
      else return "xl";
    },
  }
}
</script>
