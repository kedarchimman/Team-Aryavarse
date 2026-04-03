<template>
  <div>

<!-------------------------Hero Banner Start-------------------->
<div class="hero">
  <!-- LEFT TEXT -->
      <div class="hero-text">
        <h1>So comfortable, I can go long shifts without breaking a sweat!</h1>

        <div class="features">
          <span>☁ Super-soft</span>
          <span>💧 Breathable</span>
          <span>🪶 Featherlite</span>
        </div>

        <button class="shop-btn">Shop Now</button>
      </div>

      <!-- RIGHT IMAGE -->
      <div class="hero-image-wrapper">
        <img src="/images/doctor.png" class="hero-img" />
      </div>
    </div>
    

    <!-- Category Bar-->
    <div class="category-bar">
      <button v-for="cat in categories" :key="cat">{{ cat }}</button>
    </div>

    <!-- MAIN SECTION -->
    <div class="main-container">

      <aside class="filters">
  <h2>Filters</h2>

  <!-- Category Filter -->
  <div class="filter-group">
    <p>Category</p>
    <label v-for="c in filterCategories" :key="c" class="filter-label">
      <input type="checkbox" v-model="selectedCategories" :value="c" />
      {{ c }}
    </label>
  </div>

  <!-- Fabric Filter -->
  <div class="filter-group">
    <p>Fabric</p>
    <label v-for="f in fabrics" :key="f" class="filter-label">
      <input type="checkbox" v-model="selectedFabrics" :value="f" />
      {{ f }}
    </label>
  </div>

  <!-- Color Filter -->
  <div class="filter-group">
    <p>Color</p>
    <label v-for="color in colors" :key="color" class="filter-label color-rect">
      <input type="checkbox" v-model="selectedColors" :value="color" />
      
      {{ color }}
    </label>
  </div>
</aside>

<!-- ---------------- PRODUCTS------------- -->
<section class="products">
        <div class="top-bar">
          <span>{{ products.length }} items</span>
          <span>SORT BY : MOST POPULAR</span>
        </div>

         <div class="grid">
        <div
           v-for="product in products"
          :key="product.id"
          class="card"
        >

      <!-- IMAGE AREA -->
      <div
        class="img-wrapper"
        @mouseenter="hoveredProduct = product.id"
        @mouseleave="hoveredProduct = null"
      >
        <!-- Main / Hover Image -->
        <img
          :src="hoveredProduct === product.id ? product.images?. [2]|| product.image : product.image"
          class="product-img"
          @click="goToProduct(product.id)"
        />

        <!-- Badge -->
        <span class="badge">Bestseller</span>

      <!-- Wishlist -->
      <div class="card-icons" @click.stop="handleWishlist(product)">
          <q-icon
          :name="isInWishlist(product.id) ? 'favorite' : 'favorite_border'"
          size="22px"
          :class="{ 'active-heart': isInWishlist(product.id) }"
          />

        <!-- flying hearts -->
        <span class="fly-heart h1" :class="{ show: flyingHeartId === product.id }">❤</span>
        <span class="fly-heart h2" :class="{ show: flyingHeartId === product.id }">❤</span>
        <span class="fly-heart h3" :class="{ show: flyingHeartId === product.id }">❤</span>
        <span class="fly-heart h4" :class="{ show: flyingHeartId === product.id }">❤</span>
        <span class="fly-heart h5" :class="{ show: flyingHeartId === product.id }">❤</span>
      </div>

        

        <!-- Hover Buttons -->
        <div class="hover-actions" v-if="hoveredProduct === product.id">
          <button class="quick-btn" @click="goToProduct(product.id)">
            Quick View
          </button>
          
        </div>
      </div>

      <!-- PRODUCT INFO -->
      <p class="title">{{ product.title }}</p>
      <p class="price">₹ {{ product.price }}</p>
      </div>
      </div>
</section>
</div>
</div>
</template>

<script setup>
/*------------------------------------IMPORTS -----------------------------------*/
import { useRouter } from 'vue-router'
import { ref } from 'vue'
import { products } from 'src/data/products'
import { addToCart, toggleWishlist, isInWishlist } from 'src/stores/shop'


const router = useRouter()

// hover product id
const hoveredProduct = ref(null)

/*Go to product detail page  */
const goToProduct = (id) => {
  router.push(`/product/${id}`)
}

/*Static Data */
const categories = ["Scrub Suits", "Patient Wears", "Nurses Wear", "Lab Coats"]
const filterCategories = ["Scrubs", "Stethoscope", "Lab Coats"]
const fabrics = ["Classic", "Ecoflex"]
const colors = ["Navy", "Black", "Wine"]

/*flying hearts*/
const flyingHeartId = ref(null)

const handleWishlist = (product) => {
  toggleWishlist(product)

  flyingHeartId.value = product.id

  setTimeout(() => {
    flyingHeartId.value = null
  }, 900)
}
</script>

<style lang="scss">
@import 'src/css/home.scss';
</style>