<template>
  <div class="navbar">

    <!-- SEARCH -->
    <q-input
      v-model="search"
      dense
      outlined
      placeholder="Search orders, products, customers..."
      class="search"
    >
      <template v-slot:prepend>
        <q-icon name="search" />
      </template>
    </q-input>

    <!-- RIGHT SIDE -->
    <div class="right">

      <!-- Notification -->
      <q-icon name="notifications" size="20px" />

      <!-- User -->
      <div class="user">
        <q-avatar color="green" text-color="white">AD</q-avatar>

        <div class="user-info">
          <div class="name">Admin User</div>
          <div class="email">admin@pushpa.com</div>
        </div>
      </div>

    </div>

  </div>
</template>

<script setup>
import { ref } from 'vue'

// ✅ REQUIRED FOR Q-INPUT
const search = ref('')
</script>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: white; /* ✅ removes black */
  padding: 12px 20px;
  border-bottom: 1px solid #eee;
}

/* SEARCH BOX */
.search {
  width: 420px;
}

/* RIGHT SIDE */
.right {
  display: flex;
  align-items: center;
  gap: 20px;
}

/* USER */
.user {
  display: flex;
  align-items: center;
  gap: 10px;
}

.user-info {
  font-size: 12px;
}

.name {
  font-weight: 500;
}

.email {
  color: #777;
}
</style>