import { version } from './package.json'
import colors from 'vuetify/es5/util/colors'
const fa = require('./locales/vuetifyjs.fa.json')

export default {
  ssr: false,
  target: 'static',
  telemetry: false,
  head: {
    title: 'سامانه پیش ثبت‌نام',
    titleTemplate: '%s',
    htmlAttrs: {
      lang: 'fa',
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1, maximum-scale=1' },
      { name: 'format-detection', content: 'telephone=no' },
    ],
    link: [
      { rel: 'stylesheet', href: '/css/app.css' },
      { rel: 'stylesheet', href: '/css/fonts.css' },
      { rel: 'stylesheet', href: '/css/mobile.css' },
      { rel: 'stylesheet', href: '/css/google_font.css' },
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ],
  },
  plugins: [
    '~/plugins/axios',
    '~/plugins/helper',
    { src: '~/plugins/other.js', ssr: false },
    { src: '~/plugins/vue-persian-datetime-picker', ssr: false },
  ],
  buildModules: ['@nuxtjs/toast', '@nuxtjs/moment', '@nuxtjs/vuetify'],
  modules: [
    '@nuxtjs/axios',
    '@nuxtjs/pwa',
  ],
  toast: {
    duration: 3000,
    position: 'bottom-left',
  },
  // moment: {
  //   defaultTimezone: 'Asia/Tehran'
  // },
  vuetify: {
    // customVariables: ['~/assets/variables.scss'],
    theme: {
      dark: false,
      themes: {
        dark: {
          primary: colors.blue.darken2,
          accent: colors.grey.darken3,
          secondary: colors.blue.darken4,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3,
        },
        light: {
          info: '#00ABE1',
          error: '#ff0000',
          accent: '#1A2238',
          success: '#169e1a',
          warning: '#ffbb00',

          primary: '#6938EF',

          orange1: '#FF8B37',

          gray1: '#686677',
          gray2: '#CBCAD7',
          gray3: '#9794AA',

          black1: '#100F14',
          black2: '#19181F',

          white1: '#FFFFFF',
        }
      },
    },
    rtl: true,
    lang: {
      locales: { fa },
      current: 'fa',
    },
    icons: {
      iconfont: 'md',
    },
    defaultAssets: false,
    materialIcons: false,
  },
  router: {
    mode: 'hash'
  },
  publicRuntimeConfig: {
    version: version,
  },
  build: {
    postcss: null,
    extend(config, ctx) {
      config.resolve.alias['vue'] = 'vue/dist/vue.common'
    },
  }
}
