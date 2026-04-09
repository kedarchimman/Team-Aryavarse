<template>
  <div class="home-page">

    <!-- HERO -->
    <div class="hero">
      <div class="hero-text">
        <h1>So comfortable, I can go long shifts without breaking a sweat!</h1>
        <div class="features">
          <span>☁ Super-soft</span>
          <span>💧 Breathable</span>
          <span>🪶 Featherlite</span>
        </div>
        <button class="shop-btn" @click="scrollToProducts">Shop Now</button>
      </div>
      <div class="hero-image-wrapper">
        <img src="/images/doctor.png" class="hero-img" />
      </div>
    </div>

    <!-- PROMO STRIP -->
    <div class="promo-strip">
      <div class="promo-track">
        <div class="promo-group">
          <div class="promo-item" v-for="(item, index) in promoItems" :key="'first-' + index">
            <img :src="item.logo" :alt="item.text" class="promo-logo" />
            <span class="promo-text">{{ item.text }}</span>
            <span class="promo-separator"></span>
          </div>
        </div>
        <div class="promo-group">
          <div class="promo-item" v-for="(item, index) in promoItems" :key="'second-' + index">
            <img :src="item.logo" :alt="item.text" class="promo-logo" />
            <span class="promo-text">{{ item.text }}</span>
            <span class="promo-separator"></span>
          </div>
        </div>
      </div>
    </div>

    <!-- CATEGORY BAR -->
    <div class="category-bar">
      <button v-for="cat in categories" :key="cat">{{ cat }}</button>
    </div>

    <!-- MAIN: FILTERS + PRODUCTS -->
    <div class="main-container">

      <!-- FILTERS -->
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

      <!-- PRODUCTS — EXACT MEN/WOMEN CARD STRUCTURE -->
      <section class="products" ref="productsSection">
        <div class="top-bar">
          <span>{{ filteredProducts.length }} items</span>
          <span>SORT BY : MOST POPULAR</span>
        </div>

        <div class="grid">
          <div
            v-for="product in filteredProducts"
            :key="product.id + '-' + product.type"
            class="card"
          >
            <!-- Image Section — EXACT men/women sarkhi -->
            <div
              class="img-wrapper"
              @mouseenter="hoveredProduct = product.id + '-' + product.type"
              @mouseleave="hoveredProduct = null"
            >
              <img
                :src="hoveredProduct === product.id + '-' + product.type
                  ? product.images?.[1] || product.images?.[0]
                  : product.images?.[0]"
                class="product-img"
                @click="goToProduct(product)"
              />

              <span v-if="product.isBestSeller" class="badge">Bestseller</span>

              <!-- Wishlist — EXACT men/women sarkha -->
              <div class="card-icons" @click.stop="handleWishlist(product)">
                <q-icon
                  :name="isInWishlist(product.id) ? 'favorite' : 'favorite_border'"
                  size="22px"
                  :class="{ 'active-heart': isInWishlist(product.id) }"
                />
                <span class="fly-heart h1" :class="{ show: flyingHeartId === product.id + '-' + product.type }">❤</span>
                <span class="fly-heart h2" :class="{ show: flyingHeartId === product.id + '-' + product.type }">❤</span>
                <span class="fly-heart h3" :class="{ show: flyingHeartId === product.id + '-' + product.type }">❤</span>
                <span class="fly-heart h4" :class="{ show: flyingHeartId === product.id + '-' + product.type }">❤</span>
                <span class="fly-heart h5" :class="{ show: flyingHeartId === product.id + '-' + product.type }">❤</span>
              </div>

              <!-- Hover Quick View — EXACT men/women sarkha -->
              <div
                class="hover-actions"
                v-if="hoveredProduct === product.id + '-' + product.type"
              >
                <button class="quick-btn" @click="goToProduct(product)">
                  Quick View
                </button>
              </div>
            </div>

            <!-- Card Content — EXACT men/women sarkha -->
            <div class="card-content">
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
                <p class="price">₹{{ product.price }}</p>
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
import { ref, computed, nextTick } from 'vue'
import { menProducts } from 'src/data/menProducts'
import { womenProducts } from 'src/data/womenProducts'
import { addToCart, toggleWishlist, isInWishlist } from 'src/stores/shop'

