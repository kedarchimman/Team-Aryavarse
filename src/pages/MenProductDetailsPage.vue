<template>
  <div v-if="product" class="men-product-page">
    <div class="product-page">

      <!-- ===== LEFT — thumbs LEFT, big image RIGHT ===== -->
      <div class="left-wrap">
        <div class="left">

          <!-- Vertical thumbnails on the LEFT -->
          <div class="thumbs">
            <img
              v-for="img in product.images"
              :key="img"
              :src="img"
              :class="{ active: selectedImage === img }"
              @click="selectedImage = img"
            />
          </div>

          <!-- Main image RIGHT side of thumbs — STICKY, does not scroll -->
          <div class="main-image-box" @click="openImageDialog">
            <img :src="selectedImage" class="main-image" />
          </div>

        </div>
      </div>

      <!-- ===== RIGHT DETAILS (scrolls normally) ===== -->
      <div class="right">

        <p class="tag">Premium Men Collection</p>
        <h1>{{ product.title }}</h1>

        <div class="rating-row">
          <span class="stars">★★★★★</span>
          <span class="rating-val">{{ product.rating }}</span>
          <span class="review-count">(602 Reviews)</span>
        </div>

        <div class="price-row">
          <h2>₹{{ product.price }}</h2>
          <span class="old-price">₹{{ oldPrice }}</span>
          <span class="discount">20% OFF</span>
        </div>

        <!-- COLOUR -->
        <div class="variant-section">
          <p class="variant-label">Colour: <strong>{{ selectedColor }}</strong></p>
          <div class="color-swatches">
            <button
              v-for="c in colorOptions" :key="c.name"
              class="color-dot"
              :class="{ active: selectedColor === c.name }"
              :style="{ background: c.hex }"
              :title="c.name"
              @click="selectedColor = c.name"
            ></button>
          </div>
        </div>

        <!-- TOP SIZE -->
        <div class="variant-section">
          <div class="section-head">
            <p class="variant-label">Top Size:</p>
            <button class="size-chart-link" @click="sizeChartDialog = true">Size Chart</button>
          </div>
          <div class="size-options">
            <button
              v-for="sz in sizes" :key="'top-'+sz"
              class="size-btn" :class="{ active: selectedTopSize === sz }"
              @click="selectedTopSize = sz"
            >{{ sz }}</button>
          </div>
        </div>

        <!-- BOTTOM SIZE -->
        <div class="variant-section">
          <div class="section-head">
            <p class="variant-label">Bottom Size:</p>
            <button class="size-chart-link" @click="sizeChartDialog = true">Size Chart</button>
          </div>
          <div class="size-options">
            <button
              v-for="sz in sizes" :key="'bot-'+sz"
              class="size-btn" :class="{ active: selectedBottomSize === sz }"
              @click="selectedBottomSize = sz"
            >{{ sz }}</button>
          </div>
        </div>

        <!-- BOTTOM STYLE -->
        <div class="variant-section">
          <p class="variant-label">Bottom Style:</p>
          <div class="style-options">
            <button
              v-for="st in bottomStyles" :key="st"
              class="style-btn" :class="{ active: selectedBottomStyle === st }"
              @click="selectedBottomStyle = st"
            >{{ st }}</button>
          </div>
        </div>

        <!-- EMBROIDERY BANNER -->
        <div class="embroidery-banner">
          <span class="emb-icon">✏️</span>
          <div>
            <p class="emb-title">Custom Embroidery</p>
            <p class="emb-sub">Starting at ₹250 personalise your scrubs</p>
          </div>
        </div>

        <!-- ADD TO CART / BUY NOW -->
        <div class="btns">
          <button class="cart-btn" @click="handleAddToCart">Add to Cart</button>
          <button class="buy-btn" @click="handleBuyNow">Buy Now</button>
          <button
            class="wish-btn" :class="{ active: isInWishlist(product.id) }"
            @click="toggleWishlist(product)"
          >{{ isInWishlist(product.id) ? '♥ Wishlisted' : '♡ Wishlist' }}</button>
        </div>

        <!-- DELIVERY DETAILS -->
        <div class="delivery-section">
          <h3 class="del-title">Delivery Details</h3>
          <div class="pincode-row">
            <input
              v-model="pincode"
              type="text"
              maxlength="6"
              placeholder="Enter Pincode"
              class="pincode-input"
              @keyup.enter="checkDelivery"
            />
            <button class="pincode-btn" @click="checkDelivery">Check</button>
          </div>
          <div v-if="deliveryResult" class="delivery-result">
            <p class="del-date">
              <span>🚚</span>
              Delivery between
              <strong>{{ deliveryResult.from }}</strong> and
              <strong>{{ deliveryResult.to }}</strong>
            </p>
            <p class="cod-row">
              <span>💵</span>
              Cash on delivery
              <strong :class="deliveryResult.cod ? 'green' : 'red'">
                {{ deliveryResult.cod ? 'available' : 'not available' }}
              </strong>
            </p>
          </div>
          <p v-if="deliveryError" class="del-error">{{ deliveryError }}</p>
        </div>

        <!-- ACCORDION -->
        <div class="accordion-block">
          <div class="accordion-item" v-for="(acc, i) in accordions" :key="i">
            <button class="accordion-head" @click="acc.open = !acc.open">
              <span>{{ acc.title }}</span>
              <span class="acc-icon">{{ acc.open ? '−' : '+' }}</span>
            </button>
            <div class="accordion-body" :class="{ open: acc.open }">
              <ul v-if="acc.list">
                <li v-for="item in acc.list" :key="item">{{ item }}</li>
              </ul>
              <p v-else>{{ acc.text }}</p>
            </div>
          </div>
        </div>

      </div>
    </div>

    <!-- ============================================================
         FULL IMAGE DIALOG
         Screenshot 3: thumbs on LEFT, big image on RIGHT
         ============================================================ -->
    <q-dialog v-model="imageDialog" maximized>
      <div class="full-image-viewer" @click.self="imageDialog = false">

        <button class="full-close-btn" @click="imageDialog = false">✕</button>

        <!-- Thumbs on LEFT -->
        <div class="full-thumbs">
          <img
            v-for="img in product.images"
            :key="'fp-'+img"
            :src="img"
            :class="{ active: selectedImage === img }"
            @click="selectedImage = img"
          />
        </div>

        <!-- Big image on RIGHT -->
        <div class="full-main-image-wrap">
          <button class="img-nav prev" @click="prevImage">&#8249;</button>
          <img :src="selectedImage" class="full-main-image" :key="selectedImage" />
          <button class="img-nav next" @click="nextImage">&#8250;</button>
        </div>

      </div>
    </q-dialog>

    <!-- ============================================================
         SIZE CHART MODAL
         Screenshot 1: Both Top + Bottom tables in ONE modal (scrollable)
         Screenshot 2: How to Measure — steps LEFT, body figure RIGHT
         ============================================================ -->
    <q-dialog v-model="sizeChartDialog">
      <div class="size-chart-modal">

        <div class="modal-header">
          <h2>Size Chart</h2>
          <button class="modal-close" @click="sizeChartDialog = false">✕</button>
        </div>

        <div class="chart-tabs">
          <button class="tab-btn" :class="{ active: activeTab === 'chart' }" @click="activeTab = 'chart'">
            Size Chart
          </button>
          <button class="tab-btn" :class="{ active: activeTab === 'measure' }" @click="activeTab = 'measure'">
            How to Measure?
          </button>
        </div>

        <!-- ---- SIZE CHART TAB ---- -->
        <div v-if="activeTab === 'chart'" class="chart-tab-content">

          <div class="unit-toggle-wrap">
            <span :class="{ activeUnit: unit === 'IN' }">IN</span>
            <button class="toggle-switch" @click="toggleUnit">
              <span :class="{ moved: unit === 'CM' }"></span>
            </button>
            <span :class="{ activeUnit: unit === 'CM' }">CM</span>
          </div>

          <div class="chart-scroll">

            <!-- TOP TABLE -->
            <div class="chart-section">
              <h4>Mens Scrub Suit Top</h4>
              <div class="table-wrap">
                <table>
                  <thead>
                    <tr>
                      <th>Size</th>
                      <th>Chest</th>
                      <th>Shoulder</th>
                      <th>Length</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr
                      v-for="item in displayedTopChart"
                      :key="'t-'+item.size"
                      :class="{ 'highlight-row': selectedTopSize === item.size }"
                    >
                      <td><strong>{{ item.size }}</strong></td>
                      <td>{{ item.chest }}</td>
                      <td>{{ item.shoulder }}</td>
                      <td>{{ item.length }}</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            <!-- BOTTOM TABLE (same modal, below top) -->
            <div class="chart-section">
              <h4>Mens Scrub Suit Bottom</h4>
              <div class="table-wrap">
                <table>
                  <thead>
                    <tr>
                      <th>Size</th>
                      <th>Waist</th>
                      <th>Hip</th>
                      <th>Length</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr
                      v-for="item in displayedBottomChart"
                      :key="'b-'+item.size"
                      :class="{ 'highlight-row': selectedBottomSize === item.size }"
                    >
                      <td><strong>{{ item.size }}</strong></td>
                      <td>{{ item.waist }}</td>
                      <td>{{ item.hip }}</td>
                      <td>{{ item.length }}</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            <p class="chart-note">*All the measurements are body measurements and not garment measurements.</p>

          </div><!-- /chart-scroll -->
        </div>

        <!-- ---- HOW TO MEASURE TAB ---- -->
        <!-- Steps LEFT + Body figure RIGHT (like knya screenshot 2) -->
        <div v-else class="measure-tab-content">
          <div class="measure-layout">

            <!-- Steps on LEFT -->
            <div class="measure-steps">
              <div class="measure-card" v-for="(m, i) in measurements" :key="i">
                <span class="measure-number">{{ i + 1 }}</span>
                <div>
                  <h4>{{ m.title }}</h4>
                  <p>{{ m.desc }}</p>
                </div>
              </div>
            </div>

            <!-- Body silhouette on RIGHT (like knya image 2) -->
            <div class="body-figure">
              <svg viewBox="0 0 180 400" xmlns="http://www.w3.org/2000/svg">
                <!-- head -->
                <ellipse cx="90" cy="30" rx="24" ry="28" fill="#3a1f6e"/>
                <!-- neck -->
                <rect x="82" y="55" width="16" height="14" rx="4" fill="#3a1f6e"/>
                <!-- torso -->
                <path d="M52 70 Q34 82 30 130 L34 195 L146 195 L150 130 Q146 82 128 70 Q112 62 90 62 Q68 62 52 70Z" fill="#3a1f6e"/>
                <!-- left arm -->
                <path d="M52 74 Q22 94 18 160 Q22 178 38 175 Q50 155 50 120Z" fill="#3a1f6e"/>
                <!-- right arm -->
                <path d="M128 74 Q158 94 162 160 Q158 178 142 175 Q130 155 130 120Z" fill="#3a1f6e"/>
                <!-- left hip -->
                <path d="M34 193 Q28 224 30 255 L66 255 L70 193Z" fill="#3a1f6e"/>
                <!-- right hip -->
                <path d="M146 193 Q152 224 150 255 L114 255 L110 193Z" fill="#3a1f6e"/>
                <!-- left leg -->
                <path d="M30 253 Q26 312 28 385 L64 385 L66 253Z" fill="#3a1f6e"/>
                <!-- right leg -->
                <path d="M150 253 Q154 312 152 385 L116 385 L114 253Z" fill="#3a1f6e"/>

                <!-- measurement line 1: shoulder -->
                <line x1="52" y1="76" x2="128" y2="76" stroke="#e05c5c" stroke-width="2" stroke-dasharray="5,3"/>
                <circle cx="90" cy="76" r="10" fill="#e05c5c" opacity="0.25"/>
                <text x="87" y="80" font-size="11" fill="#e05c5c" font-weight="bold">1</text>

                <!-- measurement line 2: chest -->
                <line x1="38" y1="110" x2="142" y2="110" stroke="#e0a020" stroke-width="2" stroke-dasharray="5,3"/>
                <circle cx="90" cy="110" r="10" fill="#e0a020" opacity="0.25"/>
                <text x="87" y="114" font-size="11" fill="#e0a020" font-weight="bold">2</text>

                <!-- measurement line 3: length arrow -->
                <line x1="160" y1="68" x2="160" y2="195" stroke="#38a169" stroke-width="2"/>
                <polygon points="155,78 165,78 160,68" fill="#38a169"/>
                <polygon points="155,185 165,185 160,195" fill="#38a169"/>
                <circle cx="160" cy="132" r="10" fill="#38a169" opacity="0.25"/>
                <text x="157" y="136" font-size="11" fill="#38a169" font-weight="bold">3</text>
              </svg>
            </div>

          </div>
          <p class="chart-note">*All the measurements are body measurements and not garment measurements.</p>
        </div>

      </div>
    </q-dialog>

  </div>
