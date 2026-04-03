<template>
  <q-layout>
    <div class="navbar">

      <!-- logo -->
      <div class="logo" @click="$router.push('/')">
        Parallel
      </div>

      <!-- links -->
      <div class="links">
        <span @click="$router.push('/')">Home</span>
        <span @click="$router.push('/men')">Men</span>
        <span @click="$router.push('/women')">Women</span>
        <span @click="$router.push('/bulk')">Bulk Orders</span>
        <span @click="$router.push('/about')">About</span>
        <span @click="$router.push('/contact')">Contact</span>
      </div>

      <!-- icons -->
      <div class="icons">
        <q-icon name="search" size="22px" class="icon" />

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

    <q-page-container>
      <router-view />
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

      <!---<div class="social-icons">
        <q-icon name="fab fa-instagram" size="20px" class="social-icon" />
        <q-icon name="fab fa-facebook-f" size="20px" class="social-icon" />
        <q-icon name="fab fa-whatsapp" size="20px" class="social-icon" />
        <q-icon name="fab fa-linkedin-in" size="20px" class="social-icon" />
      </div>--->
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
import { computed } from 'vue'
import { cart } from 'src/stores/shop'

// only selected product count
const totalCartCount = computed(() => cart.value.length)
</script>

<style lang="scss">
@import 'src/css/navbar.scss';
</style>

<style lang="scss">
@import 'src/css/footer.scss';
</style>