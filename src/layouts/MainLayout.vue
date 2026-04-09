<template>
  <q-layout>
    <div class="navbar">

      <!-- HAMBURGER BUTTON -->
      <div class="hamburger" @click="menuOpen = true">
        <span></span>
        <span></span>
        <span></span>
      </div>

      <!-- logo -->
       <div class="logo" @click="$router.push('/')">
          <img src="/src/assets/logo/logo5.png" alt="Parallel Logo" class="logo-img" />

          <div class="brand-text">
            <div class="brand-title">PARALLEL</div>
              <div class="brand-subtitle">
                A Division of Pushpa Textile
              </div>
          </div>
        </div>

      <!-- links -->
      <div class="links">
        <span @click="$router.push('/')">Home</span>
        <span @click="$router.push('/men')">Men</span>
        <span @click="$router.push('/women')">Women</span>
        <span @click="$router.push('/bulk')">Bulk Orders</span>
        <span @click="$router.push('/about')">About</span>
      </div>

      <!-- icons -->
      <div class="icons">
        <q-icon name="search" size="22px" class="icon" @click="searchOpen = true" />

        <div class="icon-box" @click="$router.push('/wishlist')">
          <q-icon name="favorite" size="22px" class="icon heart-icon" />
        </div>

        <div class="icon-box" @click="$router.push('/cart')">
          <q-icon name="shopping_cart" size="22px" class="icon" />
          <span v-if="totalCartCount > 0" class="count-badge">{{ totalCartCount }}</span>
        </div>

        <q-icon
          name="person_outline"
          size="22px"
          class="icon"
          @click="$router.push('/login')"
        />
      </div>
    </div>

    <!-- SEARCH OVERLAY -->
<div v-if="searchOpen" class="search-overlay" @click="searchOpen = false"></div>

<!-- SEARCH POPUP -->
<div v-if="searchOpen" class="search-popup">
  <div class="search-header">
    <input
      v-model="searchQuery"
      type="text"
      placeholder="Search products..."
      class="search-input"
    />
    <span class="search-close" @click="searchOpen = false">✕</span>
  </div>

  <div class="search-results">
    <div
      class="search-card"
      v-for="product in filteredProducts"
      :key="product.id"
      @click="goToProduct(product)"
    >
      <img :src="product.image" :alt="product.name" class="search-product-img" />
      <h4>{{ product.name }}</h4>
      <p>{{ product.category }}</p>
    </div>
  </div>
</div>

    <!-- MOBILE MENU OVERLAY -->
    <div v-if="menuOpen" class="mobile-menu-overlay" @click="menuOpen = false"></div>

    <!-- MOBILE SIDEBAR MENU -->
    <div class="mobile-sidebar" :class="{ open: menuOpen }">
      <div class="mobile-menu-header">
        <span class="menu-title">Menu</span>
        <span class="close-btn" @click="menuOpen = false">✕</span>
      </div>

      <div class="mobile-links">
        <span @click="goToPage('/')">Home</span>
        <span @click="goToPage('/men')">Men</span>
        <span @click="goToPage('/women')">Women</span>
        <span @click="goToPage('/bulk')">Bulk Orders</span>
        <span @click="goToPage('/about')">About</span>
      </div>
    </div>

    <!-- Main page area -->
    <q-page-container class="main-page-container">
      <!-- key forces clean re-render when route changes -->
      <router-view :key="$route.fullPath" />
    </q-page-container>
  </q-layout>

  
