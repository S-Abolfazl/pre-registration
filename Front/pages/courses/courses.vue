<template>
    <v-form v-model="valid">
      
      <v-col cols="12"  class="my-4">
        
        <v-row >
          <v-col cols="6">
            <span>
              <b class="black1--text font_43">دروس ارائه شده در نیم سال اول </b>
            </span>
          </v-col>
          <v-col cols="5">
            <span>
              <v-card class="year-card blue2" >
                <v-row no-gutters >
                    <span class="title">
                      <b class="font_40 black1--text">1403-1404</b>
                    </span>
                    <span class="image-wrapper">
                      <img src="/image/panel/term_courses.png" alt="course" class="course-image" />
                    </span>
                  
                </v-row>
              </v-card>
            </span>
          </v-col>
          
        </v-row>
  
        <v-row rows="12" >
         
        </v-row>
  
        <v-row rows="12" >
         
        </v-row>
      </v-col>
  
    </v-form>
  </template>
  
  <script>
  
  export default {
    components: {
     
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
  
  
  <style scoped>
  .year-card {
    border-radius: 30px;
    width: 30%; 
    height: 45px; 
    position: relative; 
    overflow: visible;
  }
  
  .image-wrapper {
    position: absolute;
    top: -85%; 
    right: 55%; 
    width: 100%;
    
  }
  .course-image {
    width: 40%; 
  }
  .title{
    margin: 10px;
    width: 100%;
  }
  .col-6 {
    flex: 0 0 30%;
  }
  .col-5 {
      margin-top: 11px;
      flex: 0 0 35%;
  }
  </style>
  
  
  