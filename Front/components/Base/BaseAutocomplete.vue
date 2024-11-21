<template>
  <div v-if="end_render" class="px-md-3" :style="{width: width,}">
    <BaseLable
      :text="text"
      :color="color"
      test-tag="labale"
      :disabled="disabled"
      :required="required"
      :help_text="help_text"
      :starRight="starRight"
      v-if="text && show_lable"
    />
    <v-autocomplete
      dense
      eager
      outlined
      :style="{
        width: '100%',
        borderRadius: borderRadius,
      }"
      :rounded="rounded"
      :error="error"
      :chips="chips"
      :items="items"
      :prefix="prefix"
      test-tag="input"
      :rules="ruleItem"
      :loading="loading"
      v-model="inp_value"
      :readonly="readonly"
      :disabled="disabled"
      :multiple="multiple"
      :item-text="itemText"
      :placeholder="placeholder"
      @click:append="$emit('click:append', $event)"
      :class="[disabled || readonly ? 'opacity_input' : '', classC]"
    ></v-autocomplete>
  </div>
</template>

<script>
export default {
  props: {
    width: {
      type: String,
      default: '100px'
    },
    value: {
      required: false,
    },
    error: {
      required: false,
    },
    text: {
      type: String,
      required: false,
    },
    classC: {
      type: String,
      default: '',
    },
    rules: {
      default: '',
    },
    disabled: {
      type: Boolean,
      default: false,
    },
    items: {
      items: Array,
      required: true,
    },
    color: {
      type: String,
      required: false,
    },
    readonly: {
      type: Boolean,
      default: false,
    },
    show_lable: {
      type: Boolean,
      default: true,
    },
    loading: {
      type: Boolean,
      default: false,
    },
    prefix: {
      type: String,
      default: '',
    },
    value_inp: {
      default: '',
    },
    starRight: {
      type: Boolean,
      default: false,
    },
    placeholder: {
      type: String,
      default: '',
    },
    help_text: {
      type: String,
      default: '',
    },
    multiple: {
      type: Boolean,
      default: false,
    },
    chips: {
      type: Boolean,
      default: false,
    },
    itemText: { require: false, default: 'text' },
  },
  data: () => ({
    ruleItem: [],
    inpRules: {},
    inp_value: '',
    required: false,
    end_render: false,
  }),
  watch: {
    value() {
      this.inp_value = this.value
    },
    inp_value() {
      this.$emit('input', this.inp_value)
    },
    value_inp() {
      this.inp_value = this.value_inp
    },
    rules() {
      this.setRules()
    },
  },
  mounted() {
    this.setRules()
    if (this.value_inp) {
      this.inp_value = this.value_inp
    }
    if (this.value) {
      this.inp_value = this.value
    }
    this.end_render = true
  },
  methods: {
    setRules() {
      this.ruleItem = []
      let inpRules = this.$inpRules()
      if (typeof this.rules == 'string') {
        this.rules.split(',').forEach((element) => {
          if (typeof inpRules[element] != 'undefined') {
            if (element == 'require' || element == 'min_1') {
              this.required = true
            }
            this.ruleItem.push(inpRules[element])
          }
        })
      } else if (typeof this.rules == 'function') {
        this.ruleItem.push(this.rules)
      }
    },
  },
}
</script>
