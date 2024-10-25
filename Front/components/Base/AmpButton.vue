<template>
  <v-btn
    depressed
    :type="type"
    :block="block"
    :large="large"
    :small="small"
    @click="onClick"
    :x-large="xlarge"
    :x-small="xSmall"
    :width="end_width"
    :color="end_color"
    :loading="loading"
    :height="amp_height"
    :outlined="outlined"
    :disabled="disabled"
    @mouseover="is_mouseover = true"
    @mouseleave="is_mouseover = false"
    :class="[disabled ? 'opacity_input' : '', cClass, 'amp-btn']"
  >
    <span :class="['pa-5', 'white--text', end_color, 'amp-btn_text']">
      {{ text }}
    </span>
    <span v-if="icon" class="pa-6"></span>
    <v-icon
      v-if="icon"
      :class="[iClass, icon_color, 'pa-3 py-5', 'amp-btn-icon']"
    >
      {{ icon }}
    </v-icon>
  </v-btn>
</template>

<script>
export default {
  props: {
    height: {
      type: String,
    },
    large: {
      default: true,
      required: false,
    },
    xlarge: {
      default: false,
      required: false,
    },
    small: {
      default: false,
      required: false,
    },
    xSmall: {
      default: false,
      required: false,
    },
    type: {
      default: 'button',
      required: false,
    },
    block: {
      default: false,
      required: false,
    },
    color: {
      type: String,
      required: false,
      default: 'primary',
    },
    loading: {
      type: Boolean,
      default: false,
      required: false,
    },
    disabled: {
      type: Boolean,
      default: false,
      required: false,
    },
    icon: {
      type: String,
      required: false,
    },
    text: {
      type: String,
      required: true,
    },
    width: {
      type: String,
      default: '',
    },
    cClass: {
      type: String,
      default: '',
    },
    iClass: {
      type: String,
      default: '',
    },
    outlined: {
      type: Boolean,
      default: false,
    },
  },
  data: () => ({
    is_mouseover: false,
  }),
  computed: {
    end_width() {
      if (this.width) {
        return this.width
      }
      if (this.icon) {
        return 184
      }
      return ''
    },
    end_color() {
      if (this.is_mouseover) {
        return `${this.color} darken-1`
      }
      return this.color
    },
    icon_color() {
      if (this.color == 'accent') {
        return `${this.color} darken-3`
      }
      return `${this.color} darken-1`
    },
    amp_height() {
      if (this.height) {
        return this.height
      }
      return 44
    },
  },
  methods: {
    onClick(event) {
      if (this.loading || this.disabled) {
        return
      }
      this.$emit('click', event)
    },
  },
}
</script>

<style>

.v-btn--disabled .success 
{
    background-color: #9a9a9a !important;
}
.amp-btn {
  overflow: hidden;
  padding: 0 0 !important;
}
.amp-btn-icon {
  left: 0;
  color: #fff !important;
  position: absolute !important;
}
.amp-btn_text {
  width: 100%;
}
.theme--light.v-btn.v-btn--disabled .v-icon,
.theme--light.v-btn.v-btn--disabled .v-btn__loading {
  color: #fff !important;
}
/* .amp-btn  {
  transition-delay: 0.3s;
  -webkit-transition-delay: 0.3s;
  transition: background-color 0.3s ease-in-out;
  -webkit-transition: background-color 0.3s ease-in-out;
} */

.theme--light.v-btn.v-btn--disabled:not(.v-btn--flat):not(.v-btn--text):not(.v-btn-outlined) .amp-btn_text,
.theme--light.v-btn.v-btn--disabled:not(.v-btn--flat):not(.v-btn--text):not(.v-btn-outlined) .amp-btn-icon
{
    background-color: #9a9a9a !important;
}

</style>
