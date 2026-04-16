<template>
  <q-page class="bulk-page">

    <!-- ─── HERO BANNER ──────────────────────────────────────── -->
    <div class="bulk-banner">
      <img :src="bulkImg" class="bulk-banner__img" alt="Bulk Orders" />
      <div class="bulk-banner__overlay">
        <div class="bulk-banner__content">
          <p class="bulk-banner__eyebrow">FOR HOSPITALS & CLINICS</p>
          <h1 class="bulk-banner__title">Bulk Orders Made Simple</h1>
          <p class="bulk-banner__sub">
            Premium hospital scrubs with custom branding &amp; guaranteed delivery
          </p>
          <div class="bulk-banner__badges">
            <span class="badge">✅ GST Invoice</span>
            <span class="badge">✅ Minimum 20 Pieces</span>
            <span class="badge">✅ Pan India Delivery</span>
          </div>
        </div>
      </div>
    </div>

    <!-- ─── MAIN CONTENT ─────────────────────────────────────── -->
    <div class="bulk-container">
      <div class="bulk-grid">

        <!-- ── LEFT: Why Us ─────────────────────────────────── -->
        <div class="why-card">
          <h3 class="why-card__title">Why Choose Us?</h3>

          <div v-for="(f, i) in features" :key="i" class="feature-item">
            <div class="feature-item__icon-wrap">
              <q-icon :name="f.icon" color="teal" size="22px" />
            </div>
            <div>
              <p class="feature-item__title">{{ f.title }}</p>
              <p class="feature-item__desc">{{ f.desc }}</p>
            </div>
          </div>

          <div class="divider" />

          <div class="trust-badge">
            <q-icon name="verified" color="teal" size="32px" />
            <p class="trust-badge__title">Trusted by Hospitals Across India</p>
            <p class="trust-badge__sub">500+ Bulk Orders Delivered Successfully</p>
          </div>

          <!-- HOW IT WORKS -->
          <div class="divider" />
          <h4 class="steps-title">How It Works</h4>
          <div v-for="(s, i) in steps" :key="i" class="step-item">
            <div class="step-item__num">{{ i + 1 }}</div>
            <div>
              <p class="step-item__title">{{ s.title }}</p>
              <p class="step-item__desc">{{ s.desc }}</p>
            </div>
          </div>
        </div>

        <!-- ── RIGHT: Form ──────────────────────────────────── -->
        <div class="form-card">
          <div class="form-card__header">
            <h2 class="form-card__title">Bulk Order Request</h2>
            <p class="form-card__sub">
              Fill the form below — our team will contact you within 24 hours
            </p>
          </div>

          <q-form @submit.prevent="submitForm" class="bulk-form">

            <!-- ── SECTION 1: Organisation -->
<div class="form-section">
  <div class="section-header">
    <span class="section-num">01</span>
    <p class="section-title">Organisation Details</p>
  </div>

  <!-- Organisation Name -->
  <div class="form-row">
    <div class="form-field">
      <p class="field-label">Organisation / Hospital Name *</p>
      <q-input
        v-model="form.orgName"
        outlined dense
        placeholder="Enter organisation name"
        :rules="[v => !!v || 'Required']"
      />
    </div>
  </div>

  <!-- Contact + Designation -->
  <div class="form-row form-row--2">
    <div class="form-field">
      <p class="field-label">Contact Person Name *</p>
      <q-input
        v-model="form.contactName"
        outlined dense
        placeholder="Enter name"
        :rules="[v => !!v || 'Required']"
      />
    </div>

    <div class="form-field">
      <p class="field-label">Designation</p>
      <q-input
        v-model="form.designation"
        outlined dense
        placeholder="Enter designation"
      />
    </div>
  </div>

  <!-- Email + Phone -->
  <div class="form-row form-row--2">
    <div class="form-field">
      <p class="field-label">Email Address *</p>
      <q-input
        v-model="form.email"
        outlined dense
        type="email"
        placeholder="Enter email"
        :rules="[v => !!v || 'Required', v => /.+@.+/.test(v) || 'Invalid email']"
      />
    </div>

    <div class="form-field">
      <p class="field-label">Phone Number *</p>
      <q-input
        v-model="form.phone"
        outlined dense
        type="tel"
        maxlength="10"
        placeholder="Enter phone number"
        :rules="[v => !!v || 'Required']"
      />
    </div>
  </div>

  <!-- City + State -->
  <div class="form-row form-row--2">
    <div class="form-field">
      <p class="field-label">City *</p>
      <q-input
        v-model="form.city"
        outlined dense
        placeholder="Enter city"
        :rules="[v => !!v || 'Required']"
      />
    </div>

    <div class="form-field">
      <p class="field-label">State *</p>
      <q-input
        v-model="form.state"
        outlined dense
        placeholder="Enter state"
        :rules="[v => !!v || 'Required']"
      />
    </div>
  </div>

  <!-- GST + Postal -->
  <div class="form-row form-row--2">
    <div class="form-field">
      <p class="field-label">GST Number</p>
      <q-input
        v-model="form.gst"
        outlined dense
        maxlength="15"
        placeholder="Enter GST number"
      />
    </div>

    <div class="form-field">
      <p class="field-label">Postal Code</p>
      <q-input
        v-model="form.postalCode"
        outlined dense
        maxlength="6"
        placeholder="Enter postal code"
      />
    </div>
  </div>
