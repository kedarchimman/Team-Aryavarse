export default [

  // ================= DEFAULT REDIRECT =================
  {
    path: '/',
    redirect: '/admin'
  },

  // ================= USER APP =================
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: 'home', component: () => import('pages/HomePage.vue') },
      { path: 'men', component: () => import('pages/MenPage.vue') },
      { path: 'women', component: () => import('pages/WomenPage.vue') },
      { path: 'bulk', component: () => import('pages/BulkOrder.vue') },

      { path: 'product/:id', component: () => import('pages/ProductDetailsPage.vue') },
      { path: 'men-product/:id', component: () => import('pages/MenProductDetailsPage.vue') },
      { path: 'women-product/:id', component: () => import('pages/WomenProductDetails.vue') },

      { path: 'cart', component: () => import('pages/CartPage.vue') },
      { path: 'wishlist', component: () => import('pages/WishlistPage.vue') },

      { path: 'about', component: () => import('pages/AboutPage.vue') },
      { path: 'contact', component: () => import('pages/ContactPage.vue') }
    ]
  },

  // ================= AUTH =================
  {
    path: '/',
    component: () => import('layouts/AuthLayout.vue'),
    children: [
      { path: 'login', component: () => import('pages/auth/LoginPage.vue') },
      { path: 'signup', component: () => import('pages/auth/SignupPage.vue') }
    ]
  },

  // ================= ADMIN PANEL =================
 // ================= ADMIN PANEL =================
{
  path: '/admin',
  children: [
    { path: '', component: () => import('pages/admin/AdminSelect.vue') }, // ✅ NO layout

    {
      path: '',
      component: () => import('layouts/AdminLayout.vue'),
      children: [
        { path: 'dashboard', component: () => import('pages/admin/Dashboard.vue') },
        { path: 'products', component: () => import('pages/admin/Products.vue') },
        { path: 'inventory', component: () => import('pages/admin/Inventory.vue') },
        { path: 'delivery', component: () => import('pages/admin/Delivery.vue') }
      ]
    }
  ]
}

  // ================= 404 =================
 
]