<!-- ---------------- FOOTER ---------------- -->
<footer class="footer-section">
  <div class="footer-container">
    
    <!-- Brand -->
    <div class="footer-col">
      <h2 class="footer-logo">PARALLEL</h2>
      <p class="footer-text">
        A Division of Pushpa Textile <br />
        Premium scrub wear crafted for comfort, style, and professionalism.
      </p>

    <div class="social-icons">
        <a href="https://www.instagram.com/" target="_blank" class="social-icon">
        <img src="/icons/instagram.png" alt="Instagram" class="social-img" />
        </a>

        <a href="https://www.facebook.com/" target="_blank" class="social-icon">
        <img src="/icons/facebook.png" alt="Instagram" class="social-img" />
        </a>

        <a href="https://wa.me/919876543210" target="_blank" class="social-icon">
        <img src="/icons/whatsapp.png" alt="Instagram" class="social-img" />
        </a>

    </div>
    </div>

    <!-- Quick Links -->
    <div class="footer-col">
      <h4>Quick Links</h4>
      <ul>
        <li @click="$router.push('/')">Home</li>
        <li @click="$router.push('/about')">About</li>
        <li @click="$router.push('/contact')">Contact</li>
        <li @click="$router.push('/wishlist')">Wishlist</li>
        <li @click="$router.push('/cart')">Cart</li>
        <li @click="$router.push('/bulk')">Bulk Orders</li>
      </ul>
    </div>

    <!-- Categories -->
    <div class="footer-col">
      <h4>Categories</h4>
      <ul>
        <li @click="$router.push('/men')">Men Scrubs</li>
        <li @click="$router.push('/women')">Women Scrubs</li>
        <li @click="$router.push('/bulk')">Bulk Orders</li>
      </ul>
    </div>

    <!-- Contact -->
    <div class="footer-col">
      <h4>Contact Us</h4>
      <p><q-icon name="location_on" size="18px" /> Solapur, Maharashtra</p>
      <p><q-icon name="call" size="18px" /> +91 98765 43210</p>
      <p><q-icon name="mail" size="18px" /> parallelwear@gmail.com</p>
    </div>
  </div>

  <!-- Bottom -->
  <div class="footer-bottom">
    <p>© 2026 PARALLEL. All Rights Reserved.</p>
  </div>
</footer>
</template>

<script setup>
import { computed, ref } from 'vue' // ref mobile menu sathi
import { useRouter } from 'vue-router' // route navigate sathi
import { cart } from 'src/stores/shop'

// only selected product count
const totalCartCount = computed(() => cart.value.length)

// mobile menu open/close state
const menuOpen = ref(false)

// router use karaycha
const router = useRouter()

// nav item click zalyavar page open + menu close
const goToPage = (path) => {
  router.push(path)
  menuOpen.value = false
}

// search popup open/close
const searchOpen = ref(false)

// search input value
const searchQuery = ref('')

// sample searchable products
const searchProducts = ref([
  {
    id: 1,
    name: 'Men Scrub',
    category: 'Classic Collection',
    image: "src/assets/scrub_suits_models/Parallel Scrub suits models/brown and light brown scrub suit men.png",
    route: '/men'
  },
  {
    id: 2,
    name: 'Classic Scrub',
    category: 'Premium Scrub',
    image: "src/assets/scrub_suits_models/Parallel Scrub suits models/Grey full sleeves zip scrub suit men.png",
    route: '/men'
  },
  {
    id: 3,
    name: 'Women Scrub',
    category: 'Elegant Fit',
    image: "src/assets/scrub_suits_models/Parallel Scrub suits models/V neck Dark green scrub suit women.png",
    route: '/women'
  },
  {
    id: 4,
    name: 'Womens Longsleeves Scrub',
    category: 'Classic Scrub',
    image: "src/assets/scrub_suits_models/Parallel Scrub suits models/Light yellow full sleeves scrub suit women.png",
    route: '/women'
  }
])

// search filter logic
const filteredProducts = computed(() => {
  if (!searchQuery.value.trim()) return searchProducts.value

  return searchProducts.value.filter((product) =>
    product.name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
    product.category.toLowerCase().includes(searchQuery.value.toLowerCase())
  )
})

// click product => page open + popup close
const goToProduct = (product) => {
  router.push(product.route)
  searchOpen.value = false
}

</script>

<style lang="scss">
@import 'src/css/navbar.scss';
</style>

<style lang="scss">
@import 'src/css/footer.scss';
</style>