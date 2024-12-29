<template>
  <v-tooltip bottom :color="color" :max-width="width">
    <template v-slot:activator="{ on, attrs }">
      <v-icon v-if='!title' :color="color" v-bind="attrs" v-on="on">{{icon}}</v-icon>
      <v-btn small v-if='title' :class="color" v-bind="attrs" v-on='on'  >{{title}}</v-btn>
    </template>
    <span v-html="text"></span>
  </v-tooltip>
</template>

<script>
export default {
  props: {
    text: {
      type: String,
      default: '',
    },
    color:{
      default:'primary'
    },
    icon:{
      default:'info'
    },
    title:{
      type:String,
      default:''
    },
    width: {
      type: String,
      default: '350',
    },
  },
}
</script>
