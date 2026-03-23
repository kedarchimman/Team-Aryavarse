<template>
  <q-card>
    <q-img src="https://via.placeholder.com/200" />

    <q-card-section>
      <div>{{ product.name }}</div>
      <div>₹ {{ product.price }}</div>
    </q-card-section>

    <q-card-actions>
      <q-btn label="View" :to="'/product/' + product.id" />
    </q-card-actions>
  </q-card>
</template>

<script>
export default {
  props: ['product']
}
</script>