</template>

<script setup>
import { computed, ref, watch, reactive } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { menProducts } from 'src/data/menProducts'
import { addToCart, toggleWishlist, isInWishlist } from 'src/stores/shop'

const route  = useRoute()
const router = useRouter()

const product = computed(() => menProducts.find(p => p.id === Number(route.params.id)))

// ---- Images ----
const selectedImage = ref('')
const imageDialog   = ref(false)

watch(product, val => { if (val) selectedImage.value = val.images[0] }, { immediate: true })

const openImageDialog = () => { imageDialog.value = true }
const prevImage = () => {
  const imgs = product.value.images
  selectedImage.value = imgs[(imgs.indexOf(selectedImage.value) - 1 + imgs.length) % imgs.length]
}
const nextImage = () => {
  const imgs = product.value.images
  selectedImage.value = imgs[(imgs.indexOf(selectedImage.value) + 1) % imgs.length]
}

// ---- Variants ----
const sizes               = ['XS','S','M','L','XL','2XL','3XL','4XL']
const selectedTopSize     = ref('M')
const selectedBottomSize  = ref('M')
const selectedBottomStyle = ref('2 Pockets')
const bottomStyles        = ['2 Pockets', '6 Pockets']

const colorOptions = [
  { name:'Navy',       hex:'#1e3a5f' }, { name:'Maroon',    hex:'#6b1a2a' },
  { name:'Black',      hex:'#1a1a1a' }, { name:'Steel Blue',hex:'#4a6fa5' },
  { name:'Dark Teal',  hex:'#2a5f5f' }, { name:'Burgundy',  hex:'#8b1a3a' },
  { name:'Dusty Rose', hex:'#c47a7a' }, { name:'Sky Blue',  hex:'#87ceeb' },
  { name:'Lavender',   hex:'#c9b8e8' }, { name:'Royal Blue',hex:'#2452c8' },
  { name:'Blush Pink', hex:'#f4a3b0' }, { name:'Mint',      hex:'#7dd8c2' },
  { name:'Olive',      hex:'#7a8c3a' }, { name:'Forest',    hex:'#2d4a2d' },
]
const selectedColor = ref('Navy')

