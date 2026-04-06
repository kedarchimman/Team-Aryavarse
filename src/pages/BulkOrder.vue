<template>
  <q-page class="q-pa-xl bg-grey-2 page">

    <!-- HERO -->
    <div class="hero-box q-pa-lg q-mb-xl">
      <div class="hero-title">
        Bulk Orders for Healthcare Facilities
      </div>
      <div class="hero-sub">
        Outfit your entire medical staff with premium quality uniforms. Get exclusive pricing,
        dedicated support, and customization options for bulk orders.
      </div>
    </div>

    <!-- CONTENT -->
    <div class="row q-col-gutter-xl">

      <!-- LEFT -->
      <div class="col-12 col-md-6">
        <div class="section-title">
          Why Choose Parallel for Bulk Orders?
        </div>

        <div
          v-for="item in features"
          :key="item.title"
          class="row items-start feature-item"
        >
          <q-icon :name="item.icon" class="feature-icon q-mr-md" />

          <div>
            <div class="feature-title">{{ item.title }}</div>
            <div class="feature-desc">{{ item.desc }}</div>
          </div>
        </div>
      </div>

      <!-- RIGHT FORM -->
      <div class="col-12 col-md-6">
        <q-card flat bordered class="q-pa-lg form-card">

          <div class="form-title">
            Request a Bulk Quote
          </div>

          <!-- ✅ FORM ADDED -->
          <q-form ref="formRef" @submit.prevent="onSubmit">

            <!-- Organization -->
            <q-input
              v-model="form.organization"
              outlined dense
              label="Organization Name *"
              placeholder="Hospital/Clinic Name"
              :rules="[v => !!v || 'Please fill this']"
              class="q-mb-md"
            />

            <!-- Contact -->
            <q-input
              v-model="form.contact"
              outlined dense
              label="Contact Person *"
              placeholder="Your Name"
              :rules="[v => !!v || 'Please fill this']"
              class="q-mb-md"
            />

            <!-- Email + Phone -->
            <div class="row q-col-gutter-sm">
              <div class="col">
                <q-input
                  v-model="form.email"
                  outlined dense
                  label="Email *"
                  placeholder="email@hospital.com"
                  :rules="[
                    v => !!v || 'Please fill this',
                    v => /.+@.+\..+/.test(v) || 'Invalid email'
                  ]"
                />
              </div>

              <div class="col">
                <q-input
                  v-model="form.phone"
                  outlined dense
                  label="Phone *"
                  placeholder="+91 98765 43210"
                  :rules="[v => !!v || 'Please fill this']"
                />
              </div>
            </div>

            <!-- Category -->
            <q-select
              v-model="form.category"
              outlined dense
              label="Product Category *"
              :options="['Scrubs', 'Lab Coats', 'Nurse Uniforms']"
              :rules="[v => !!v || 'Please fill this']"
              class="q-mt-md"
            />

            <!-- Quantity -->
            <q-input
              v-model="form.quantity"
              outlined dense
              label="Estimated Quantity *"
              placeholder="Number of units"
              :rules="[v => !!v || 'Please fill this']"
              class="q-mt-md"
            />

            <!-- Requirements -->
            <q-input
              v-model="form.requirements"
              outlined dense
              type="textarea"
              label="Additional Requirements"
              placeholder="Tell us about your specific requirements..."
              class="q-mt-md"
            />

            <!-- Submit -->
            <q-btn
              label="Submit Request"
              type="submit"
              class="full-width q-mt-lg submit-btn"
              unelevated
            />

          </q-form>

          <div class="form-footer">
            Our team will contact you within 24 hours with a customized quote
          </div>

        </q-card>
      </div>

    </div>

  </q-page>
</template>

<script setup>
import { ref } from 'vue'

const formRef = ref(null)

// ✅ FIX: form reactive (input typing works now)
const form = ref({
  organization: '',
  contact: '',
  email: '',
  phone: '',
  category: '',
  quantity: '',
  requirements: ''
})

// submit
const onSubmit = () => {
  formRef.value.validate().then(valid => {
    if (valid) {
      alert("Form Submitted ✅")
    }
  })
}

// features unchanged
const features = [
  {
    icon: "verified",
    title: "Hospital-Grade Quality",
    desc: "Premium fabrics and construction designed to withstand the demands of daily use in medical environments."
  },
  {
    icon: "sell",
    title: "Bulk Pricing",
    desc: "Special discounted rates for large orders. The more you order, the more you save."
  },
  {
    icon: "support_agent",
    title: "Dedicated Support",
    desc: "Your dedicated account manager will handle all aspects of your order from quotation to delivery."
  },
  {
    icon: "mail",
    title: "Custom Branding",
    desc: "Add your hospital logo, department names, or custom embroidery to create a professional unified look."
  }
]
</script>

<style scoped>

/* FONT + PAGE */
.page {
  font-family: 'Poppins', sans-serif;
}

/* HERO */
.hero-box {
  background: #1f7a6b;
  border-radius: 10px;
}

.hero-title {
  font-size: 24px;
  font-weight: 600;
  color: white;
}

.hero-sub {
  font-size: 14px;
  color: white;
  margin-top: 6px;
  max-width: 600px;
}

/* LEFT */
.section-title {
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 16px;
}

.feature-item {
  margin-bottom: 14px;
}

.feature-icon {
  background: #e6f4f1;
  color: #1f7a6b;
  padding: 8px;
  border-radius: 6px;
}

.feature-title {
  font-size: 14px;
  font-weight: 600;
}

.feature-desc {
  font-size: 12px;
  color: #777;
}

/* FORM */
.form-card {
  border-radius: 10px;
}

.form-title {
  font-size: 14px;
  font-weight: 600;
  margin-bottom: 10px;
}

.submit-btn {
  background: #2fb5a3;
  color: white;
}

.form-footer {
  font-size: 11px;
  text-align: center;
  color: #888;
  margin-top: 8px;
}

</style>