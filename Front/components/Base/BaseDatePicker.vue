<template>
    <v-flex v-if="end_render" class="mb-n6 px-3">
      <v-menu
        v-model="menu"
        min-width="290px"
        transition="scale-transition"
        :close-on-content-click="false"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-flex>
            <amp-labale
              :text="text"
              :color="color"
              test-tag="labale"
              :required="required"
              v-if="text && show_lable"
            />
            <v-text-field
              dense
              :clearable="clearable"
              full-width
              :outlined="outlined"
              :readonly="readonly"
              v-on="on"
              :type="type"
              :dark="dark"
              class="testi"
              :class="cClass"
              :prefix="prefix"
              test-tag="input"
              :rules="ruleItem"
              :height="amp_height"
              :placeholder="placeholder"
              :label="label"
              :background-color="backcolor"
              @update:error="change_error"
              v-model="inp_value"
              :prepend-inner-icon="innerIcon"
              :prepend-icon="prependIcon"
              :append-outer-icon="outerIcon"
              @click:prepend="$emit('click:prepend', $event)"
            >
            </v-text-field>
          </v-flex>
        </template>
        <div style="background-color: white">
          <persian-date-picker
            :simple="simple"
            class="mt-n10"
            auto-submit
            inline
            ref="date_picker"
            v-model="inp_value"
            :format="format"
            display-format="dddd YYYY/MM/DD "
            custom-input=".custom-input"
            color="#6A1B9A"
            no-title
            scrollable
            :min="min"
            :max="max"
            test-tag="date_picker"
            :allowed-dates="allowedDates"
            :weekday-format="weekdayFormat"
            :active-picker.sync="activePicker"
          />
          <v-btn text class="mx-5 mb-1" color="primary" @click="ok">
            تایید
          </v-btn>
        </div>
      </v-menu>
    </v-flex>
  </template>
  
  <script>
  let jmoment = require('jalali-moment')
  export default {
    props: {
      dashboard: {
        type: Boolean,
        default: false,
        required: false,
      },
      clearable: {
        type: Boolean,
        default: false,
        required: false,
      },
      dark: {
        type: Boolean,
      },
      value: {
        required: false,
      },
      backcolor: {
        type: String,
        default: 'backInput',
      },
      format: {
        type: String,
        required: false,
        default: 'jYYYY-jMM-jDD',
      },
      innerIcon: {
        type: String,
        required: false,
      },
      outerIcon: {
        type: String,
        required: false,
      },
      prependIcon: {
        type: String,
        required: false,
      },
      placeholder: {
        default: '',
        type: String,
      },
      label: {
        type: String,
      },
      text: {
        default: '',
        type: String,
      },
      activePicker: {
        default: 'DATE',
        type: String,
      },
      simple: {
        type: Boolean,
        default: false,
        required: false,
      },
      outlined: {
        type: Boolean,
        default: true,
        required: false,
      },
  
      cClass: {
        type: String,
        required: false,
      },
      min: {
        type: String,
        required: false,
      },
      max: {
        type: String,
        required: false,
      },
      rules: {
        type: String,
        default: '',
      },
      show_lable: {
        type: Boolean,
        default: true,
      },
      type: {
        type: String,
        default: 'text',
      },
      color: {
        type: String,
        required: false,
      },
      readonly: {
        type: Boolean,
        default: true,
      },
      prefix: {
        type: String,
        default: '',
      },
      allowedDates: {
        required: false,
      },
    },
    data: () => ({
      menu: false,
      ruleItem: [],
      inpRules: {},
      inp_value: '',
      required: false,
      end_render: false,
    }),
    watch: {
      menu(val) {
        val &&
          setTimeout(
            () => (this.$refs.date_picker.activePicker = this.activePicker)
          )
      },
      value() {
        this.inp_value = this.value
      },
      inp_value() {
        this.$emit('input', this.inp_value)
      },
    },
    computed: {
      amp_height() {
        if (this.$vuetify.breakpoint.xl) {
          return 10
        }
        return 10
      },
    },
    mounted() {
      this.ruleItem = []
      this.inpRules = this.$inpRules()
      this.rules.split(',').forEach((element) => {
        if (
          typeof this[element] != 'undefined' &&
          typeof this.inpRules[element] != 'undefined'
        ) {
          if (element == 'require') {
            this.required = true
          }
          this.ruleItem.push(this[element])
        }
      })
      if (this.value) {
        this.inp_value = this.value
      }
      this.end_render = true
    },
    methods: {
      ok() {
        this.menu = false
        if (this.dashboard) {
          this.$emit('test')
        }
      },
      change_error(data) {
        this.$emit('change_error', data)
      },
      require(value) {
        let check = this.$inpRules().require(value)
        if (check != true) {
          return this.error_text || this.text + check
        } else {
          return true
        }
      },
      weekdayFormat(date) {
        return this.$moment(date).format('ddd')
      },
    },
  }
  </script>
  <style scoped>
  .v-text-field {
    min-width: 160px;
  }
  .testi >>> .v-input__slot::before {
    border: 0px !important;
  }
  </style>
  