import Vue from 'vue'
import VuePersianDatetimePicker from 'vue-persian-datetime-picker'
import 'vue-json-pretty/lib/styles.css';

import AmpHelp from '~/components/Base/AmpHelp.vue'
import AmpCard from '~/components/Base/AmpCard.vue'
import AmpChart from '~/components/Base/AmpChart.vue'
import AmpInput from '~/components/Base/AmpInput.vue'
import AmpTitle from '~/components/Base/AmpTitle.vue'
import AmpJdate from '~/components/Base/AmpJdate.vue'
import AmpSelect from '~/components/Base/AmpSelect.vue'
import AmpButton from '~/components/Base/AmpButton.vue'
import AmpTextarea from '~/components/Base/AmpTextarea.vue'
import AmpDatePicker from '~/components/Base/AmpDatePicker.vue';
import AmpAutocomplete from '~/components/Base/AmpAutocomplete.vue'

Vue.component('persian-date-picker', VuePersianDatetimePicker)

Vue.component('AmpHelp', AmpHelp)
Vue.component('AmpCard', AmpCard)
Vue.component('AmpInput', AmpInput)
Vue.component('AmpTitle', AmpTitle)
Vue.component('AmpJdate', AmpJdate)
Vue.component('AmpChart', AmpChart)
Vue.component('AmpSelect', AmpSelect)
Vue.component('AmpButton', AmpButton)
Vue.component('AmpTextarea', AmpTextarea)
Vue.component('AmpDatePicker', AmpDatePicker)
Vue.component('AmpAutocomplete', AmpAutocomplete)
