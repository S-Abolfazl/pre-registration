<template>
  <div>
  <v-container fluid class="pa-0">

    <v-row justify="center" class="my-4 mx-0 ml-7">
      <v-col v-if="role == 'student'" cols="5">
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

      <v-col cols="3" v-if="role == 'academicassistant'">
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
</div>
</template>

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
  head() {
    return{
      title: 'پنل اصلی',
    }
  },
  computed: {
    role() {
      return JSON.parse(localStorage.getItem('user')).type;
    }
  },
}
</script>
