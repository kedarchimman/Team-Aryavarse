<template>
  <div v-if="product" class="aprons-product-page">
    <div class="product-page">

      <!-- LEFT: thumbs + main image -->
      <div class="left-wrap">
        <div class="left">
          <!-- thumbnails -->
          <div class="thumbs">
            <img
              v-for="img in product.images"
              :key="img"
              :src="img"
              :class="{ active: selectedImage === img }"
              @click="selectedImage = img"
            />
          </div>

          <!-- main image -->
          <div class="main-image-box" @click="openImageDialog">
            <img :src="selectedImage" class="main-image" />
            <!---<div class="zoom-icon">
              <i class="bi bi-zoom-in"></i>
            </div>--->
          </div>
        </div>
      </div>

      <!-- RIGHT: details -->
      <div class="right">
        <p class="tag">Premium Aprons Collection</p>
        <h1>{{ product.title }}</h1>

        <div class="rating-row">
          <span class="stars">★★★★★</span>
          <span class="rating-val">{{ product.rating }}</span>
          <span class="review-count">(602 Reviews)</span>
        </div>

        <div class="price-row">
          <h2>
            ₹ {{ Number(product.price).toLocaleString('en-IN', { minimumFractionDigits: 2 }) }}
          </h2>
          <span class="old-price">
            ₹ {{ Number(oldPrice).toLocaleString('en-IN', { minimumFractionDigits: 2 }) }}
          </span>
          <span class="discount">20% OFF</span>
        </div>

        <!-- COLOUR -->
        <!-----<div class="variant-section">
          <p class="variant-label">Colour: <strong>{{ selectedColor }}</strong></p>
          <div class="color-swatches">
            <button
              v-for="c in colorOptions" :key="c.name"
              class="color-dot"
              :class="{ active: selectedColor === c.name }"
              :style="{ background: c.hex }"
              :title="c.name"
              @click="changeColor(c.name)"
            ></button>
          </div>
        </div>---->

        <!-- SIZE SECTION -->
        <div class="variant-section">
          <div class="section-head">
            <p class="variant-label">
              Size: <strong>{{ selectedSize }}</strong>
            </p>
            <button class="size-chart-link" @click="sizeChartDialog = true">
              Size Chart
            </button>
          </div>

          <div class="size-options">
            <button
              v-for="s in sizes" :key="s"
              class="size-btn"
              :class="{ active: selectedSize === s }"
              @click="selectedSize = s"
            >
              {{ s }}
            </button>
          </div>
        </div>

        <!-- BUTTONS -->
        <div class="btns">
          <button class="cart-btn" @click="handleAddToCart">Add to Cart</button>
          <button class="buy-btn" @click="handleBuyNow">Buy Now</button>
        </div>

        <!-- Delivery features -->
        <div class="delivery-cols">
          <div class="delivery-col">
            <i class="bi bi-truck-flatbed"></i>
            <p class="delivery-title">1–3 Day<br />Express Shipping</p>
          </div>
          <div class="delivery-col">
            <i class="bi bi-box-seam"></i>
            <p class="delivery-title">Easy Exchange<br />&amp; Returns</p>
          </div>
          <div class="delivery-col">
            <i class="bi bi-truck"></i>
            <p class="delivery-title">Cash on Delivery<br />Available</p>
          </div>
        </div>

        <!-- pin code section -->
        <div class="section delivery-details">
          <h3>Delivery Details</h3>

          <div class="pincode-checker">
            <div class="input-btn-group">
              <q-input
                v-model="pincode"
                type="number"
                dense
                class="pincode-input"
                placeholder="Enter pincode"
                :hide-bottom-space="true"
              />
              <q-btn
                class="check-btn"
                :loading="isChecking"
                :disable="isChecking"
                label="Check"
                @click="checkPincode"
              />
            </div>

            <div v-if="pincodeError" class="error-msg">
              {{ pincodeError }}
            </div>

            <div v-if="deliveryStatus" class="delivery-messages">
              <div class="delivery-date">
                <i class="bi bi-truck"></i>
                {{ deliveryStatus.deliveryDate }}
              </div>
              <div class="delivery-cod" v-if="deliveryStatus.cod">
                <i class="bi bi-cash-stack"></i>
                {{ deliveryStatus.cod }}
              </div>
            </div>
          </div>
        </div>

        <!-- details -->
        <div class="product-info-right">

          <!-- Details & Fit -->
          <div class="section accordion">
            <div class="accordion-header" @click="activeAccordion = activeAccordion === 0 ? null : 0">
              <span>Details &amp; Fit</span>
              <q-icon :name="activeAccordion === 0 ? 'remove' : 'add'" />
            </div>
            <div v-show="activeAccordion === 0" class="accordion-content">
              <p>
                These premium aprons are built for performance and crafted for style.<br>
              </p>
              <ul>
                <li>Adjustable neck and waist straps for the perfect fit.</li>
                <li>Roomy pockets for all essentials.</li>
                <li>Durable and easy to clean material.</li>
                <li>Loop ring to hold your ID badge.</li>
                <li>Professional look for everyday use.</li>
                <li>Classic, practical, and always professional.</li>
              </ul>
            </div>
          </div>

          <!-- Fabric & Care -->
          <div class="section accordion">
            <div class="accordion-header" @click="activeAccordion = activeAccordion === 1 ? null : 1">
              <span>Fabric &amp; Care</span>
              <q-icon :name="activeAccordion === 1 ? 'remove' : 'add'" />
            </div>
            <div v-show="activeAccordion === 1" class="accordion-content">
              <p>Engineered with our proprietary fabric, these aprons are designed to keep every shift comfortable and effortless.</p>
              <ul>
                <li>75% Poly</li>
                <li>25% Viscose</li>
                <li>Wash inside out with like colors in 40°C water.</li>
                <li>Do not bleach and only tumble dry.</li>
              </ul>
            </div>
          </div>

          <!-- Return & Exchange -->
          <div class="section accordion">
            <div class="accordion-header" @click="activeAccordion = activeAccordion === 2 ? null : 2">
              <span>Return &amp; Exchange</span>
              <q-icon :name="activeAccordion === 2 ? 'remove' : 'add'" />
            </div>
            <div v-show="activeAccordion === 2" class="accordion-content">
              <p>We want you to love your aprons. If something isn't right, you can request a return or exchange within 7 days of delivery for all non-customised orders.</p>
              <p><strong>Please note:</strong></p>
              <ul>
                <li>Embroidery products are not eligible for return or exchange.</li>
                <li>Items that have been used, washed, or had their tags removed cannot be returned.</li>
                <li>Orders placed during sale events are final and not eligible for return and can be exchanged.</li>
              </ul>
            </div>
          </div>
        </div>

      </div>
    </div>

    <!-- IMAGE DIALOG -->
    <div v-if="imageDialog" class="image-popup" @click.self="imageDialog = false">
      <button class="full-close-btn" @click="imageDialog = false">✕</button>
      <img :src="selectedImage" class="popup-image" />
    </div>

    <!-- SIZE CHART POPUP -->
    <q-dialog v-model="sizeChartDialog">
      <div class="size-chart-popup">
        <!-- HEADER -->
        <div class="size-chart-header">
          <h3>Size Chart</h3>
          <button class="size-chart-close" @click="sizeChartDialog = false">✕</button>
        </div>

        <!-- TABS -->
        <div class="size-chart-tabs">
          <button
            class="tab"
            :class="{ active: activeTab === 'size' }"
            @click="activeTab = 'size'"
          >
            Size
          </button>
          <button
            class="tab"
            :class="{ active: activeTab === 'measure' }"
            @click="activeTab = 'measure'"
          >
            How to Measure
          </button>
        </div>

        <!-- CONTENT -->
        <div class="size-chart-content">
          <img
            v-if="activeTab === 'size'"
            :src="sizeChartImg"
            class="size-chart-img"
          />
          <img
            v-else
            :src="measureImg"
            class="size-chart-img"
          />
        </div>
      </div>
    </q-dialog>

  </div>