const oldPrice = computed(() => product.value ? Number(product.value.price) + 300 : 0)

// ---- Pincode-based Delivery ----
const pincode        = ref('')
const deliveryResult = ref(null)
const deliveryError  = ref('')

// Pincode zone map — Indian postal zones → delivery days
const getPincodeZone = (pin) => {
  const p = parseInt(pin)
  const prefix2 = Math.floor(p / 10000)
  const prefix3 = Math.floor(p / 1000)

  // Maharashtra (410xxx–445xxx) — 2–3 days
  if (p >= 400000 && p <= 445999) return { days: [2, 3], cod: true, zone: 'Maharashtra' }

  // Nearby states: Gujarat, Karnataka, Goa, MP, Telangana, AP — 3–4 days
  if (
    (p >= 360000 && p <= 396999) || // Gujarat
    (p >= 560000 && p <= 591999) || // Karnataka
    (p >= 403000 && p <= 403999) || // Goa
    (p >= 450000 && p <= 480999) || // MP
    (p >= 500000 && p <= 535999) || // Telangana
    (p >= 500000 && p <= 535999) || // AP
    (p >= 515000 && p <= 535999)    // AP
  ) return { days: [3, 4], cod: true, zone: 'Nearby' }

  // North India: Delhi, UP, Rajasthan, Punjab, Haryana — 4–5 days
  if (
    (p >= 110000 && p <= 110099) || // Delhi
    (p >= 201000 && p <= 285999) || // UP
    (p >= 301000 && p <= 345999) || // Rajasthan
    (p >= 140000 && p <= 160999) || // Punjab
    (p >= 121000 && p <= 136999)    // Haryana
  ) return { days: [4, 5], cod: true, zone: 'North India' }

  // East India: WB, Bihar, Odisha — 5–6 days
  if (
    (p >= 700000 && p <= 743999) || // WB
    (p >= 800000 && p <= 855999) || // Bihar
    (p >= 750000 && p <= 770999)    // Odisha
  ) return { days: [5, 6], cod: true, zone: 'East India' }

  // NE / Jammu / remote — 6–8 days
  if (p >= 190000 && p <= 199999) return { days: [6, 8], cod: false, zone: 'J&K / Remote' }
  if (p >= 790000 && p <= 799999) return { days: [7, 9], cod: false, zone: 'North East' }

  // Default / South India — 4–5 days
  return { days: [4, 5], cod: true, zone: 'Other' }
}

