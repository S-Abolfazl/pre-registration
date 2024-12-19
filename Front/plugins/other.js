import Vue from 'vue'
import VuePersianDatetimePicker from 'vue-persian-datetime-picker'
import 'vue-json-pretty/lib/styles.css';

import BaseHelp from '~/components/Base/BaseHelp.vue'
import BaseCard from '~/components/Base/BaseCard.vue'
import BaseInput from '~/components/Base/BaseInput.vue'
import BaseLable from '~/components/Base/BaseLable.vue';
import BaseTitle from '~/components/Base/BaseTitle.vue'
import BaseJdate from '~/components/Base/BaseJdate.vue'
import BaseSelect from '~/components/Base/BaseSelect.vue'
import BaseButton from '~/components/Base/BaseButton.vue'
import BaseTextarea from '~/components/Base/BaseTextarea.vue'
import BaseDatePicker from '~/components/Base/BaseDatePicker.vue';
import BaseAutocomplete from '~/components/Base/BaseAutocomplete.vue'
import Bar from '~/components/Panel/Bar.vue'

Vue.component('persian-date-picker', VuePersianDatetimePicker)

Vue.component('BaseHelp', BaseHelp)
Vue.component('BaseCard', BaseCard)
Vue.component('BaseInput', BaseInput)
Vue.component('BaseLable', BaseLable)
Vue.component('BaseTitle', BaseTitle)
Vue.component('BaseJdate', BaseJdate)
Vue.component('BaseSelect', BaseSelect)
Vue.component('BaseButton', BaseButton)
Vue.component('BaseTextarea', BaseTextarea)
Vue.component('BaseDatePicker', BaseDatePicker)
Vue.component('BaseAutocomplete', BaseAutocomplete)
Vue.component('Navigationbar', Bar)
