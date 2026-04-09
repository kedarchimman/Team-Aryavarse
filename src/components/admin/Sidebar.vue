<template>
  <q-drawer show-if-above bordered>
    <q-list>

      <q-item clickable to="/admin">
        <q-item-section>Dashboard</q-item-section>
      </q-item>

      <q-item clickable to="/admin/products">
        <q-item-section>Products</q-item-section>
      </q-item>

      <q-item clickable to="/admin/inventory">
        <q-item-section>Inventory</q-item-section>
      </q-item>

      <q-item clickable to="/admin/delivery">
        <q-item-section>Delivery</q-item-section>
      </q-item>

    </q-list>
  </q-drawer>
</template>