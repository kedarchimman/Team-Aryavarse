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
                @click="goToMenProduct(product.id)"
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
                <button class="quick-btn" @click="goToMenProduct(product.id)">
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
import { menProducts } from 'src/data/menProducts'
import { addToCart, toggleWishlist, isInWishlist } from 'src/stores/shop'

const router = useRouter()

const hoveredProduct = ref(null)
const flyingHeartId = ref(null)

const selectedCategories = ref([])
const selectedFabrics = ref([])
const selectedColors = ref([])

const filterCategories = ["Scrubs", "Lab Coats", "Surgical Wear"]
const fabrics = ["Classic", "Ecoflex"]
const colors = ["Navy", "Black", "Wine", "Olive", "Grey"]

const goToMenProduct = (id) => {
  router.push(`/men-product/${id}`)
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
  return menProducts.filter(product => {
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
@import 'src/css/men.scss';
</style>