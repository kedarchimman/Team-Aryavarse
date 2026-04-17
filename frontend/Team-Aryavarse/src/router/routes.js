export default [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      // HOME
      { path: '', component: () => import('pages/HomePage.vue') },
      { path: 'home', component: () => import('pages/HomePage.vue') },

      // CATEGORY PAGES
      { path: 'men', component: () => import('pages/MenPage.vue') },
      { path: 'women', component: () => import('pages/WomenPage.vue') },
      { path: 'aprons', component: () => import('pages/Aprons.vue') },

      // BULK (new override instead of old HomePage)
      { path: 'bulk', component: () => import('pages/BulkOrder.vue') },

      // PRODUCT DETAILS
      { path: 'product/:id', component: () => import('pages/ProductDetailsPage.vue') },
      { path: 'men-product/:id', component: () => import('pages/MenProductDetailsPage.vue') },
      { path: 'women-product/:id', component: () => import('pages/WomenProductDetails.vue') },
      { path: 'aprons-product/:id', component: () => import('pages/ApronsProductDetail.vue') },

      // USER FEATURES
      { path: 'cart', component: () => import('pages/CartPage.vue') },
      { path: 'wishlist', component: () => import('pages/WishlistPage.vue') },
      { path: 'profile', component: () => import('pages/ProfilePage.vue') }, // ✅ from old

      // FOOTER / INFO
      { path: 'about', component: () => import('pages/AboutPage.vue') },
      { path: 'contact', component: () => import('pages/ContactPage.vue') },
    ]
  },

  // AUTH LAYOUT
  {
    path: '/',
    component: () => import('layouts/AuthLayout.vue'),
    children: [
      { path: 'login', component: () => import('pages/auth/LoginPage.vue') },
      { path: 'signup', component: () => import('pages/auth/SignupPage.vue') },

      // ✅ from old file
      { path: 'forgot-password', component: () => import('pages/auth/ForgotPassword.vue') }
    ]
  },

  // ✅ AUTH CALLBACK (important for OAuth / Firebase / etc.)
  {
    path: '/auth/callback',
    component: () => import('pages/AuthCallback.vue')
  },

  // 404
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]