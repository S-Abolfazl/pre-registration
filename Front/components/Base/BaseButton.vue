<template>
  <v-btn
    :class="cClass"
    :disabled="disabled || loading"
    :outlined="outlined"
    @click="handleClick"
    :loading="loading"
    :color="color"
    :width="width"
    :height="height"
    :fab="fab"
    :block="fullWidth"
    :small="size === 'small'"
    :medium="size === 'medium'"
    :large="size === 'large'"
    :style="{ borderRadius: borderRadius }"
  >
    <img v-if="svg" :src="svg" class="button-svg" />

    <v-icon v-if="icon">{{ icon }}</v-icon>

    <span v-if="!loading" :class="textClass">{{ text }}</span>
  </v-btn>
</template>

<script>
export default {
  props: {
    text: {
      type: String,
      required: true,
    },
    color: {
      type: String,
      default: 'primary',
    },
    svg: {
      type: String,
      default: '',
    },
    textClass: {
      type: String,
    },
    borderRadius: {
      type: String,
      default: '6px'
    },
    width: {
      type: String,
      default: '100%',
    },
    height: {
      type: String,
      default: '44px',
    },
    size: {
      type: String,
      default: 'medium',
    },
    disabled: {
      type: Boolean,
      default: false,
    },
    outlined: {
      type: Boolean,
      default: false,
    },
    icon: {
      type: String,
      default: '',
    },
    loading: {
      type: Boolean,
      default: false,
    },
    fullWidth: {
      type: Boolean,
      default: false,
    },
    fab: {
      type: Boolean,
      default: false, // Set to true for floating action buttons
    },
  },
  computed: {
    cClass() {
      return [
        'base-button',
        { 'btn-disabled': this.disabled || this.loading },
      ];
    },
  },
  methods: {
    handleClick() {
      this.$emit('click');
    },
  },
};
</script>

<style scoped>
.base-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  font-weight: 600;
  text-transform: uppercase;
  padding: 8px 16px;
}

.v-btn--outlined {
  border: 1px solid #CBCAD7;
}

.base-button .v-icon {
  margin-right: 8px;
}

.base-button .v-btn--loading {
  pointer-events: none;
}
.button-svg {
  height: 24px;
  width: 24px;
  margin-left: 6px;
  vertical-align: middle;
}
</style>