</template>

<script setup>
import { computed, ref, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { apronsProducts } from 'src/data/apronsProducts'
import { addToCart, toggleWishlist, isInWishlist } from 'src/stores/shop'
//import sizeChartImg from 'src/assets/size_chart/size-chart.png'
//import measureImg from 'src/assets/size_chart/measure.png'

//image show on different product 
const sizeChartImg = computed(() => product.value?.sizeChart)
const measureImg   = computed(() => product.value?.measureChart)

// accordion
const activeAccordion = ref(null)

const route  = useRoute()
const router = useRouter()

const product = computed(() => apronsProducts.find(p => p.id === Number(route.params.id)))

// Images
const selectedImage = ref('')
const imageDialog   = ref(false)

watch(product, val => {
  if (val) selectedImage.value = val.images[0]
}, { immediate: true })

const openImageDialog = () => {
  imageDialog.value = true
}

const prevImage = () => {
  const imgs = product.value.images
  selectedImage.value = imgs[(imgs.indexOf(selectedImage.value) - 1 + imgs.length) % imgs.length]
}
const nextImage = () => {
  const imgs = product.value.images
  selectedImage.value = imgs[(imgs.indexOf(selectedImage.value) + 1) % imgs.length]
}

const oldPrice = computed(() => product.value ? Number(product.value.price) + 300 : 0)

// SIZE
const sizes = ['S','M','L','XL','2XL']
const selectedSize = ref('M')

// popup
const sizeChartDialog = ref(false)
const activeTab = ref('size')

// pin code
const pincode = ref('')
const deliveryStatus = ref(null)
const pincodeError = ref('')
const isChecking = ref(false)

const solapurPincodes = [
  '413001','413002','413003','413004','413005',
  '413006','413007','413101','413109','413112',
  '413203','413212','413214','413215','413216',
  '413219','413221','413222','413228','413253',
  '413301','413303','413304','413305','413306',
  '413307','413309','413310','413311','413314',
  '413401','413402','413403','413406','413409',
  '413410','413411'
]

const checkPincode = () => {
  const pin = pincode.value.trim()
  deliveryStatus.value = null
  pincodeError.value = ''

  if (!pin) {
    pincodeError.value = 'Please enter a valid pincode'
    return
  }

  isChecking.value = true

  setTimeout(() => {
    if (solapurPincodes.includes(pin)) {
      deliveryStatus.value = {
        deliveryDate: 'Delivery between 11th and 12th Apr',
        cod: 'Cash on delivery available'
      }
    } else {
      deliveryStatus.value = null
      pincodeError.value = 'Sorry, delivery not available for this pincode'
    }
    isChecking.value = false
  }, 1200)
}

// Cart
const handleAddToCart = () => {
  addToCart({
    ...product.value,
    size: selectedSize.value,
  })
}

const handleBuyNow = () => {
  handleAddToCart()
  router.push('/cart')
}
</script>

<style lang="scss">
@import 'src/css/aprons-product-details.scss';
</style>