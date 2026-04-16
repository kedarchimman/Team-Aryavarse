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
        <!--<span @click="goToPage('/aprons')">Aprons</span>--->
        <span @click="$router.push('/bulk')">Bulk Orders</span>
        <span @click="$router.push('/about')">About Us</span>
        
      </div>

      <!-- icons -->
      <div class="icons">
        <q-icon name="search" size="22px" class="icon" @click="searchOpen = true" />

        <div class="icon-box" @click="$router.push('/wishlist')">
          <q-icon name="favorite" size="22px" class="icon heart-icon" />
        </div>

        <div class="icon-box cart-icon" id="cartIcon" @click="$router.push('/cart')">
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

      <!-- DROPDOWN (ONLY HERE) -->
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

      <!-- NO RESULT -->
      <div v-if="searchQuery && !suggestions.length" class="no-result">
        No product found
      </div>

    </div>

    

    <span class="search-close" @click="searchOpen = false">✕</span>
  </div>

  <!-- RECENT SEARCHES -->
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
        <span @click="goToPage('/Aprons')">Aprons</span>
        <span @click="goToPage('/bulk')">Bulk Orders</span>
        <span @click="goToPage('/about')">About Us</span>
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

        <a  href="https://www.linkedin.com/company/two-elephants-technologies-llp/" 
        target="_blank" class="social-icon">
        <img src="/icons/linkdin.png" alt="Instagram" class="social-img" />
        </a>

    </div>
    </div>

    <!-- Quick Links -->
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

    <!-- Categories -->
    <div class="footer-col">
      <h4>Categories</h4>
      <ul>
        <li @click="$router.push('/men')">Men Scrubs</li>
        <li @click="$router.push('/women')">Women Scrubs</li>
        <li @click="$router.push('/aprons')">Aprons</li>
      </ul>
    </div>

    <!-- Contact -->
    <div class="footer-col">
      <h4>Contact Us</h4>
      <p><q-icon name="location_on" size="18px" /> Solapur, Maharashtra</p>
      <p><q-icon name="call" size="18px" /> +91 98765 43210</p>
      <p><q-icon name="mail" size="18px" />
      <a href="https://mail.google.com/mail/?view=cm&fs=1&to=info@twoelephants.org" 
      target="_blank"
      rel="noopener noreferrer"
      class="footer-email"
      >
      info@twoelephants.org
      </a>
      </p>
    </div>
  </div>

  <!-- Bottom -->
  <div class="footer-bottom">
    <p>© 2026 PARALLEL. All Rights Reserved.</p>
  </div>
</footer>
</template>

<script setup>
import { computed, ref, watch } from 'vue' // ref mobile menu sathi
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
const searchProducts = ref([])

//recent Searches
const recentSearches = ref([])
const addToRecent = (text) => {
  const q = text.trim().toLowerCase()

  if (!q) return

  recentSearches.value = [
    q,
    ...recentSearches.value.filter(i => i !== q)
  ].slice(0, 6)
}

const searchMap = [
  { key: 'apron', route: '/aprons' },
  { key: 'aprons', route: '/aprons' },
  { key: 'women scrub', route: '/women' },
  { key: 'men scrub', route: '/men' },
  { key: 'scrub', route: '/women' },
  { key: 'bulk', route: '/bulk' },
]

const goSearch = () => {
  const q = searchQuery.value.toLowerCase().trim()

  if (!q) return

  const match = searchMap.find(item =>
    q.includes(item.key)
  )

  if (match) {
    router.push(match.route)
    searchOpen.value = false
    searchQuery.value = ''
  }
}
watch(searchQuery, () => {
  goSearch()
})

//suggestions search 
const suggestions = computed(() => {
  const q = searchQuery.value.toLowerCase().trim()

  if (!q) return []

  return searchIndex.filter(item =>
    item.keywords.some(k =>
      k.includes(q) || q.includes(k)
    )
  )
})


//search index 
const searchIndex = [
  {
    keywords: ['men', 'men scrub', 'male scrub', 'mens scrubs'],
    route: '/men',
    label: 'Men Scrubs'
  },
  {
    keywords: ['women', 'women scrub', 'female scrub', 'womens scrubs'],
    route: '/women',
    label: 'Women Scrubs'
  },

  // COLORS + STYLE SMART MATCH
  {
    keywords: ['blue scrub', 'blue v neck', 'v neck blue scrub', 'blue v neck scrub'],
    route: '/men?color=blue&type=vneck',
    label: 'Blue V Neck Scrub'
  },

  {
    keywords: ['red scrub', 'red v neck'],
    route: '/women?color=red&type=vneck',
    label: 'Red Scrub'
  }
]

// click behaviour 
const goToResult = (item) => {
  addToRecent(item.label)   // ✅ ADD THIS

  router.push(item.route)
  searchOpen.value = false
  searchQuery.value = ''
}

//AUTO DIRECT (ENTER PRESS LOGIC)
const handleSearchEnter = () => {
  const q = searchQuery.value.toLowerCase().trim()

  if (!q) return

  addToRecent(q)

  const match = searchIndex.find(item =>
    item.keywords.some(k => k === q)
  )

  if (match) {
    router.push(match.route)
  } else {
    router.push(`/search?q=${q}`) // fallback page
  }

  searchOpen.value = false
}

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