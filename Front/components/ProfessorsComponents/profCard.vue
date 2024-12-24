<template>
    <div class="card" style="width:100%;">
        <div class="header white1--text">
            <img :src="profileImage" alt="Profile" class="profile-image" style="margin-left: 4%;"/>
            <div>
                <p class="font_10" style="margin-bottom: 0%;">{{ role }}</p>
                <h2 class="font_15">{{ name }}</h2>
                <p class="font_10">{{ faculty }}/{{ field }}</p>
            </div>
        </div>
      <div class="black1--text mx-2 pa-2 font_10"  :style="{ lineHeight: '2' }" >
        <p>{{ description }}</p>
      </div>

      <div class="footer">
        <div>
    <v-row>
        <v-col cols="2">
            <v-icon color="white" style="-webkit-text-stroke: 2px black;" size="x-large">
                mdi-star
            </v-icon>
        </v-col>
        <v-col cols="8" class="mx-3">
            <p class="font-15" style="font-weight: bold;">نمره استاد</p>
        </v-col>
    </v-row>
    <!-- Adjust spacing between rows -->
    <v-row class="mx-2" style="margin-top: -8px;"> <!-- Adjust -8px as needed -->
        <v-icon
            v-for="n in 5"
            :key="n"
            :style="n <= rating ?  filledStyle : unfilledStyle"
            size="medium"
        >
            mdi-star
        </v-icon>
    </v-row>
</div>

      <div>
        <v-row  >
            <v-col cols="4">
            <v-icon color="white" style="-webkit-text-stroke: 2px black;" size="x-large">
                mdi-school
            </v-icon>
        </v-col>
        <v-col cols="8" style="margin-right: -10px;">
            <p class="font-15 " style="font-weight: bold;">تحصيلات</p>
        </v-col>
        </v-row>
        <v-row >
          <v-col cols="8" class="mx-2 grey--text" style="margin-top: -30px;">
            <p class="font-10"> {{ degree }}: {{ degreeDiscreption }}</p>
          </v-col>
    </v-row>
      </div>
      
      
      <div>
        <v-row  >
            <v-col cols="4">
            <v-icon color="white" style="-webkit-text-stroke: 2px black;" size="x-large">
                mdi-phone
            </v-icon>
        </v-col>
        <v-col cols="8" style="margin-right: -30px;">
            <p class="font-15 " style="font-weight: bold;">تماس</p>
        </v-col>
        </v-row>
        <v-row >
          <v-col cols="12" class="mx-2 grey--text" style="margin-top: -20px;">
            <v-row>
              <p class="font-10">شماره تماس</p>
              <p class="font-10"> {{ phone }}</p>
            </v-row>
            <v-row  style="margin-top: -15px;">
              <p class="font-10">رايانامه </p>
              <p class="font-10">{{ email }} </p>

            </v-row>
          </v-col>
    </v-row>
      </div>
        
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "ProfCard",
    props: {
      name: {
        type: String,
        required: true,
      },
      faculty: {
        type: String,
        required: true,
      },
      field: {
        type: String,
        required: true,
      },
      profileImage: {
        type: String,
        required: true,
      },
      description: {
        type: String,
        required: true,
      },
      phone: {
        type: String,
        required: true,
      },
      email: {
        type: String,
        required: true,
      },
      rating: {
        type: Number,
        required: true,
      },
      role:{
        type: String,
        required:true
      },
      degree:{
        type: String,
        required:true
      },
      degreeDiscreption:{
        type: String,
        required:true
      }
    },
    computed: {
    filledStyle() {
      return {
        background: "linear-gradient(to top, #FF8B37, #7B5FF1)",
        WebkitBackgroundClip: "text",
        WebkitTextFillColor: "transparent",
      };
    },
    unfilledStyle() {
      return {
        color: "white", // The center color
        WebkitTextStroke: "0.5px grey", // The black outline
      };
    }
}
  };
  </script>
  
  <style scoped>
  .card {
    border: 1px solid #e0e0e0;
    border-radius: 15px;
    overflow: hidden;
  }
  
  .header {
    display: flex;
    background: linear-gradient(to right, #FF8B37, #7B5FF1);
    padding: 8px 20px;
  }
  
  .profile-image {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    border: 2px solid #fff;
  }
  

  
  .footer {
    display: flex;
    justify-content: space-between;
    padding: 10px 20px;
  }
  
  
  .stars {
    font-size: 1.2em;
    color: linear-gradient(to top, #FF8B37, #7B5FF1);
  }
  
  .stars .filled {
    color: linear-gradient(to top, #FF8B37, #7B5FF1);
  }
  
  .stars span {
    color: linear-gradient(to top, #FF8B37, #7B5FF1);
  }
  </style>
  