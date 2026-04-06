<template>
  <div class="home-page">
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

    <!-- Premium Moving Brand Slider -->
    <div class="promo-strip">
      <div class="promo-track">
        <div class="promo-group">
          <div
            class="promo-item"
            v-for="(item, index) in promoItems"
            :key="'first-' + index"
          >
            <img :src="item.logo" :alt="item.text" class="promo-logo" />
            <span class="promo-text">{{ item.text }}</span>
            <span class="promo-separator"></span>
          </div>
        </div>

        <div class="promo-group">
          <div
            class="promo-item"
            v-for="(item, index) in promoItems"
            :key="'second-' + index"
          >
            <img :src="item.logo" :alt="item.text" class="promo-logo" />
            <span class="promo-text">{{ item.text }}</span>
            <span class="promo-separator"></span>
          </div>
        </div>
      </div>
    </div>

    <!-- Category Bar -->
    <div class="category-bar">
      <button v-for="cat in categories" :key="cat">{{ cat }}</button>
    </div>

    <!-- ================= MAIN SECTION (MEN PAGE EXACT STYLE) ================= -->
    <div class="main-container">

      <!-- FILTERS (Men page exact) -->
      <aside class="filters">
        <h2>Filters</h2>

        <div class="filter-group">
          <p>Category</p>
          <label v-for="c in filterCategories" :key="c" class="filter-label">
            <input type="checkbox" v-model="selectedCategories" :value="c" />
            {{ c }}
          </label>
        </div>

        <div class="filter-group">
          <p>Fabric</p>
          <label v-for="f in fabrics" :key="f" class="filter-label">
            <input type="checkbox" v-model="selectedFabrics" :value="f" />
            {{ f }}
          </label>
        </div>

        <div class="filter-group">
          <p>Color</p>
          <label v-for="color in colors" :key="color" class="filter-label">
            <input type="checkbox" v-model="selectedColors" :value="color" />
            {{ color }}
          </label>
        </div>
      </aside>

      <!-- PRODUCTS (Men page exact) -->
      <section class="products">
        <div class="top-bar">
          <span>{{ filteredProducts.length }} items</span>
          <span>SORT BY : MOST POPULAR</span>
        </div>

        <div class="grid">
          <div
            v-for="product in filteredProducts"
            :key="product.id"
            class="card"
          >
            <!-- Image Section -->
            <div
              class="img-wrapper"
              @mouseenter="hoveredProduct = product.id"
              @mouseleave="hoveredProduct = null"
            >
              <img
                :src="hoveredProduct === product.id ? product.images?.[1] || product.image : product.image"
                class="product-img"
                @click="goToProduct(product.id)"
              />

              <span class="badge">Bestseller</span>

              <!-- Wishlist -->
              <div class="card-icons" @click.stop="handleWishlist(product)">
                <q-icon
                  :name="isInWishlist(product.id) ? 'favorite' : 'favorite_border'"
                  size="22px"
                  :class="{ 'active-heart': isInWishlist(product.id) }"
                />

                <span class="fly-heart h1" :class="{ show: flyingHeartId === product.id }">❤</span>
                <span class="fly-heart h2" :class="{ show: flyingHeartId === product.id }">❤</span>
                <span class="fly-heart h3" :class="{ show: flyingHeartId === product.id }">❤</span>
                <span class="fly-heart h4" :class="{ show: flyingHeartId === product.id }">❤</span>
                <span class="fly-heart h5" :class="{ show: flyingHeartId === product.id }">❤</span>
              </div>

              <!-- Hover button -->
              <div class="hover-actions" v-if="hoveredProduct === product.id">
                <button class="quick-btn" @click="goToProduct(product.id)">
                  Quick View
                </button>
              </div>
            </div>

            <!-- Content (Men page exact) -->
            <div class="card-content">
              <!-- Fabric tooltip (Men page exact) -->
              <div class="fabric-wrap">
                <span class="fabric-link">{{ product.fabric }}</span>
                <div class="fabric-tooltip">
                  {{ getFabricDescription(product.fabric) }}
                </div>
              </div>

              <p class="title">{{ product.title }}</p>

              <div class="rating-row">
                <span class="stars">★★★★★</span>
                <span class="rating-text">{{ product.rating || 4.8 }}</span>
              </div>

              <div class="price-row">
                <p class="price">₹ {{ product.price }}</p>
              </div>

              
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { ref, computed } from 'vue'
import { products } from 'src/data/products'
import { addToCart, toggleWishlist, isInWishlist } from 'src/stores/shop'

const router = useRouter()

const hoveredProduct = ref(null)
const flyingHeartId = ref(null)

const selectedCategories = ref([])
const selectedFabrics = ref([])
const selectedColors = ref([])

// Men page exact filter options
const filterCategories = ["Scrubs", "Lab Coats", "Surgical Wear"]
const fabrics = ["Classic", "Ecoflex"]
const colors = ["Navy", "Black", "Wine", "Olive", "Grey"]

// Category bar
const categories = ["Scrub Suits", "Patient Wears", "Nurses Wear", "Lab Coats"]

// Promo strip
const promoItems = [
  { text: "Akasa Air",       logo: "src/assets/slider_logo/akasa_air.png" },
  { text: "Maruti Suguki",   logo: "src/assets/slider_logo/maruti_suguki.png" },
  { text: "IndiGo",          logo: "src/assets/slider_logo/indigo.png" },
  { text: "MGM Healthcare",  logo: "src/assets/slider_logo/mgm.png" },
  { text: "RSS",             logo: "src/assets/slider_logo/rss.png" },
  { text: "Rucha",           logo: "src/assets/slider_logo/rucha.png" },
  { text: "Spicejet",        logo: "src/assets/slider_logo/spicejet.png" },
  { text: "Yashoda Hospital",logo: "src/assets/slider_logo/yashoda.png" }
]

const goToProduct = (id) => {
  router.push(`/product/${id}`)
}

const handleWishlist = (product) => {
  toggleWishlist(product)
  flyingHeartId.value = product.id
  setTimeout(() => {
    flyingHeartId.value = null
  }, 900)
}

const handleAddToCart = (product) => {
  addToCart({
    ...product,
    size: 'M'
  })
}

// Men page exact fabric description
const getFabricDescription = (fabric) => {
  if (fabric === 'Classic') {
    return 'Classic fit • Soft feel • Everyday comfort'
  }
  if (fabric === 'Ecoflex') {
    return 'Ecoflex stretch • Breathable • Premium movement'
  }
  return 'Premium scrub fabric'
}

const filteredProducts = computed(() => {
  return products.filter(product => {
    const matchCategory =
      selectedCategories.value.length === 0 ||
      selectedCategories.value.includes(product.category)

    const matchFabric =
      selectedFabrics.value.length === 0 ||
      selectedFabrics.value.includes(product.fabric)

    const matchColor =
      selectedColors.value.length === 0 ||
      selectedColors.value.includes(product.color)

    return matchCategory && matchFabric && matchColor
  })
})
</script>

<style scoped lang="scss">
@import 'src/css/home.scss';
</style>