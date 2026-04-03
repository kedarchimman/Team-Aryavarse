<template>
  <div class="filters">

    <h2>Filters</h2>

    <!-- CATEGORY -->
    <div class="section">
      <h4>CATEGORY</h4>
      <label v-for="item in categories" :key="item">
        <input type="checkbox" /> {{ item }}
      </label>
    </div>

    <!-- FABRIC -->
    <div class="section">
      <h4>FABRIC TECHNOLOGY</h4>
      <label v-for="item in fabrics" :key="item">
        <input type="checkbox" /> {{ item }}
      </label>
    </div>

    <!-- STYLE -->
    <div class="section">
      <h4>STYLE</h4>
      <label v-for="item in styles" :key="item">
        <input type="checkbox" /> {{ item }}
      </label>
    </div>

    <!-- COLOR -->
    <div class="section">
      <h4>COLOUR</h4>

      <label v-for="color in colors" :key="color.name" class="color-item">
        <span class="dot" :style="{ background: color.code }"></span>
        {{ color.name }}
        <input type="checkbox" />
      </label>

      <p class="show-more">+ Show more</p>
    </div>

    <!-- POCKETS -->
    <div class="section">
      <h4>POCKETS</h4>
      <label v-for="item in pockets" :key="item">
        <input type="checkbox" /> {{ item }}
      </label>
    </div>

  </div>
</template>

<script setup>
const categories = [
  "Scrubs",
  "Stethoscope",
  "DRIFT Jacket",
  "Lab Coats",
  "Underscrubs",
  "Scrub Caps"
]

const fabrics = [
  "Classic Scrubs",
  "Ecoflex Lite",
  "Ecoflex Scrubs",
  "Fleece"
]

const styles = [
  "Hijab",
  "6sense",
  "6sense Lite",
  "DRIFT Jacket",
  "Joggers",
  "Long Sleeves",
  "Mandarin Collar"
]

const pockets = [
  "5 Pockets",
  "8 Pockets",
  "10 Pockets"
]

const colors = [
  { name: "Navy", code: "#1d3557" },
  { name: "Wine", code: "#5a2a3a" },
  { name: "Black", code: "#000" },
  { name: "Forest Green", code: "#2f4f4f" },
  { name: "Ceil Blue", code: "#8fbcd4" },
  { name: "Heather Grey", code: "#9aa0a6" },
  { name: "Galaxy Blue", code: "#2c5aa0" },
  { name: "Olive", code: "#6b705c" },
  { name: "Hot Pink", code: "#ff4d6d" },
  { name: "Steel Grey", code: "#555" }
]
</script>

<style scoped lang="scss">
.filters {
  width: 260px;
  padding: 20px;
  background: #fff;
}

/* TITLE */
h2 {
  margin-bottom: 20px;
}

/* SECTION */
.section {
  margin-bottom: 25px;
  border-bottom: 1px solid #eee;
  padding-bottom: 15px;

  h4 {
    font-size: 14px;
    margin-bottom: 10px;
    letter-spacing: 1px;
  }

  label {
    display: flex;
    justify-content: space-between;
    margin: 8px 0;
    font-size: 14px;
    cursor: pointer;
  }

  input {
    cursor: pointer;
  }
}

/* COLOR */
.color-item {
  align-items: center;

  .dot {
    width: 14px;
    height: 14px;
    border-radius: 50%;
    margin-right: 8px;
    display: inline-block;
  }
}

/* SHOW MORE */
.show-more {
  margin-top: 10px;
  font-size: 13px;
  cursor: pointer;
  color: #555;
}
</style>