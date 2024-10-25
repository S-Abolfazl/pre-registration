<template>
  <div v-if="end_render" :class="parentClass">
    <amp-labale
      :text="text"
      :color="color"
      test-tag="labale"
      :disabled="disabled"
      :required="required"
      :help_text="help_text"
      :starRight="starRight"
      v-if="text && show_lable"
      :tooltipWidth="tooltipWidth"
    />
    <v-select

      dense
      eager
      outlined
      :dark="dark"
      :chips="chips"
      :items="items"
      :prefix="prefix"
      test-tag="input"
      :rules="ruleItem"
      v-model="inp_value"
      :readonly="readonly"
      :disabled="disabled"
      :multiple="multiple"
      :clearable="clearable"	
      :background-color="backgroundColor"
      :placeholder="placeholder"
      :class="[disabled || readonly ? 'opacity_input' : '', classC, cClass]"
    ></v-select>
  </div>
</template>

<script>
export default {
  props: {
    value: {
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
    clearable: {
      type: Boolean,
      default: false,
    },
    dark: {
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
    cClass: {
      type: String,
      required: false,
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
    help_text: {
      type: String,
      default: '',
    },
    parentClass: {
      default: 'px-md-3',
    },
    multiple: {
      type: Boolean,
      default: false,
    },
    chips: {
      type: Boolean,
      default: false,
    },
    backgroundColor: {
      type: String,
      default: '',
    },
    tooltipWidth: {
      type: String,
      default: '350',
    },
    placeholder: {
      type: String,
      default: 'انتخاب کنید',
    },
    firstSelect: {
      type: Boolean,
      default: false,
    },
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
    items() {
      this.checkIsItem()
      this.checkFirstSelect()
    },
  },
  mounted() {
    this.setRules()
    if (this.value_inp || this.value_inp === false) {
      this.inp_value = this.value_inp
    }
    if (this.value) {
      this.inp_value = this.value
    }

    this.end_render = true
    this.checkFirstSelect()
  },
  methods: {
    setRules() {
      this.required = false
      this.ruleItem = []
      let inpRules = this.$inpRules()
      if (typeof this.rules == 'string') {
        this.rules.split(',').forEach((element) => {
          if (typeof inpRules[element] != 'undefined') {
            if (element == 'require') {
              this.required = true
            }
            this.ruleItem.push(inpRules[element])
          }
        })
      } else if (typeof this.rules == 'function') {
        this.ruleItem.push(this.rules)
      }
    },
    checkIsItem() {
      if (!Array.isArray(this.items)) {
        return
      }
      if (this.multiple) {
        return
      }
      let item = this.items.find((x) => x.value == this.value)
      if (item == null) {
        this.inp_value = ''
      }
    },

    checkFirstSelect() {
      if (this.firstSelect && this.items.length > 0) {
        this.inp_value = this.items[0].value
      }
    },
  },
}
</script>
