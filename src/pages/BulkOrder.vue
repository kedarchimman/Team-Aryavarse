<template>
  <q-page class="bg-grey-1 q-pa-sm">

    <!-- 🔥 PREMIUM HERO BANNER -->
    <div class="banner">
      <img :src="bulkImg" class="banner-img" />

      <div class="banner-overlay">
        <div class="banner-content">
          <h2>Bulk Orders Made Simple</h2>
          <p>High-quality uniforms with custom branding & fast delivery</p>
        </div>
      </div>
    </div>

    <div class="container">

      <div class="row q-col-gutter-md">

        <!-- LEFT PANEL -->
        <div class="col-12 col-md-4">
          <q-card class="left-panel">

            <h5 class="text-bold q-mb-md">Why Choose Us?</h5>

            <div v-for="(item,i) in features" :key="i" class="feature">
              <q-icon :name="item.icon" color="teal" size="28px"/>
              <div>
                <div class="text-weight-medium">{{ item.title }}</div>
                <div class="text-caption text-grey-7">{{ item.desc }}</div>
              </div>
            </div>

            <q-separator class="q-my-md"/>

            <div class="text-center">
              <q-icon name="verified" color="teal" size="30px" />
              <div class="text-weight-medium q-mt-sm">
                Trusted by Hospitals Across India
              </div>

              <div class="text-caption text-grey-7">
                500+ Bulk Orders Delivered Successfully
              </div>
            </div>

          </q-card>
        </div>

        <!-- RIGHT PANEL -->
        <div class="col-12 col-md-8">
          <q-card class="form-card">

            <div class="text-h6 q-mb-md">Bulk Order Request</div>

            <q-form @submit.prevent="submitForm" class="q-gutter-md">

              <div class="section-title">Contact Information</div>

              <q-input outlined dense v-model="form.orgName" label="Organization Name *"/>
              <q-input outlined dense v-model="form.contactName" label="Contact Person Name *"/>

              <div class="row q-col-gutter-sm">
                <div class="col-12 col-md-6">
                  <q-input outlined dense v-model="form.email" label="Email *"/>
                </div>
                <div class="col-12 col-md-6">
                  <q-input outlined dense v-model="form.phone" label="Phone *"/>
                </div>
              </div>

              <q-input outlined dense v-model="form.location" label="City / State *"/>
              <q-input outlined dense v-model="form.gst" label="GST Number"/>

              <div class="section-title">Order Details</div>

              <q-select outlined dense v-model="form.category" :options="categories" label="Product Category *"/>

              <div class="row q-col-gutter-sm">
                <div class="col-12 col-md-6">
                  <q-select outlined dense v-model="form.fabric" :options="fabrics" label="Fabric"/>
                </div>
                <div class="col-12 col-md-6">
                  <q-select outlined dense v-model="form.gender" :options="genderOptions" label="Gender Split *"/>
                </div>
              </div>

              <q-input outlined dense type="number" v-model="form.quantity" label="Estimated Quantity *"/>
              <q-input outlined dense v-model="form.sizes" label="Size Requirements"/>
              <q-input outlined dense v-model="form.colors" label="Preferred Colors"/>
              <q-input outlined dense type="date" v-model="form.deliveryDate" label="Expected Delivery Date *"/>
              <q-input outlined dense type="textarea" v-model="form.notes" label="Additional Requirements"/>

              <q-toggle v-model="form.customization" label="Add Custom Branding?" />

              <div v-if="form.customization" class="custom-box">

                <q-option-group
                  v-model="form.customType"
                  :options="customOptions"
                  type="checkbox"
                />

                <q-file outlined dense v-model="form.logo" label="Upload Logo"/>

                <q-select outlined dense v-model="form.placement"
                  :options="placementOptions"
                  label="Placement"
                  multiple
                />

                <q-input outlined dense v-model="form.text" label="Text to Print"/>
                <q-input outlined dense v-model="form.brandColor" label="Brand Color"/>
                <q-input outlined dense type="textarea" v-model="form.customNotes" label="Customization Notes"/>

              </div>

              <q-banner class="bg-red-1 text-red text-caption">
                Customized orders are non-cancellable once production begins.
              </q-banner>

              <q-btn type="submit" label="Submit Request" color="teal" class="full-width"/>

            </q-form>

          </q-card>
        </div>

      </div>

    </div>

  </q-page>
