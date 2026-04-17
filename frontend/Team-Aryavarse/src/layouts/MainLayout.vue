<template>
  <q-layout view="lHh Lpr lFf">
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
        <span @click="$router.push('/about')">About Us</span>
      </div>

      <!-- icons -->
      <div class="icons">
        <q-icon name="search" size="22px" class="icon" @click="searchOpen = true" />

        <div class="icon-box" @click="$router.push('/wishlist')">
          <q-icon name="favorite" size="22px" class="icon heart-icon" />
        </div>

        <div class="icon-box cart-icon" @click="$router.push('/cart')">
          <q-icon name="shopping_cart" size="22px" class="icon" />
          <span v-if="totalCartCount > 0" class="count-badge">{{ totalCartCount }}</span>
        </div>

        <!-- ✅ AUTH LOGIC MERGED -->
        <template v-if="isLoggedIn">
          <q-icon
            name="person"
            size="22px"
            class="icon"
            @click="$router.push('/profile')"
          />
          <span class="logout-btn" @click="handleLogout">Logout</span>
        </template>

        <template v-else>
          <q-icon
            name="person_outline"
            size="22px"
            class="icon"
            @click="$router.push('/login')"
          />
        </template>
      </div>
    </div>

    <!-- SEARCH OVERLAY -->
    <div v-if="searchOpen" class="search-popup">
      <div class="search-header">
        <div class="search-input-wrapper">
          <input
            v-model="searchQuery"
            @keyup.enter="handleSearchEnter"
            type="text"
            placeholder="Search scrubs, aprons..."
            class="search-input"
          />

          <div v-if="suggestions.length" class="dropdown">
            <div
              v-for="item in suggestions"
              :key="item.route"
              class="item"
              @click="goToResult(item)"
            >
              {{ item.label }}
            </div>
          </div>

          <div v-if="searchQuery && !suggestions.length" class="no-result">
            No product found
          </div>
        </div>

        <span class="search-close" @click="searchOpen = false">✕</span>
      </div>

      <div v-if="recentSearches.length" class="recent-box">
        <div class="recent-title">Recent Searches</div>

        <div class="recent-list">
          <span
            v-for="item in recentSearches"
            :key="item"
            class="recent-chip"
            @click="searchQuery = item"
          >
            {{ item }}
          </span>
        </div>
      </div>
    </div>

    <!-- MOBILE MENU -->
    <div v-if="menuOpen" class="mobile-menu-overlay" @click="menuOpen = false"></div>

    <div class="mobile-sidebar" :class="{ open: menuOpen }">
      <div class="mobile-menu-header">
        <span class="menu-title">Menu</span>
        <span class="close-btn" @click="menuOpen = false">✕</span>
      </div>

      <div class="mobile-links">
        <span @click="goToPage('/')">Home</span>
        <span @click="goToPage('/men')">Men</span>
        <span @click="goToPage('/women')">Women</span>
        <span @click="goToPage('/aprons')">Aprons</span>
        <span @click="goToPage('/bulk')">Bulk Orders</span>
        <span @click="goToPage('/about')">About Us</span>
      </div>
    </div>

    <!-- MAIN -->
    <q-page-container class="main-page-container">
      <router-view :key="$route.fullPath" />
    </q-page-container>

    <!-- FOOTER -->
    <footer class="footer-section">
      <div class="footer-container">
        <div class="footer-col">
          <h2 class="footer-logo">PARALLEL</h2>
          <p class="footer-text">
            A Division of Pushpa Textile <br />
            Premium scrub wear crafted for comfort, style, and professionalism.
          </p>
        </div>

        <div class="footer-col">
          <h4>Quick Links</h4>
          <ul>
            <li @click="$router.push('/')">Home</li>
            <li @click="$router.push('/bulk')">Bulk Orders</li>
            <li @click="$router.push('/about')">About Us</li>
            <li @click="$router.push('/wishlist')">Wishlist</li>
            <li @click="$router.push('/cart')">Cart</li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Categories</h4>
          <ul>
            <li @click="$router.push('/men')">Men Scrubs</li>
            <li @click="$router.push('/women')">Women Scrubs</li>
            <li @click="$router.push('/aprons')">Aprons</li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Contact Us</h4>
          <p><q-icon name="location_on" size="18px" /> Solapur, Maharashtra</p>
          <p><q-icon name="call" size="18px" /> +91 98765 43210</p>
          <p><q-icon name="mail" size="18px" /> info@twoelephants.org</p>
        </div>
      </div>

      <div class="footer-bottom">
        <p>© 2026 PARALLEL. All Rights Reserved.</p>
      </div>
    </footer>
  </q-layout>
</template>

<script setup>
import { computed, ref, watch } from 'vue'
import { useRouter } from 'vue-router'
import { cart } from 'src/stores/shop'
import { useAuthStore } from 'src/stores/auth' // ✅ added

const router = useRouter()
const authStore = useAuthStore()

// ✅ AUTH STATE
const isLoggedIn = computed(() => authStore.isLoggedIn)

function handleLogout() {
  authStore.logout()
  router.push('/login')
}

// CART
const totalCartCount = computed(() => cart.value.length)

// MOBILE MENU
const menuOpen = ref(false)
const goToPage = (path) => {
  router.push(path)
  menuOpen.value = false
}

// SEARCH
const searchOpen = ref(false)
const searchQuery = ref('')
const recentSearches = ref([])

const addToRecent = (text) => {
  const q = text.trim().toLowerCase()
  if (!q) return

  recentSearches.value = [
    q,
    ...recentSearches.value.filter(i => i !== q)
  ].slice(0, 6)
}

// SEARCH INDEX
const searchIndex = [
  { keywords: ['men'], route: '/men', label: 'Men Scrubs' },
  { keywords: ['women'], route: '/women', label: 'Women Scrubs' },
]

// SUGGESTIONS
const suggestions = computed(() => {
  const q = searchQuery.value.toLowerCase().trim()
  if (!q) return []

  return searchIndex.filter(item =>
    item.keywords.some(k => k.includes(q) || q.includes(k))
  )
})

const goToResult = (item) => {
  addToRecent(item.label)
  router.push(item.route)
  searchOpen.value = false
  searchQuery.value = ''
}

const handleSearchEnter = () => {
  const q = searchQuery.value.toLowerCase().trim()
  if (!q) return

  addToRecent(q)

  const match = searchIndex.find(item =>
    item.keywords.includes(q)
  )

  if (match) {
    router.push(match.route)
  } else {
    router.push(`/search?q=${q}`)
  }

  searchOpen.value = false
}
</script>

<style lang="scss">
@import 'src/css/navbar.scss';
@import 'src/css/footer.scss';

.logout-btn {
  cursor: pointer;
  font-size: 14px;
  margin-left: 8px;
  color: #ff4444;

  &:hover {
    text-decoration: underline;
  }
}
</style>