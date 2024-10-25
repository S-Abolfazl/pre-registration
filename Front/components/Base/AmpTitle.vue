<template>
  <div class="my-2">
    <v-progress-circular
      :size="25"
      indeterminate
      v-if="loading"
      color="success"
      test-tag="progress"
      class="amp_card-progress"
    ></v-progress-circular>
    <div
      v-else
      test-tag="btn_rounded"
      class="pa-1 mr-1 my-1 success rounded-circle d-inline-block"
    ></div>
    <span test-tag="title" class="font_xl secondarylabale--text">
      {{ text }}
    </span>
  </div>
</template>

<script>
export default {
  props: {
    text: {
      type: String,
      required: true,
    },
    loading: {
      type: Boolean,
      default: false,
    },
  },
}
</script>
