import { version } from './package.json';
import colors from 'vuetify/es5/util/colors';
const fa = require('./locales/vuetifyjs.fa.json');

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
      { rel: 'icon', type: 'image/x-icon', href: 'favicon.ico' }
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
  vuetify: {
    theme: {
      dark: false,
      themes: {
        dark: {
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
          gray4: '#303030',

          black1: '#FFFFFF',
          black2: '#FFFFAA',

          white1: '#19181F',

          red1: '#FF1100',
        },
        light: {
          info: '#00ABE1',
          error: '#ff0000',
          accent: '#1A2238',
          success: '#169e1a',
          warning: '#ffbb00',
          primary: '#6938EF',
          orange1: '#FF8B37',
          orange2: '#FFD7C7',

          gray1: '#686677',
          gray2: '#CBCAD7',
          gray3: '#9794AA',
          gray4: '#EAE6FA',

          black1: '#100F14',
          black2: '#19181F',
          black3: '#000000',

          white1: '#FFFFFF',

          blue1: '#E3E3FF',
          blue2: '#7B5FF1',

          red1: '#FF1100',
        }
      },
    },
    rtl: true,
    lang: {
      locales: { fa },
      current: 'fa',
    },
    icons: {
      defaultSet: 'mdi', // Use the Material Design Icons
      iconfont: 'mdi',    // Ensure the correct font is used
    },
    defaultAssets: {
      icons: 'mdi', // Ensure default assets are loaded
    },
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
      config.resolve.alias['vue'] = 'vue/dist/vue.common';
    },
  },
  css: [
    '@mdi/font/css/materialdesignicons.css'
  ]
};