const addWorkingDays = (date, days) => {
  const d = new Date(date)
  let added = 0
  while (added < days) {
    d.setDate(d.getDate() + 1)
    const day = d.getDay()
    if (day !== 0) added++ // skip Sundays only
  }
  return d
}

const checkDelivery = () => {
  deliveryError.value  = ''
  deliveryResult.value = null

  const pin = pincode.value.trim()
  if (!pin || pin.length !== 6 || isNaN(Number(pin))) {
    deliveryError.value = 'Please enter a valid 6-digit pincode.'
    return
  }

  const zone = getPincodeZone(pin)
  const today = new Date()
  const fromDate = addWorkingDays(today, zone.days[0])
  const toDate   = addWorkingDays(today, zone.days[1])

  const fmt = { day: 'numeric', month: 'short' }
  deliveryResult.value = {
    from: fromDate.toLocaleDateString('en-IN', fmt),
    to:   toDate.toLocaleDateString('en-IN', fmt),
    cod:  zone.cod,
  }
}

// ---- Size Chart ----
const sizeChartDialog = ref(false)
const activeTab       = ref('chart')
const unit            = ref('IN')
const toggleUnit      = () => { unit.value = unit.value === 'IN' ? 'CM' : 'IN' }

const topChartIN = [
  { size:'XS', chest:'35-37', shoulder:'18.75', length:'27.5' },
  { size:'S',  chest:'37-39', shoulder:'19.25', length:'28'   },
  { size:'M',  chest:'39-41', shoulder:'19.75', length:'28.5' },
  { size:'L',  chest:'41-43', shoulder:'20.25', length:'29'   },
  { size:'XL', chest:'43-45', shoulder:'20.75', length:'29.5' },
  { size:'2XL',chest:'45-47', shoulder:'21.25', length:'30'   },
  { size:'3XL',chest:'47-49', shoulder:'21.75', length:'30.5' },
  { size:'4XL',chest:'49-51', shoulder:'22.25', length:'31'   },
]
const topChartCM = [
  { size:'XS', chest:'89-94',   shoulder:'47.5', length:'70'   },
  { size:'S',  chest:'94-99',   shoulder:'49.0', length:'71'   },
  { size:'M',  chest:'99-104',  shoulder:'50.0', length:'72.5' },
  { size:'L',  chest:'104-109', shoulder:'51.5', length:'74'   },
  { size:'XL', chest:'109-114', shoulder:'53.0', length:'75'   },
  { size:'2XL',chest:'114-119', shoulder:'54.0', length:'76'   },
  { size:'3XL',chest:'119-124', shoulder:'55.5', length:'77.5' },
  { size:'4XL',chest:'124-130', shoulder:'57.0', length:'79'   },
]
const bottomChartIN = [
  { size:'XS', waist:'27-28', hip:'33-35', length:'39' },
  { size:'S',  waist:'28-30', hip:'33-35', length:'39' },
  { size:'M',  waist:'30-32', hip:'35-37', length:'40' },
  { size:'L',  waist:'32-34', hip:'37-39', length:'41' },
  { size:'XL', waist:'34-36', hip:'39-41', length:'41' },
  { size:'2XL',waist:'36-38', hip:'41-43', length:'42' },
  { size:'3XL',waist:'38-40', hip:'43-45', length:'42' },
  { size:'4XL',waist:'40-42', hip:'45-47', length:'43' },
]
const bottomChartCM = [
  { size:'XS', waist:'69-72',  hip:'79-84',   length:'99'  },
  { size:'S',  waist:'72-76',  hip:'84-89',   length:'99'  },
  { size:'M',  waist:'76-81',  hip:'89-94',   length:'101.5'},
  { size:'L',  waist:'81-86',  hip:'94-99',   length:'104' },
  { size:'XL', waist:'86-91',  hip:'99-104',  length:'104' },
  { size:'2XL',waist:'91-96',  hip:'104-109', length:'107' },
  { size:'3XL',waist:'96-101', hip:'109-114', length:'107' },
  { size:'4XL',waist:'101-107',hip:'114-119', length:'110' },
]

