<template>
  <div>
    <!-- Header Section -->
    <v-row :style="{ padding: '2%' }">
      <v-col cols="8">
        <h1 class="font_40" style="text-align: right; margin-bottom: 2%;">اساتید دانشکده مهندسی کامپیوتر بهشتی</h1>
        <h2 class="font_24" style="text-align: right">
          برای انتخاب واحد بهتر و آشنایی بیشتر با اساتید میتونید در این صفحه نظرات دانشجویان ببینید
        </h2>
        <SearchBar
      v-model="searchQuery"
      style="margin-top: 8%;"
      width="70%"
      @search="onSearch"
    />
      </v-col>
      <v-col cols="4">
        <img
          src="~/static/image/professors/Collaborate 1.png"
          alt="png"
          style="width: 90%;"
        />
      </v-col>
    </v-row>

    <!-- Main Content Section -->
    <v-row style="width:100%;">
      <!-- Left Column -->
      <v-col cols="7" >
        <div v-for="(prof, index) in leftProfessors" :key="prof.name" style="margin-bottom: 2rem;">
          <profCard
            :name="prof.name"
            :avatar ="prof.avatar "
            :description ="prof.description "
            :mobile_number="prof.mobile_number"
            :email="prof.email"
            :rate ="prof.rate "
            :role="prof.role"
            :department="prof.department"
            :field="prof.field"
            :education="prof.education"
            :specialization="prof.specialization"
          />
        </div>
      </v-col>

      <!-- Right Column -->
      <v-col cols="5">
        <div v-for="(prof, index) in rightProfessors" :key="prof.name" style="margin-bottom: 2rem;">
          <profCard
            :name="prof.name"
            :avatar ="prof.avatar "
            :description ="prof.description "
            :mobile_number="prof.mobile_number"
            :email="prof.email"
            :rate ="prof.rate "
            :role="prof.role"
            :department="prof.department"
            :field="prof.field"
            :education="prof.education"
            :specialization="prof.specialization"
          />
        </div>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import SearchBar from "../ProfessorsComponents/searchBar.vue";
import profCard from "../ProfessorsComponents/profCard.vue";

export default {
  components: {
    SearchBar,
    profCard,
  },
  data() {
    return {
      searchQuery: '',
      professors: [],
    };
  },
  computed: {
    // Dynamically filters professors based on the search query
    filteredProfessors() {
      const query = this.searchQuery.toLowerCase();
      return this.professors.filter(prof =>
        prof.name.toLowerCase().includes(query)
      );
    },
    // Splits the filtered professors into the left column
    leftProfessors() {
      return this.filteredProfessors.filter((_, index) => index % 2 === 0);
    },
    // Splits the filtered professors into the right column
    rightProfessors() {
      return this.filteredProfessors.filter((_, index) => index % 2 === 1);
    },
  },
  methods: {
    onSearch(query) {
      this.searchQuery = query; // Update searchQuery when user types
    },
    getData(){
      this.$reqApi("master/list/", {}, {}, true, 'get')
      .then((response) => {
        this.professors = response;
      })
      .catch((error) => {
        this.$toast.error(error);
      })
    },
  },
mounted() {
  this.filteredProfessors = this.professors; // Default to all professors
  this.getData();
}
};
</script>
