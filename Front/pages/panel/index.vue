<template>
  <v-container fluid class="pa-0">

    <v-row justify="center" class="my-4 mx-0 ml-7">

      <v-col cols="5">
        <pishsabt />
      </v-col>

      <v-col cols="4">
        <term_course />
      </v-col>

      <v-col cols="3">
        <chart />
      </v-col>
    </v-row>

    <v-row justify="center" align="center" class="my-4 mx-0 ml-7">

      <v-col cols="3" >
        <amar />
      </v-col>

      <v-col cols="4" >
        <taghvim />
      </v-col>

      <v-col cols="5" >
        <professor />
      </v-col>
    </v-row>

  </v-container>
</template>

<script>

export default {
  components: {
    amar,
    chart,
    pishsabt,
    professor,
    taghvim,
    term_course,
  },
};
</script>

<style scoped>
.v-col {
  margin-bottom: 16px;
  padding: 0 8px;
}

@media (max-width: 600px) {
  .v-col {
    flex: 0 0 100% !important;
  }
}
</style>


<script>
import amar from '~/components/Panel/amar.vue';
import chart from '~/components/Panel/chart.vue';
import pishsabt from '~/components/Panel/pishsabt.vue';
import professor from '~/components/Panel/professor.vue';
import taghvim from '~/components/Panel/taghvim.vue';
import term_course from '~/components/Panel/term_course.vue';

export default {
  components: {
    amar,
    chart,
    pishsabt,
    professor,
    taghvim,
    term_course,
  },
  data: () => ({
    title: 'پنل اصلی',
  }),
  computed: {},
  beforeMount() {
    this.$store.dispatch('setPageTitle', this.title);
  },
  methods: {},
}
</script>
