<template>
  <q-page class="q-pa-md bg-grey-2">

    <!-- TITLE -->
    <div class="text-h5 text-weight-medium q-mb-xs">
      Operations Dashboard
    </div>
    <div class="text-subtitle2 text-grey-7 q-mb-md">
      Overview of your e-commerce operations
    </div>

    <!-- CARDS -->
    <div class="row q-col-gutter-md q-mb-lg">

      <!-- Card 1 -->
      <div class="col-12 col-md-3">
        <q-card class="dashboard-card">
          <div class="row items-center justify-between">
            <div>
              <div class="text-caption text-grey">Total Orders</div>
              <div class="text-h6">1,247</div>
              <div class="text-positive text-caption">↑ 12% from last month</div>
            </div>
            <q-avatar class="bg-blue-1 text-blue">
              <q-icon name="shopping_cart" />
            </q-avatar>
          </div>
        </q-card>
      </div>

      <!-- Card 2 -->
      <div class="col-12 col-md-3">
        <q-card class="dashboard-card">
          <div class="row items-center justify-between">
            <div>
              <div class="text-caption text-grey">Pending Orders</div>
              <div class="text-h6">23</div>
            </div>
            <q-avatar class="bg-yellow-2 text-orange">
              <q-icon name="schedule" />
            </q-avatar>
          </div>
        </q-card>
      </div>

      <!-- Card 3 -->
      <div class="col-12 col-md-3">
        <q-card class="dashboard-card">
          <div class="row items-center justify-between">
            <div>
              <div class="text-caption text-grey">Revenue Today</div>
              <div class="text-h6">₹45,280</div>
              <div class="text-positive text-caption">↑ 8% from yesterday</div>
            </div>
            <q-avatar class="bg-green-1 text-green">
              <q-icon name="currency_rupee" />
            </q-avatar>
          </div>
        </q-card>
      </div>

      <!-- Card 4 -->
      <div class="col-12 col-md-3">
        <q-card class="dashboard-card">
          <div class="row items-center justify-between">
            <div>
              <div class="text-caption text-grey">Low Stock Alerts</div>
              <div class="text-h6 text-negative">7</div>
            </div>
            <q-avatar class="bg-red-1 text-red">
              <q-icon name="warning" />
            </q-avatar>
          </div>
        </q-card>
      </div>

    </div>

    <!-- TABLE -->
    <q-card class="q-mb-lg rounded-borders">

      <div class="row items-center justify-between q-pa-md">
        <div class="text-subtitle1 text-weight-medium">Recent Orders</div>
        <q-btn flat label="View All" />
      </div>

      <q-table
        :rows="orders"
        :columns="columns"
        row-key="id"
        flat
      >

        <!-- STATUS BADGES -->
        <template v-slot:body-cell-status="props">
          <q-td>
            <q-badge
              :color="getStatusColor(props.row.status)"
              rounded
              class="q-px-sm"
            >
              {{ props.row.status }}
            </q-badge>
          </q-td>
        </template>

        <!-- PAYMENT -->
        <template v-slot:body-cell-payment="props">
          <q-td>
            <span
              :class="props.row.payment === 'Paid' ? 'text-positive' : ''"
            >
              {{ props.row.payment }}
            </span>
          </q-td>
        </template>

      </q-table>

    </q-card>

    <!-- ALERTS -->
    <q-card class="q-pa-md">

      <div class="text-subtitle1 q-mb-sm">Alerts & Notifications</div>

      <q-banner class="bg-yellow-1 text-black q-mb-sm rounded-borders">
        ⚠ Navy Blue Scrubs (M) - Only 5 units left
      </q-banner>

      <q-banner class="bg-blue-1 text-black q-mb-sm rounded-borders">
        ℹ Return request for Order #ORD-0098
      </q-banner>

      <q-banner class="bg-red-1 text-black rounded-borders">
        ❌ White Lab Coats (L) - Out of stock
      </q-banner>

    </q-card>

  </q-page>
</template>

<script setup>

const columns = [
  { name: 'id', label: 'Order ID', field: 'id' },
  { name: 'customer', label: 'Customer', field: 'customer' },
  { name: 'products', label: 'Products', field: 'products' },
  { name: 'amount', label: 'Amount', field: 'amount' },
  { name: 'status', label: 'Status', field: 'status' },
  { name: 'payment', label: 'Payment', field: 'payment' },
  { name: 'date', label: 'Date', field: 'date' }
]

const orders = [
  { id: '#ORD-1001', customer: 'Rajesh Kumar', products: '3 items', amount: '₹4,250', status: 'Pending', payment: 'COD', date: 'Apr 6, 2026' },
  { id: '#ORD-1002', customer: 'Priya Singh', products: '2 items', amount: '₹3,100', status: 'Processing', payment: 'Paid', date: 'Apr 6, 2026' },
  { id: '#ORD-1003', customer: 'Amit Patel', products: '5 items', amount: '₹8,500', status: 'Shipped', payment: 'Paid', date: 'Apr 5, 2026' },
  { id: '#ORD-1004', customer: 'Sneha Reddy', products: '1 item', amount: '₹1,950', status: 'Delivered', payment: 'Paid', date: 'Apr 5, 2026' }
]

// STATUS COLORS
const getStatusColor = (status) => {
  if (status === 'Pending') return 'yellow'
  if (status === 'Processing') return 'blue'
  if (status === 'Shipped') return 'purple'
  if (status === 'Delivered') return 'green'
}

</script>

<style scoped>
.dashboard-card {
  padding: 16px;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
</style>