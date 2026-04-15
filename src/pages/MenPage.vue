<template>
  <div class="men-page">
    <div class="main-container">
      <!-- Filters -->
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

         <!-- SLEEVE -->
        <div class="filter-group">
          <p>Style</p>
          <label v-for="s in sleeves" :key="s" class="filter-label">
          <input type="checkbox" v-model="selectedSleeves" :value="s" />
          {{ s }}
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

      <!-- Products -->
      <section class="products">
        <div class="top-bar">
          <span>{{ filteredProducts.length }} items</span>
          <SortDropdown v-model="selectedSort" />
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
                @click="goToMenProduct(product)"
              />

              <span v-if="product.isBestSeller" class="badge">Bestseller</span>

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
                <button class="quick-btn" @click="goToMenProduct(product)">
                  Quick View
                </button>
              </div>
            </div>

            <!-- Content -->
            <div class="card-content">
              <!-- Knya style fabric text -->
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
                <p class="price">₹ {{ Number(product.price).toFixed(2) }}</p>
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
import { menProducts } from 'src/data/menProducts'
import { apronsProducts } from 'src/data/apronsProducts'
import { addToCart, toggleWishlist, isInWishlist } from 'src/stores/shop'
import SortDropdown from 'src/components/SortDropdown.vue'

//sort by code
const selectedSort = ref('')

const router = useRouter()

const hoveredProduct = ref(null)
const flyingHeartId = ref(null)


// FILTER STATES
const selectedCategories = ref([])
const selectedFabrics = ref([])
const selectedColors = ref([])
const selectedSleeves = ref([])


// FILTER OPTIONS
const filterCategories = ["Scrubs", "Aprons"]

const fabrics = ["Classic", "Ecoflex Lite","Ecoflex"]

const sleeves = [
 "Full Sleeve Aprons",
 "3-4 Sleeve Aprons",
 "Half Sleeve Aprons"
]

const colors = ["Brown", "Green", "Grey", "Mint Green", "Maroon","White"]


// MERGE MEN PRODUCTS + ONLY MEN APRONS
const allMenProducts = computed(() => {
  return [
    ...menProducts,

    ...apronsProducts.filter(
      apron => apron.gender === "Men"
    )
  ]
})

// ROUTING men/aprons mix 
const goToMenProduct = (product) => {

  if (product.type === 'aprons') {
    router.push(`/aprons-product/${product.id}`)
  }

  else {
    router.push(`/men-product/${product.id}`)
  }

}

// WISHLIST
const handleWishlist = (product) => {
  toggleWishlist(product)

  flyingHeartId.value = product.id

  setTimeout(() => {
    flyingHeartId.value = null
  }, 900)
}


// CART
const handleAddToCart = (product) => {
  addToCart({
    ...product,
    size: 'M'
  })
}


// FABRIC DESCRIPTION
const getFabricDescription = (fabric) => {
  if (fabric === 'Classic') {
    return 'Classic fit • Soft feel • Everyday comfort'
  }

  if (fabric === 'Ecoflex') {
    return 'Ecoflex stretch • Breathable • Premium movement'
  }

  return 'Premium scrub fabric'
}


// FILTER LOGIC
const filteredProducts = computed(() => {

  let products = allMenProducts.value.filter(product => {

    const matchCategory =
      selectedCategories.value.length === 0 ||
      selectedCategories.value.includes(product.category)

    const matchFabric =
      selectedFabrics.value.length === 0 ||
      selectedFabrics.value.includes(product.fabric)

    const matchSleeve =
      selectedSleeves.value.length === 0 ||
      selectedSleeves.value.includes(product.sleeve)

    const matchColor =
      selectedColors.value.length === 0 ||
      selectedColors.value.includes(product.color)

    return matchCategory && matchFabric && matchSleeve && matchColor
  })


  // SORTING
  if (selectedSort.value === 'low') {
    products.sort((a, b) => a.price - b.price)
  }

  else if (selectedSort.value === 'high') {
    products.sort((a, b) => b.price - a.price)
  }

  else if (selectedSort.value === 'bestseller') {
    products = products.filter(product => product.isBestSeller)
  }

  return products
})

</script>

<style scoped lang="scss">
@import 'src/css/men.scss';
</style>