<template>
  <div class="d-flex rtl-item">
    <div class="py-1">
      <span :class="[color, textClass, 'font_16', 'gray3--text']" v-html="text"> </span>
    </div>

    <div v-if="required" class="pt-1 mr-1">
      <span class="red--text font_16">*</span>
    </div>

    <v-tooltip
      bottom
      color="primary"
      v-if="help_text"
      :max-width="tooltipWidth"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-icon v-bind="attrs" v-on="on" class="font_20 mr-auto">
          mdi-information-outline
        </v-icon>
      </template>
      <span v-html="help_text"></span>
    </v-tooltip>
  </div>
</template>

<script>
export default {
  props: {
    text: {
      type: String,
      required: false,
    },
    color: {
      type: '',
      required: false,
    },
    tooltipWidth: {
      type: String,
      default: '350',
    },
    required: {
      type: Boolean,
      default: false,
    },
    help_text: {
      type: String,
      default: '',
    },
    disabled: {
      type: Boolean,
      default: false,
    },
    textClass: {
      type: String,
      default: '',
    },
    tooltipWidth: {
      type: String,
      default: '350',
    },
  },
}
</script>