const displayedTopChart    = computed(() => unit.value === 'IN' ? topChartIN    : topChartCM)
const displayedBottomChart = computed(() => unit.value === 'IN' ? bottomChartIN : bottomChartCM)

// ---- How to Measure ----
const measurements = [
  { title:'Shoulder', desc:'Measure from left shoulder end to the right shoulder end.' },
  { title:'Chest',    desc:'Measure around the fullest part of your chest.' },
  { title:'Length',   desc:'Measure from the highest point of your shoulder to the hip.' },
]

// ---- Accordion ----
const accordions = reactive([
  { title:'Details & Fit', open:false, list:[
    'Designed for long shifts and everyday hospital comfort',
    'Breathable, soft-touch and durable premium fabric',
    'Professional fit with 3 functional utility pockets',
    'Modern Structured Fit — 75% Poly, 25% Viscose',
  ]},
  { title:'Fabric & Care', open:false,
    text:'Machine wash cold. Do not bleach. Tumble dry low. Iron on low heat. Do not dry clean.' },
  { title:'Return & Exchange', open:false,
    text:'Easy 7-day returns & exchange. Item must be unused with original tags. Free pickup available at select pincodes.' },
])

// ---- Cart / Buy ----
const handleAddToCart = () => {
  addToCart({
    ...product.value,
    topSize:     selectedTopSize.value,
    bottomSize:  selectedBottomSize.value,
    bottomStyle: selectedBottomStyle.value,
    color:       selectedColor.value,
  })
}
const handleBuyNow = () => { handleAddToCart(); router.push('/cart') }
</script>

<style scoped lang="scss">
@import 'src/css/men-product-details.scss';
</style>