const router = useRouter()

const hoveredProduct = ref(null)
const flyingHeartId = ref(null)
const productsSection = ref(null) // ✅ IMPORTANT

// FILTERS
const selectedCategories = ref([])
const selectedFabrics = ref([])
const selectedColors = ref([])

const filterCategories = ["Scrubs", "Aprons"]
const fabrics = ["Classic", "Ecoflex", "Ecoflex Lite"]
const colors = ["Maroon", "Black", "Green", "Dark Green", "Grey"]

// PROMO ITEMS
const promoItems = [
  { text: "Akasa Air",        logo: "src/assets/slider_logo/akasa_air.png" },
  { text: "Maruti Suguki",    logo: "src/assets/slider_logo/maruti_suguki.png" },
  { text: "IndiGo",           logo: "src/assets/slider_logo/indigo.png" },
  { text: "MGM Healthcare",   logo: "src/assets/slider_logo/mgm.png" },
  { text: "RSS",              logo: "src/assets/slider_logo/rss.png" },
  { text: "Rucha",            logo: "src/assets/slider_logo/rucha.png" },
  { text: "Spicejet",         logo: "src/assets/slider_logo/spicejet.png" },
  { text: "Yashoda Hospital", logo: "src/assets/slider_logo/yashoda.png" }
]

// HOME PRODUCTS IDS
const homeProductIds = [
  { id: 101, type: 'men' },
  { id: 1,   type: 'women' },
  { id: 102, type: 'men' },
  { id: 2,   type: 'women' },
  { id: 103, type: 'men' },
  { id: 3,   type: 'women' },
  { id: 105, type: 'men' },
  { id: 4,   type: 'women' },
]

// PRODUCTS FETCH
const homeProducts = computed(() => {
  return homeProductIds.map(item => {
    let product = null
    if (item.type === 'men') {
      product = menProducts.find(p => p.id === item.id)
    } else {
      product = womenProducts.find(p => p.id === item.id)
    }
    if (product) return { ...product, type: item.type }
    return null
  }).filter(Boolean)
})

// FILTER APPLY
const filteredProducts = computed(() => {
  return homeProducts.value.filter(product => {
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

// ✅ WORKING SHOP NOW SCROLL
const scrollToProducts = async () => {
  await nextTick()

  if (productsSection.value) {
    const top =
      productsSection.value.getBoundingClientRect().top + window.pageYOffset - 100

    window.scrollTo({
      top,
      behavior: 'smooth'
    })
  }
}

// ROUTING — men/women detail page
const goToProduct = (product) => {
  if (product.type === 'men') {
    router.push(`/men-product/${product.id}`)
  } else {
    router.push(`/women-product/${product.id}`)
  }
}

// WISHLIST
const handleWishlist = (product) => {
  toggleWishlist(product)
  flyingHeartId.value = product.id + '-' + product.type
  setTimeout(() => { flyingHeartId.value = null }, 900)
}

// CART
const handleAddToCart = (product) => {
  addToCart({ ...product, size: 'M' })
}

// FABRIC DESCRIPTION
const getFabricDescription = (fabric) => {
  if (fabric === 'Classic') return 'Classic fit • Soft feel • Everyday comfort'
  if (fabric === 'Ecoflex') return 'Ecoflex stretch • Breathable • Premium movement'
  if (fabric === 'Ecoflex Lite') return 'Ecoflex Lite • Ultra light • Max comfort'
  return 'Premium scrub fabric'
}
</script>

<style scoped lang="scss">
@import 'src/css/home.scss';
</style>