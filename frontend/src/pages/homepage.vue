<template>
  <q-page>

    <Navbar />

    <HeroSection />

    <CategorySection />

    <!-- Featured Products -->
    <div class="q-pa-lg">
      <div class="row justify-between items-center">
        <h5>Featured Products</h5>
        <q-btn flat label="View All →" />
      </div>

      <div class="row q-col-gutter-md q-mt-md">
        <div class="col-3" v-for="p in products" :key="p.id">
          <ProductCard :product="p" />
        </div>
      </div>
    </div>

    <!-- Info Banner -->
    <div class="row q-pa-lg bg-grey-2">
      <div class="col-6 flex flex-center bg-primary text-white">
        <div>
          <h5>Trusted by Healthcare Professionals</h5>
          <p>Premium uniforms designed for comfort & durability</p>
          <q-btn label="Learn More" color="secondary" />
        </div>
      </div>
      <div class="col-6">
        <img src="https://via.placeholder.com/600x400" style="width:100%" />
      </div>
    </div>

    <!-- Testimonials -->
    <div class="q-pa-xl text-center bg-teal text-white">
      <h5>What Our Customers Say</h5>

      <q-card class="q-mt-lg q-pa-md" style="max-width:500px;margin:auto;">
        <p>"Best medical wear quality!"</p>
        <strong>Dr. XYZ</strong>
      </q-card>
    </div>

    <!-- Bulk Order -->
    <div class="q-pa-xl flex flex-center">
      <q-card class="q-pa-lg bg-dark text-white" style="width:600px;">
        <h6>Bulk Orders for Hospitals & Clinics</h6>
        <p>Get premium quality uniforms in bulk</p>
        <q-btn label="Request Quote" color="warning" />
      </q-card>
    </div>

    <FooterSection />

  </q-page>
</template>

<script>
import Navbar from 'components/Navbar.vue'
import HeroSection from 'components/HeroSection.vue'
import CategorySection from 'components/CategorySection.vue'
import ProductCard from 'components/ProductCard.vue'
import FooterSection from 'components/FooterSection.vue'

export default {
  components: {
    Navbar,
    HeroSection,
    CategorySection,
    ProductCard,
    FooterSection
  },
  data() {
    return {
      products: [
        { id: 1, name: 'Scrubs Set', price: 999 },
        { id: 2, name: 'Lab Coat', price: 1299 },
        { id: 3, name: 'Nurse Uniform', price: 899 },
        { id: 4, name: 'Surgical Scrub', price: 1099 }
      ]
    }
  }
}
</script>