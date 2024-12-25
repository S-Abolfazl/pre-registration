<template>
  <div class="breadcrumb-container ">
    <div 
      v-for="(item, index) in breadcrumbItems" 
      :key="index"
      class="breadcrumb-item "
      :style="{
        backgroundColor: item.color,
        borderTopLeftRadius: index === 0 ? '0px' : '0px',
        borderBottomLeftRadius: index === 0 ? '0px' : '0px',
        borderTopRightRadius: index === breadcrumbItems.length - 1 ? '30px' : '30px',
        borderBottomRightRadius: index === breadcrumbItems.length - 1 ? '30px' : '30px',
      }"
      @mouseover="showTooltip(index, item.tooltip)"
      @mouseleave="hideTooltip"
    >
      <b class="font_20">{{ item.text }}</b>
      <!-- Tooltip -->
      <div v-if="tooltipVisible && activeTooltipIndex === index" class="tooltip">
        {{ item.tooltip }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
data() {
  return {
    tooltipVisible: false,
    activeTooltipIndex: null,
    breadcrumbItems: [
      { text: "امتحانات گروه معارف اسلامی", tooltip: "تاریخ: 01/01/1403", color: "#FF8B37" },
      { text: "امتحانات", tooltip: "تاریخ: 15/01/1403", color: "#FFA96B" },
      { text: "پایان کلاسها", tooltip: "تاریخ: 01/02/1403", color: "#FFEDE0" },
      { text: "آخرین مهلت حذف تکدرس", tooltip: "تاریخ: 15/02/1403", color: "#E3E0F1" },
      { text: "حذف و اضافه", tooltip: "تاریخ: 01/03/1403", color: "#D4CDF1" },
      { text: "شروع کلاسها", tooltip: "تاریخ: 15/03/1403", color: "#AB9AF1" },
      { text: "انتخاب واحد", tooltip: "تاریخ: 01/04/1403", color: "#7B5FF1" },
    ],
  };
},
methods: {
  showTooltip(index, tooltip) {
    this.activeTooltipIndex = index;
    this.tooltipVisible = true;
  },
  hideTooltip() {
    this.tooltipVisible = false;
    this.activeTooltipIndex = null;
  },
},
};
</script>

<style scoped>
.breadcrumb-container {
display: flex;
/* align-items: center; */
/* justify-content: space-between; */
height: 80px;
width: 100%;
/* overflow: hidden; */
padding: 10px;
  

}

.breadcrumb-item {
position: relative;
flex: 1;
display: flex;
align-items: center;
justify-content: center;
text-align: center;
padding: 10px;
color: rgb(0, 0, 0);
cursor: default;
margin-right: -30px; 
z-index: 1;

}

/* .breadcrumb-item:before {
content: "";
position: absolute;
top: 0;
right: -10px;
width: 20px;
height: 50px;
background-color: inherit;
border-radius: 50%;
z-index: -1;
} */

.tooltip {
position: absolute;
top: -40px;
background-color: rgb(32, 24, 24);
color: white;
padding: 5px 10px;
border-radius: 10px;
font-size: 12px;
white-space: nowrap;
box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}
</style>