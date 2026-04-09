<template>
  <div class="page">

    <!-- HEADER -->
    <div class="header">
      <h1>Parallel</h1>
          </div>
<p class="subtitle">Admin Dashboard</p>
      <p class="desc">Select your admin role to continue</p>
    <!-- CARDS -->
    <div class="cards">

      <!-- Operations -->
      <div class="card">
        <div class="icon blue">🛒</div>
        <h4>Operations Admin</h4>
        <p>Manage orders, products, inventory, and delivery operations</p>

        <ul>
          <li>View & manage orders</li>
          <li>Product catalog</li>
          <li>Inventory tracking</li>
          <li>Delivery management</li>
        </ul>

        <button @click="go('operations')">Enter Dashboard</button>
      </div>

      <!-- Payment -->
      <div class="card">
        <div class="icon green">💳</div>
        <h4>Payment & Support</h4>
        <p>Handle payments, refunds, issues, and customer support tickets</p>

        <ul>
          <li>Payment tracking</li>
          <li>Refund processing</li>
          <li>Payment issues</li>
          <li>Support tickets</li>
        </ul>

        <button @click="go('payment')">Enter Dashboard</button>
      </div>

      <!-- Super -->
      <div class="card">
        <div class="icon purple">🛡️</div>
        <h4>Super Admin</h4>
        <p>Full access to analytics, reports, admin management, and settings</p>

        <ul>
          <li>Analytics dashboard</li>
          <li>Admin management</li>
          <li>Reports & metrics</li>
          <li>Platform settings</li>
        </ul>

        <button @click="go('super')">Enter Dashboard</button>
      </div>

    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useAdmin } from 'src/stores/admin'

const router = useRouter()
const { setRole } = useAdmin()

const go = (role) => {
  setRole(role)
  router.push('/admin/dashboard')
}
</script>

<style scoped>
.page {
  min-height: 100vh;
  background: #f5f6f8;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.header {
  text-align: center;
  margin-bottom: 40px;
}

.header h1 {
  font-size: 28px;
  font-weight: 600;
}

.subtitle {
  color: #777;
}

.desc {
  color: #999;
  font-size: 13px;
}

.cards {
  display: flex;
  gap: 30px;
}

.card {
  width: 260px;
  background: white;
  padding: 20px;
  border-radius: 12px;
  box-shadow: 0 4px 14px rgba(0,0,0,0.08);
  text-align: center;
}

.card h3 {
  margin-top: 10px;
}

.card p {
  font-size: 13px;
  color: #666;
}

.card ul {
  text-align: left;
  font-size: 13px;
  margin: 10px 0;
}

button {
  width: 100%;
  background: #0f766e;
  color: white;
  padding: 10px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}

.icon {
  font-size: 30px;
  padding: 10px;
  border-radius: 10px;
  display: inline-block;
}

.blue { background: #e0ecff; }
.green { background: #e4f8ec; }
.purple { background: #f0e7ff; }

.footer {
  margin-top: 30px;
  font-size: 12px;
  color: #aaa;
}
</style>