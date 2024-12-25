<template>
  <div class="table-container">
    <table class="responsive-table">
      <thead>
        <tr>
          <th>نام درس</th>
          <th>واحد</th>
          <th>نوع</th>
          <th>ظرفیت</th>
          <th>استاد</th>
          <th>روز ارائه و امتحان</th>
          <th>توضیحات</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(row, index) in TableData" :key="index" :class="{ 'alt-row': index % 2 === 0 }">
          <td>{{ row.courseName }}</td>
          <td>{{ row.unit }}</td>
          <td>{{ row.type }}</td>
          <td>{{ row.capacity }}</td>
          <td>{{ row.teacher }}</td>
          <td>{{ row.schedule }}</td>
          <td>{{ row.description }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data: ()=>({
    //   Data:[
    //   // {
    //   //   courseName: "آزمایشگاه شبکه های کامپیوتری",
    //   //   unit: 1,
    //   //   type: "عملی",
    //   //   capacity: 15,
    //   //   teacher: "دکتر وزین نژاد",
    //   //   schedule: "سه‌شنبه‌ها 19:00-17:00",
    //   //   description: "مدرس: دکتر وزین نژاد"
    //   // }
    // ],
  }),
  props: {
    TableData: {
      type: Array,
      required: false,
    },
  },
  computed: {
      finalData() {
        //this.Data = TableData;
        return this.TableData; 
    },
  },

  // mounted() {
    
  //   fetch("/path/to/data.json")
  //     .then((response) => response.json())
  //     .then((data) => {
  //       this.tableData = data; 
  //     })
  //     .catch((error) => {
  //       console.error("Error loading JSON:", error);
  //     });
  // },
  // watch: {
  //   TableData: {
  //     immediate: true,
  //     handler(newData) {
  //       this.Data = newData;
  //     },
  //   },
  // },
};
</script>


<style scoped>
.table-container {
  overflow-x: auto;
  margin: 0 auto;
  width: calc(100% - 20px); /* جلوگیری از چسبیدن به لبه‌ها */
  padding: 10px; /* افزودن فاصله از لبه‌ها */
  
}

.responsive-table {
  width: 100%;
  border-collapse: collapse;
  text-align: center;
  direction: rtl;  
  border-radius: 20px;
  overflow: hidden;
}

.responsive-table th {
  
  background-color: #7B5FF1;
  color: white;
  border: 3px solid #7B5FF1; /* هم‌رنگ با خطوط کلی جدول */
  padding: 12px;
  font-weight: bold;
}

.responsive-table td {
 
  border: 3px solid #7B5FF1; /* یکنواخت‌سازی خطوط داخلی */
  padding: 8px;
}

.responsive-table tr.alt-row td {
  background-color: rgba(123, 95, 241, 0.15); 
}

@media (max-width: 768px) {
  .responsive-table th,
  .responsive-table td {
    font-size: 12px;
    padding: 6px;
  }
}
</style>
