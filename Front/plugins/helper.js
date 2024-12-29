let jmoment = require('jalali-moment')

export default ({ _, store }, inject) => {
  inject('reloadPage', () => {
    window.location.reload()
  })
  inject('FarsiToEnglishNumber', (stringNumber) => {
    if (!Boolean(stringNumber)) {
      return stringNumber
    }
    return String(
      stringNumber
        .toString()
        .replace(/[٠١٢٣٤٥٦٧٨٩]/g, function (d) {
          return d.charCodeAt(0) - 1632 // Convert Arabic numbers
        })
        .replace(/[۰۱۲۳۴۵۶۷۸۹]/g, function (d) {
          return d.charCodeAt(0) - 1776 // Convert Persian numbers
        })
    )
  })
  inject('inpRules', () => {
    return {
      require: (v) => (typeof v != 'undefined' && v !== '' && v != null && v.toString().replace(/\s/g, '') != '') || 'کامل نشده',
      max_250: (v) => !v || v.length <= 200 || 'حداکثر 250 حرف',
      fa_text: (v) => !v || /^[\u0600-\u06FF ]+$/.test(v) || 'فقط حروف فارسی',
      en_text: (v) => !v || /^[a-z A-Z 0-9 \- _ \.]+$/.test(v) || 'فقط حروف انگلیسی',
      number: (v) => !v || /^[0-9][0-9]*$/.test(v) || 'فقط اعداد صحیح',
      number_float: (v) => !v || /^[1-9][0-9 .]*$/.test(v) || 'فقط اعداد صحیح و اعشاری',
      len_4: (v) => !v || v.length == 4 || 'چهار رقمی وارد کنید',
      min_6: (v) => !v || v.length >= 6 || 'حداقل 6 حرف',
      min_10:(v)=>  !v || v.length >= 10 || 'حداقل 10 حرف',
      ip: (v) => !v || /^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$/.test(v) || 'آی پی درست نیست',
      min_1: (v) => !v || v.length >= 1 || 'حداقل یک مورد انتخاب بشود',
      percent: (v) => !v || (0 <= v && v <= 100) || 'عدد بین 0 تا 100',
      url: (v) => !v || /(http[s]?:\/\/(www\.)?|ftp:\/\/(www\.)?|www\.){1}[0-9A-Za-z-\\.@:%_\+~#=]+\.[0-9A-Za-z-\\.@:%_\+~#=]+/.test(v) || 'آدرس(url) نامعتبر',
      phone: (v) => !v || v.length == 11 || 'شماره تلفن درست وارد نشده',
      mobile: (v) => !v || (/^(9|09|٩|٠٩|۹|۰۹)/.test(v) && v.length == 11) || 'شماره وارد شده صحیح نیست',
      national_code: (v) => !v || (v.length == 10 && /^[0-9][0-9]*$/.test(v)) || 'کد ملی اشتباه است',
      post_code: (v) => !v || v.length == 10 || 'کدپستی درست وارد نشده',
      password: (v) => !v || /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{6,}$/.test(v) || 'رمز عبور نامعتبر',
      email: (v) => !v || /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(v) || 'پست الکترونیکی نامعتبر',
    }
  })
  inject('checkNotNull', (...item) => {
    for (let index = 0; index < item.length; index++) {
      const element = item[index]
      if (typeof element == 'undefined' || element === '' || element === '' || element === null) {
        return false
      }
    }
    return true
  })
  inject('toJalali', (date, format_in = 'YYYY-MM-DDTHH:mm:ss.SSSZ', format_out = 'jYYYY/jMM/jDD HH:mm') => {
    try {
      return jmoment(date, format_in).format(format_out)
    } catch (error) {
      return date
    }
  })
  inject('getSettingList', (key) => {
    let items = store.state.setting.site_settings.map((x) => {
      if (x.key == key) {
        let value = JSON.parse(x.value)
        return { text: value.text, value: value.value }
      }
    })
    return items
  })
}