</template>

<script>
import bulkImg from 'src/assets/bulk.png'

export default {
  data() {
    return {
      bulkImg,

      form: {
        orgName: "",
        contactName: "",
        email: "",
        phone: "",
        location: "",
        gst: "",
        category: "",
        fabric: "",
        gender: "",
        quantity: "",
        sizes: "",
        colors: "",
        deliveryDate: "",
        notes: "",
        customization: false,
        customType: [],
        logo: null,
        placement: [],
        text: "",
        brandColor: "",
        customNotes: ""
      },

      categories: ["Doctor Scrubs", "Nurse Uniforms", "Hospital Uniforms", "Mixed"],
      fabrics: ["Apollo", "Aqua", "Cottex", "Avenue"],
      genderOptions: ["Men", "Women", "Mixed"],
      placementOptions: ["Left Chest", "Right Chest", "Back", "Sleeve"],

      customOptions: [
        { label: "Logo Print", value: "print" },
        { label: "Embroidery", value: "embroidery" },
        { label: "Department Name", value: "dept" },
        { label: "Name Tags", value: "tags" }
      ],

      features: [
        { icon: "local_hospital", title: "Hospital Quality", desc: "Premium fabrics" },
        { icon: "payments", title: "Bulk Pricing", desc: "Best discounts" },
        { icon: "support_agent", title: "Dedicated Manager", desc: "End-to-end support" },
        { icon: "palette", title: "Custom Branding", desc: "Logo & embroidery" },
        { icon: "local_shipping", title: "Flexible Payment", desc: "50% advance" }
      ]
    }
  },

  methods: {
    submitForm() {
      this.$q.notify({
        type: "positive",
        message: "Request Submitted!"
      })
    }
  }
}
</script>

<style scoped>

/* CONTAINER */
.container {
  max-width: 1200px;
  margin: auto;
}

/* 🔥 HERO BANNER */
.banner {
  width: 100%;
  height: 55vh;
  min-height: 300px;
  position: relative;
  overflow: hidden;
  border-radius: 20px;
  margin-bottom: 30px;
}
.banner-img {
  width: 100%;
  height: 100%;
  object-fit: cover;

  /* 👇 FACE FIX */
  object-position: center 10%;
}

/* OVERLAY */
.overlay {
  background: none;   /* ❌ no glass */
  backdrop-filter: none;
  padding: 0;
}

/* TEXT BOX */
.banner-content {
  text-align: center;
  color: white;
  backdrop-filter: blur(10px);
  background: rgba(255,255,255,0.08);
  padding: 25px 35px;
  border-radius: 16px;
}

.banner-content h2 {
  font-size: 38px;
  font-weight: 700;
}

.banner-content p {
  font-size: 16px;
  margin-top: 150px;
}

/* LEFT PANEL */
.left-panel {
  border-radius: 16px;
  padding: 20px;
  background: white;
  box-shadow: 0 10px 30px rgba(0,0,0,0.08);
}

/* FEATURES */
.feature {
  display: flex;
  gap: 12px;
  margin-bottom: 18px;
  align-items: center;
}

/* FORM CARD */
.form-card {
  border-radius: 16px;
  padding: 25px;
  background: white;
  box-shadow: 0 10px 30px rgba(0,0,0,0.08);
}

/* SECTION */
.section-title {
  font-weight: 600;
  margin-top: 15px;
}

/* CUSTOM BOX */
.custom-box {
  padding: 15px;
  border-radius: 12px;
  background: #f6f6f6;
}

/* BUTTON */
.q-btn {
  border-radius: 10px;
  font-weight: 600;
}

/* RESPONSIVE */
@media (max-width: 768px) {
  .banner {
    height: 40vh;
  }

  .banner-content h2 {
    font-size: 24px;
  }
}

</style>