<template>
  <div class="new-page">
    <ProductSection :products="newProducts" />
  </div>
</template>

<script setup>
import ProductSection from 'src/components/ProductSection.vue'
import { products } from 'src/data/products'

const newProducts = products.filter(item => item.isNew === true)
</script>