</div>

           <!-- ── SECTION 2: Order Details -->
<div class="form-section">
  <div class="section-header">
    <span class="section-num">02</span>
    <p class="section-title">Order Details</p>
  </div>

  <!-- Category + Quantity -->
  <div class="form-row form-row--2">

    <div class="form-field">
      <p class="field-label">Product Category *</p>
      <q-select
        v-model="form.category"
        :options="categories"
        outlined dense
        :display-value="form.category ? form.category : 'Select category'"
        :rules="[v => !!v || 'Required']"
      />
    </div>

    <div class="form-field">
      <p class="field-label">Quantity (Min. 20) *</p>
      <q-input
        v-model.number="form.quantity"
        outlined dense
        type="number"
        min="20"
        placeholder="Enter quantity"
        :rules="[v => v >= 20 || 'Minimum 20 pieces required']"
      />
    </div>

  </div>

  <!-- Gender + Fabric -->
  <div class="form-row form-row--2">

    <div class="form-field">
      <p class="field-label">Gender *</p>
      <q-select
        v-model="form.gender"
        :options="genderOptions"
        outlined dense
        :display-value="form.gender ? form.gender : 'Select gender'"
        :rules="[v => !!v || 'Required']"
      />
    </div>

    <div class="form-field">
      <p class="field-label">Fabric Preference</p>
      <q-select
        v-model="form.fabric"
        :options="fabrics"
        outlined dense
        :display-value="form.fabric ? form.fabric : 'Select fabric'"
      />
    </div>

  </div>

  <!-- Size Split -->
  <div class="form-row">
    <p class="field-label">Size Requirement (Approximate Pieces per Size)</p>

    <div class="size-split-grid">
      <div v-for="size in sizeSplit" :key="size.label" class="size-split-item">
        <span class="size-label">{{ size.label }}</span>
        <q-input
          v-model.number="size.qty"
          type="number"
          outlined
          dense
          class="size-qty-input"
          input-class="text-center"
        />
      </div>
    </div>

    <p class="field-hint">Total entered: {{ totalSizeQty }} pcs</p>
  </div>

  <!-- Colors + Delivery -->
  <div class="form-row form-row--2">

    <div class="form-field">
      <p class="field-label">Preferred Colors</p>
      <q-select
        v-model="form.colors"
        :options="colorOptions"
        outlined dense
        multiple
        use-chips
        :display-value="form.colors.length ? form.colors.join(', ') : 'Select colors'"
      />
    </div>

    <div class="form-field">
      <p class="field-label">Expected Delivery Date *</p>
      <q-input
        v-model="form.deliveryDate"
        outlined dense
        type="date"
        placeholder="Select date"
        :rules="[v => !!v || 'Required']"
      />
    </div>

  </div>

  <!-- Notes -->
  <div class="form-row">
    <div class="form-field">
      <p class="field-label">Additional Requirements</p>
      <q-input
        v-model="form.notes"
        outlined dense
        type="textarea"
        rows="3"
        placeholder="Any specific requirements, packaging notes, etc."
      />
    </div>
  </div>

</div>

            <!-- ── SECTION 3: Customization ── -->
