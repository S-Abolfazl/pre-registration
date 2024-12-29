<template>
  <div>
    <ampTitle test-tag="title" v-if="title" :loading="loading" :text="title" />
    <v-card
      :disabled="loading"
      :height="cardFixHeight"
      :min-height="cardHeight"
      :class="[showPadding ? 'pa-10' : '', 'rounded-xl', classC]"
    >
      <v-progress-circular
        :size="20"
        indeterminate
        v-if="loadingCard"
        color="success"
        test-tag="progress"
        class="amp_card-progress"
      ></v-progress-circular>
      <slot></slot>
    </v-card>
  </div>
</template>

<script>
export default {
  props: {
    classC: {
      type: String,
      default: '',
    },
    loading: {
      type: Boolean,
      default: false,
    },
    loadingCard: {
      type: Boolean,
      default: false,
    },
    showPadding: {
      type: Boolean,
      default: true,
    },
    title: {
      type: String,
      default: '',
    },
    cardHeight: {
      default: '',
    },
    cardFixHeight: {
      default: '',
    },
  },
}
</script>

<style scoped>
.amp_card-progress {
  position: absolute;
  top: 6px;
  left: 6px;
}
</style>