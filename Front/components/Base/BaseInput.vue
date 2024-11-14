<template>
  <div v-if="end_render" :class="parentClass">
    <BaseLable
      :text="text"
      :color="color"
      :disabled="disabled"
      test-tag="labale"
      :required="required"
      :textClass="textClass"
      :help-text="helpText"
      :starRight="starRight"
      v-if="text && showLable"
    />
    <v-text-field
      dense
      :style="{
        width: width,
        borderRadius: borderRadius,
      }"
      :type="inp_type"
      :outlined="outlined"
      :rounded="rounded"
      :suffix="suffix"
      :prefix="prefix"
      test-tag="input"
      :rules="ruleItem"
      @click="inputClick"
      v-model="inp_value"
      :readonly="readonly"
      :disabled="disabled"
      :maxlength="maxlength"
      :append-icon="append_icon"
      :placeholder="placeholder"
      @click:append="appendClick"
      :background-color="backgroundColor"
      :prepend-inner-icon="prependInnerIcon"
      :autocomplete="type == 'password' ? 'new-password' : ''"
      :class="[cClass, isFloat || isNumber ? 'ltr-item' : '', (disabled || readonly) && activeOpacity ? 'opacity_input' : '']"
    >
    </v-text-field>
  </div>
</template>

<script>
export default {
  props: {
    width: {
      type: String,
      default: '100px'
    },
    borderRadius: {
      type: String,
      default: '6px'
    },
    activeOpacity: {
      type: Boolean,
      default: true,
    },
    textClass: {
      type: String,
      default: '',
    },
    outlined: {
      type: Boolean,
      default: true,
    },
    isFloat: {
      type: Boolean,
      default: false,
    },
    isNumber: {
      type: Boolean,
      default: false,
    },
    value: {
      required: false,
    },
    text: {
      type: String,
      required: false,
    },
    cClass: {
      type: String,
      required: false,
    },
    placeholder: {
      type: String,
      default: '',
    },
    rules: {
      default: '',
    },
    type: {
      type: String,
      default: 'text',
    },
    color: {
      type: String,
      required: false,
    },
    backgroundColor: {
      type: String,
      default: '',
    },
    appendIcon: {
      type: String,
      default: '',
    },
    prependInnerIcon: {
      default: '',
    },
    rounded: {
      type: Boolean,
      required: false,
    },
    showLable: {
      type: Boolean,
      default: true,
    },
    readonly: {
      type: Boolean,
      default: false,
    },
    prefix: {
      type: String,
      default: '',
    },
    suffix: {
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
    disabled: {
      type: Boolean,
      default: false,
    },
    activeInputClick: {
      type: Boolean,
      default: true,
    },
    helpText: {
      type: String,
      default: '',
    },
    maxlength: {
      default: '',
    },
    parentClass: {
      default: '',
    },
  },
  data: () => ({
    ruleItem: [],
    inpRules: {},
    inp_value: '',
    required: false,
    end_render: false,
    password_click: false,
  }),
  computed: {
    append_icon() {
      if (this.appendIcon) {
        return this.appendIcon
      }
      if (this.type == 'password') {
        return this.password_click ? 'visibility' : 'visibility_off'
      }
    },
    inp_type() {
      if (this.type == 'password' && this.password_click) {
        return 'text'
      }
      return this.type
    },
  },
  watch: {
    value() {
      let value = this.value
      if (Boolean(value)) {
        if (this.isPrice || this.isNumber || this.isFloat) {
          value = this.$FarsiToEnglishNumber(value)
        }
        if (this.isPrice) {
          value = this.$price(value)
        }
      }
      this.inp_value = value
    },
    inp_value() {
      let value = this.inp_value
      if (Boolean(value) && (this.isPrice || this.isNumber || this.isFloat)) {
        value = this.$FarsiToEnglishNumber(value)
        value = value.replace(/\D/g, '')
      }
      this.$emit('input', value)
    },
    value_inp() {
      this.inp_value = this.value_inp
    },
    rules: {
      deep: true,
      handler() {
        this.setRules()
      },
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
      this.required = false
      let ruleItem = []
      this.ruleItem = []
      let inpRules = this.$inpRules()
      if (typeof this.rules == 'string') {
        this.rules.split(',').forEach((element) => {
          if (typeof inpRules[element] != 'undefined') {
            if (element == 'require') {
              this.required = true
            }
            if (element == 'password') {
              ruleItem = [...ruleItem, ...inpRules[element]]
            } else {
              ruleItem.push(inpRules[element])
            }
          }
        })
      } else if (typeof this.rules == 'function') {
        ruleItem.push(this.rules)
      }
      this.$nextTick(() => {
        this.ruleItem = [...ruleItem]
      })
    },
    appendClick($event) {
      this.$emit('click:append', $event)
      this.password_click = !this.password_click
    },
    inputClick($event) {
      if (this.activeInputClick) {
        this.$emit('click:append', $event)
      }
    },
  },
}
</script>