<div class="form-section">
  <div class="section-header">
    <span class="section-num">03</span>
    <p class="section-title">Branding & Customization</p>
  </div>

  <q-toggle
    v-model="form.hasCustomization"
    label="Add Custom Branding to this Order"
    color="teal"
    class="custom-toggle"
  />

  <transition name="slide-down">
    <div v-if="form.hasCustomization" class="custom-block">

      <!-- Customization Types -->
      <p class="field-label">Customization Type *</p>
      <div class="custom-type-grid">
        <button
          v-for="ct in customizationTypes"
          :key="ct.id"
          type="button"
          class="type-chip"
          :class="{ 'type-chip--active': form.customTypes.includes(ct.id) }"
          @click="toggleCustomType(ct.id)"
        >
          <span>{{ ct.icon }}</span>
          <span>{{ ct.name }}</span>
          <span class="chip-price">+₹{{ ct.price }}/pc</span>
        </button>
      </div>

      <!-- Position -->
      <div v-if="form.customTypes.length" class="mt-14">
        <p class="field-label">Placement Position</p>
        <div class="position-grid">
          <button
            v-for="pos in positions"
            :key="pos.id"
            type="button"
            class="pos-chip"
            :class="{ 'pos-chip--active': form.positions.includes(pos.id) }"
            @click="togglePosition(pos.id)"
          >
            {{ pos.name }}
          </button>
        </div>
      </div>

      <!-- Text -->
      <div v-if="requiresText" class="mt-14">
        <p class="field-label">Text to Print / Embroider *</p>
        <q-input
          v-model="form.customText"
          outlined
          dense
          maxlength="50"
          placeholder="e.g. Apollo Hospital, Dr. Mehta"
          class="form-field"
          counter
        />
      </div>

      <!-- Logo Upload -->
      <div v-if="requiresLogo" class="mt-14">
        <p class="field-label">Upload Logo / Design File</p>

        <div class="upload-zone" @click="$refs.logoInput.click()">
          <div v-if="!form.logoFile">
            <q-icon name="cloud_upload" size="30px" color="teal" />
            <p class="upload-text">Click to upload (PNG, JPG, SVG)</p>
          </div>

          <div v-else class="upload-preview">
            <img :src="logoPreview" class="logo-thumb" />
            <span class="logo-filename">{{ form.logoFile.name }}</span>
            <button type="button" class="remove-logo" @click.stop="removeLogo">✕</button>
          </div>

          <input
            ref="logoInput"
            type="file"
            accept=".png,.jpg,.jpeg,.svg"
            style="display:none"
            @change="handleLogoUpload"
          />
        </div>
      </div>

      <!-- Notes -->
      <div class="mt-14">
        <p class="field-label">Customization Notes</p>
        <q-input
          v-model="form.customNotes"
          outlined
          dense
          type="textarea"
          rows="2"
          placeholder="Font style, color preference, size of logo..."
          class="form-field"
        />
      </div>

      <q-banner class="custom-warning">
        <template #avatar>
          <q-icon name="warning" color="orange-8" />
        </template>
        Customized orders are <strong>non-cancellable</strong> once production begins.
        Approval takes 24–48 hours before production starts.
      </q-banner>

    </div>
  </transition>
</div>

            <!-- ── SECTION 4: Quote Summary ──────────────────── -->
            <div v-if="form.quantity >= 20" class="quote-summary">
              <div class="quote-header">
                <q-icon name="receipt_long" color="teal" size="20px" />
                <span>Estimated Quote Summary</span>
              </div>
              <div class="quote-rows">
                <div class="quote-row">
                  <span>Quantity</span>
                  <span>{{ form.quantity }} pcs</span>
                </div>
                <div class="quote-row">
                  <span>Estimated Price / Piece</span>
                  <span>₹{{ estimatedPricePerPiece }}</span>
                </div>
                <div v-if="form.hasCustomization && customizationCost > 0" class="quote-row">
                  <span>Customization / Piece</span>
                  <span>+₹{{ customizationCost }}</span>
                </div>
                <div class="quote-row quote-row--total">
                  <span>Estimated Total</span>
                  <span>₹{{ estimatedTotal.toLocaleString('en-IN') }}</span>
                </div>
              </div>
              <p class="quote-note">
                * Final pricing will be confirmed by our team after reviewing your request.
                50% advance required to begin production.
              </p>
            </div>

            <!-- ── SUBMIT ──────────────────────────────────────── -->
            <div class="form-submit">
              <q-btn
                type="submit"
                label="Submit Bulk Request"
                color="teal"
                class="submit-btn"
                :loading="submitting"
                unelevated
                no-caps
              >
                <template #loading>
                  <q-spinner-dots size="20px" />
                </template>
              </q-btn>
              <p class="submit-note">
                Our team will reach out within 24 business hours
              </p>
            </div>

          </q-form>
        </div>

      </div>
    </div>

    <!-- ── SUCCESS DIALOG ──────────────────────────────────── -->
    <q-dialog v-model="successDialog">
      <div class="success-card">
        <div class="success-icon">✅</div>
        <h3>Request Submitted!</h3>
        <p>
          Your bulk order request has been received.<br />
          Request ID: <strong>{{ requestNumber }}</strong>
        </p>
        <p class="success-sub">
          Our team will contact you at <strong>{{ form.email }}</strong>
          within 24 business hours with a quote.
        </p>
        <q-btn
          label="Done"
          color="teal"
          unelevated
          no-caps
          v-close-popup
          class="done-btn"
        />
      </div>
    </q-dialog>

  </q-page>
