<template>
  <q-page class="wishlist-page">
    <div class="wishlist-container">
      <h1 class="wishlist-heading">My Wishlist</h1>

      <div class="wishlist-layout">
        <!-- LEFT SIDE -->
        <div class="wishlist-left">
          <div v-if="wishlist.length > 0">
            <div
              v-for="item in wishlist"
              :key="item.id"
              class="wishlist-card"
            >
              <!-- image -->
              <img :src="item.image" :alt="item.title" class="wishlist-img" />

              <!-- details -->
              <div class="wishlist-info">
                <h3 class="product-title">{{ item.title }}</h3>
                <p class="product-meta">
                  Size: {{ item.size || 'M' }}
                  <span class="dot">•</span>
                  Color: {{ item.color || 'Default' }}
                </p>

                <div class="wishlist-btns">
                  <button class="cart-btn" @click="addToCart(item)">
                    Add to Cart
                  </button>
                  <button class="remove-btn" @click="removeFromWishlist(item.id)">
                    Remove
                  </button>
                </div>
              </div>

              <!-- price -->
              <div class="price-box">
                ₹{{ item.price.toLocaleString() }}
              </div>
            </div>
          </div>

          <!-- empty wishlist -->
          <div v-else class="empty-wishlist">
            <h3>Your wishlist is empty</h3>
            <p>Save your favorite products here.</p>
            <button class="continue-btn" @click="$router.push('/')">
              Continue Shopping
            </button>
          </div>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script setup>
import { wishlist, addToCart, removeFromWishlist } from 'src/stores/shop'
</script>

<style lang="scss">
@import 'src/css/wishlist.scss';
</style>