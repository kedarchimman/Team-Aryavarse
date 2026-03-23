<template>
  <div class="q-pa-lg text-center">
    <h5>Shop by Category</h5>

    <div class="row q-col-gutter-md q-mt-md justify-center">
      <div class="col-2" v-for="c in categories" :key="c">
        <q-card class="q-pa-md">
          <p>{{ c }}</p>
        </q-card>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      categories: [
        'Medical Scrubs',
        'Lab Coats',
        'Nurse Uniforms',
        'Patient Gowns',
        'Caps',
        'PPE Kits'
      ]
    }
  }
}
</script>