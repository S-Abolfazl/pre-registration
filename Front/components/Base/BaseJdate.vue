<template>
  <div v-if="end_render" class="px-md-3">
    <amp-labale
      :text="text"
      :color="color"
      test-tag="labale"
      :disabled="disabled"
      :required="required"
      :help_text="help_text"
      :starRight="starRight"
      v-if="text && show_lable"
    />
    <persian-date-picker
      :view="view"
      :type="type"
      :max="max_end"
      :min="min_end"
      color="#6cc662"
      :simple="simple"
      :format="format"
      v-model="inp_value"
      :disabled="disabled"
      :clearable="clearable"
      :placeholder="placeholder"
      :input-format="inputFormat"
      :class="[disabled || readonly ? 'opacity_input' : '']"
    >
      <template #close-btn>
        <v-icon color="error" :size="clear ? 20 : 1">close</v-icon>
      </template>
      <template #clear-btn>
        <v-icon color="error" :size="clear ? 20 : 1">close</v-icon>
      </template>
    </persian-date-picker>
    <div class="font_12 error--text mt-n8">{{ error_message }}</div>
    <v-text-field v-model="inp_value" :rules="ruleItem" v-show="false" />
  </div>
</template>

<script>
let jmoment = require('jalali-moment')
export default {
  props: {
    value: {
      required: false,
    },
    readonly: {
      type: Boolean,
      default: false,
    },
    clear: {
      type: Boolean,
      default: true,
    },
    simple: {
      type: Boolean,
      default: true,
    },
    max: {
      type: String,
      required: false,
    },
    min: {
      type: String,
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
    rules: {
      default: '',
    },
    clearable: {
      type: Boolean,
      default: true,
    },
    format: {
      type: String,
      default: 'jYYYY/jMM/jDD',
    },
    inputFormat: {
      type: String,
      default: 'jYYYY/jMM/jDD',
    },
    color: {
      type: String,
      default: '#6cc662',
    },
    show_lable: {
      type: Boolean,
      default: true,
    },
    disabled: {
      type: Boolean,
      default: false,
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
    placeholder: {
      type: String,
      default: '',
    },
    type: {
      type: String,
      default: 'date',
    },
    view: {
      type: String,
      default: '',
    },
  },
  data: () => ({
    ruleItem: [],
    inpRules: {},
    inp_value: '',
    required: false,
    end_render: false,
  }),
  computed: {
    error_message() {
      if (typeof this.rules == 'function') {
        let message = this.rules(this.value)
        if (typeof message == 'string') {
          return message
        }
      }
      return ''
    },
    amp_height() {
      // if (this.$vuetify.breakpoint.xl) {
      //   return 70;
      // }
      return 40
    },
    max_end() {
      if (this.max) {
        return jmoment(this.max, 'YYYY-MM-DD').format('jYYYY/jMM/jDD')
      }
      return ''
    },
    min_end() {
      if (this.min) {
        return jmoment(this.min, 'YYYY-MM-DD').format('jYYYY/jMM/jDD')
      }
      return ''
    },
  },
  watch: {
    value(value) {
      this.setInpValue(value)
    },
    inp_value() {
      let date = ''
      if (this.inp_value) {
        date = jmoment(this.inp_value, 'jYYYY/jMM/jDD').format('YYYY-MM-DD')
      }
      this.$emit('input', date)
    },
    value_inp() {
      this.setInpValue(this.value)
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
      this.setInpValue(this.value)
    }
    this.end_render = true
  },
  methods: {
    setInpValue(value) {
      let date = ''
      if (value) {
        date = jmoment(value, 'YYYY-MM-DD').format('jYYYY/jMM/jDD')
      }
      this.inp_value = date
    },
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
  },
}
</script>

<style>
.vpd-input-group > input {
  width: 100%;
  height: 40px;
  box-shadow: none !important;
  border: 1px solid #cbcbcb !important;
}

.vpd-day[disabled] .vpd-day-text {
  color: #c2c2c2 !important;
}

.min_date > .vpd-main > .vpd-input-group > label {
  padding: 0 !important;
}

.vpd-input-group > label {
  position: absolute;
  left: 0;
  background-color: #51b34e00 !important;
}

.vpd-input-group > label > svg {
  margin-top: 12px;
  margin-bottom: 12px;
  margin-left: 6px;
  fill: #51b34e;
}

.vpd-input-group {
  height: 70px;
}

.vpd-input-group .vpd-clear-btn {
  opacity: 1 !important;
  display: block !important;
  margin-top: 3px !important;
  margin-left: 32px !important;
}

.vpd-input-group > input::placeholder {
  opacity: 1;
  color: #ffffff85;
}

.vpd-input-group > input:-ms-input-placeholder {
  color: #ffffff85;
}

.vpd-input-group > input::-ms-input-placeholder {
  color: #ffffff85;
}
</style>