</template>

<script>
import bulkImg from 'src/assets/bulk.png'

export default {
  name: 'BulkOrderPage',

  data() {
    return {
      bulkImg,
      submitting: false,
      successDialog: false,
      requestNumber: '',
      logoPreview: null,

      // ── Form — maps to bulk_order_request + organization tables ──
      form: {
        // organization table
        orgName:        '',
        contactName:    '',
        designation:    '',
        email:          '',
        phone:          '',
        city:           '',
        state:          '',
        postalCode:     '',
        gst:            '',

        // bulk_order_request
        category:       null,
        quantity:       20,
        gender:         null,
        fabric:         null,
        colors:         [],
        deliveryDate:   '',
        notes:          '',

        // size split (maps: bulk_order_request_item.quantity per variant)
        // Will be converted to bulk_order_request_item rows

        // customization (maps: order_item_customization)
        hasCustomization: false,
        customTypes:    [],   // customization_type_id[]
        positions:      [],   // position_id[]
        customText:     '',   // text_value
        logoFile:       null, // image_url after upload
        customNotes:    '',
      },

      // Size split data — maps to product_variant (size) + bulk_order_request_item
      sizeSplit: [
        { label: 'XS', qty: 0 },
        { label: 'S',  qty: 0 },
        { label: 'M',  qty: 0 },
        { label: 'L',  qty: 0 },
        { label: 'XL', qty: 0 },
        { label: 'XXL',qty: 0 },
        { label: '3XL',qty: 0 },
      ],

      // ── Dropdown data ─────────────────────────────────────
      categories: [
        'Collar Scrub Suit', 'V-Neck Scrub Suit',
        'Doctor Apron', 'Nurse Uniform', 'OT Gown', 'Mixed'
      ],
      fabrics: ['Apollo', 'Aqua', 'Cottex', 'Avenue', 'Poly-Cotton'],
      genderOptions: ['Men', 'Women', 'Mixed (Men + Women)'],
      colorOptions: ['Black', 'Navy Blue', 'Royal Blue', 'Green', 'Dark Grey', 'Brown', 'Maroon', 'White'],

      // Maps: customization_type table
      customizationTypes: [
        { id: 1, name: 'Embroidery',      icon: '🪡', price: 150, requiresText: true,  requiresLogo: false },
        { id: 2, name: 'Logo Print',       icon: '🖨️', price: 100, requiresText: false, requiresLogo: true  },
        { id: 3, name: 'Name Tag',         icon: '🏷️', price: 80,  requiresText: true,  requiresLogo: false },
        { id: 4, name: 'Dept. Print',      icon: '🏥', price: 120, requiresText: true,  requiresLogo: false },
        { id: 5, name: 'Custom Patch',     icon: '🎖️', price: 200, requiresText: false, requiresLogo: true  },
      ],

      // Maps: customization_position table
      positions: [
        { id: 1, name: 'Left Chest'  },
        { id: 2, name: 'Right Chest' },
        { id: 3, name: 'Back'        },
        { id: 4, name: 'Sleeve'      },
        { id: 5, name: 'Collar'      },
      ],

      features: [
        { icon: 'local_hospital',  title: 'Hospital-Grade Quality',   desc: 'Premium, durable medical fabrics' },
        { icon: 'payments',        title: 'Best Bulk Pricing',         desc: 'Discounts starting at 20 pieces' },
        { icon: 'support_agent',   title: 'Dedicated Account Manager', desc: 'End-to-end support & follow-up'  },
        { icon: 'palette',         title: 'Custom Branding',           desc: 'Logo, embroidery & name tags'     },
        { icon: 'local_shipping',  title: 'Flexible Payment',          desc: '50% advance, 50% on delivery'    },
        { icon: 'receipt_long',    title: 'GST Invoice',               desc: 'Proper B2B tax invoice provided'  },
      ],

      steps: [
        { title: 'Submit Request',   desc: 'Fill the form with your requirements' },
        { title: 'Get a Quote',      desc: 'Our team sends pricing within 24 hours' },
        { title: 'Approve & Pay',    desc: '50% advance to start production' },
        { title: 'Production',       desc: 'Manufacturing + customization in 7–10 days' },
        { title: 'Delivery',         desc: 'Pan-India shipping to your door' },
      ]
    }
  },

  computed: {
    totalSizeQty() {
      return this.sizeSplit.reduce((sum, s) => sum + (s.qty || 0), 0)
    },
    requiresText() {
      return this.form.customTypes.some(id => {
        const t = this.customizationTypes.find(c => c.id === id)
        return t && t.requiresText
      })
    },
    requiresLogo() {
      return this.form.customTypes.some(id => {
        const t = this.customizationTypes.find(c => c.id === id)
        return t && t.requiresLogo
      })
    },
    customizationCost() {
      return this.form.customTypes.reduce((sum, id) => {
        const t = this.customizationTypes.find(c => c.id === id)
        return sum + (t ? t.price : 0)
      }, 0)
    },
    estimatedPricePerPiece() {
      const qty = this.form.quantity || 0
      if (qty >= 200) return 700
      if (qty >= 100) return 750
      if (qty >= 50)  return 820
      return 900
    },
    estimatedTotal() {
      const qty = this.form.quantity || 0
      return qty * (this.estimatedPricePerPiece + this.customizationCost)
    }
  },

  methods: {
    toggleCustomType(id) {
      const idx = this.form.customTypes.indexOf(id)
      if (idx === -1) this.form.customTypes.push(id)
      else            this.form.customTypes.splice(idx, 1)
    },
    togglePosition(id) {
      const idx = this.form.positions.indexOf(id)
      if (idx === -1) this.form.positions.push(id)
      else            this.form.positions.splice(idx, 1)
    },
    handleLogoUpload(e) {
      const file = e.target.files[0]
      if (!file) return
      this.form.logoFile = file
      this.logoPreview   = URL.createObjectURL(file)
    },
    removeLogo() {
      this.form.logoFile = null
      this.logoPreview   = null
    },

    async submitForm() {
      this.submitting = true

      // Build payload matching bulk_order_request schema
      const payload = {
        // organization table fields
        organization: {
          name:           this.form.orgName,
          contact_person: this.form.contactName,
          email:          this.form.email,
          phone:          this.form.phone,
          gst_number:     this.form.gst || null,
          city:           this.form.city,
          state:          this.form.state,
          postal_code:    this.form.postalCode || null,
          country:        'India',
        },
        // bulk_order_request table fields
        request: {
          status:                 'PENDING',
          notes:                  this.form.notes || null,
          expected_delivery_date: this.form.deliveryDate || null,
          category:               this.form.category,
          gender:                 this.form.gender,
          fabric:                 this.form.fabric,
          colors:                 this.form.colors,
        },
        // bulk_order_request_item (one per size)
        items: this.sizeSplit
          .filter(s => s.qty > 0)
          .map(s => ({ size: s.label, quantity: s.qty })),
        // customization (order_item_customization schema)
        customization: this.form.hasCustomization ? {
          customization_type_ids: this.form.customTypes,
          position_ids:           this.form.positions,
          text_value:             this.form.customText || null,
          image_name:             this.form.logoFile?.name || null,
          approval_status:        'PENDING',
          notes:                  this.form.customNotes || null,
        } : null
      }

      console.log('Bulk Order Payload:', payload)

      // Simulate API call
      await new Promise(r => setTimeout(r, 1500))

      // Generate request number (frontend placeholder)
      this.requestNumber = 'BLK-' + Date.now().toString().slice(-8)
      this.submitting = false
      this.successDialog = true
    }
  }
}
</script>

<style lang="scss">
@import 'src/css/bulkorder.scss';
</style>