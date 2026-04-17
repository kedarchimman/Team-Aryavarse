<template>
  <div class="product-section">
    <div class="main-container">
      <!-- FILTERS -->
      <aside class="filters">
        <h2>Filters</h2>

        <div class="filter-group">
          <p>Category</p>
          <label
            v-for="c in availableCategories"
            :key="c"
            class="filter-label"
          >
            <input type="checkbox" v-model="selectedCategories" :value="c" />
            {{ c }}
          </label>
        </div>

        <div class="filter-group">
          <p>Fabric</p>
          <label
            v-for="f in availableFabrics"
            :key="f"
            class="filter-label"
          >
            <input type="checkbox" v-model="selectedFabrics" :value="f" />
            {{ f }}
          </label>
        </div>

        <div class="filter-group">
          <p>Color</p>
          <label
            v-for="color in availableColors"
            :key="color"
            class="filter-label"
          >
            <input type="checkbox" v-model="selectedColors" :value="color" />
            {{ color }}
          </label>
        </div>
      </aside>

      <!-- PRODUCTS -->
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

              <div class="hover-actions" v-if="hoveredProduct === product.id">
                <button class="quick-btn" @click="goToProduct(product.id)">
                  Quick View
                </button>
              </div>
            </div>

            <!-- EXACT MEN PAGE CONTENT -->
            <div class="card-content">
              <div class="fabric-wrap">
                <span class="fabric-link">{{ product.fabric }}</span>
                <div class="fabric-tooltip">
                  Premium fabric • Comfortable wear
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

              <button
                class="card-cart-btn"
                @click="handleAddToCart(product)"
              >
                Add to Cart
              </button>
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { addToCart, toggleWishlist, isInWishlist } from 'src/stores/shop'

const props = defineProps({
  products: {
    type: Array,
    default: () => []
  }
})

const router = useRouter()

const hoveredProduct = ref(null)
const flyingHeartId = ref(null)

const selectedCategories = ref([])
const selectedFabrics = ref([])
const selectedColors = ref([])

const availableCategories = computed(() => {
  return [...new Set(props.products.map(p => p.category).filter(Boolean))]
})

const availableFabrics = computed(() => {
  return [...new Set(props.products.map(p => p.fabric).filter(Boolean))]
})

const availableColors = computed(() => {
  return [...new Set(props.products.map(p => p.color).filter(Boolean))]
})

const filteredProducts = computed(() => {
  return props.products.filter(product => {
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

const goToProduct = (id) => {
  router.push(`/product/${id}`)
}

const handleAddToCart = (product) => {
  addToCart(product)
}

const handleWishlist = (product) => {
  toggleWishlist(product)
  flyingHeartId.value = product.id

  setTimeout(() => {
    flyingHeartId.value = null
  }, 900)
}
</script>

<style lang="scss">
@import 'src/css/product-section.scss';
</style>