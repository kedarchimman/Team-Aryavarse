export default [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      // Home page
      { path: '', component: () => import('pages/HomePage.vue') },

      // Other pages
      { path: 'men', component: () => import('pages/MenPage.vue') },
      { path: 'women', component: () => import('pages/WomenPage.vue') },
      { path: 'bulk', component: () => import('pages/HomePage.vue') },

      // Product details
      { path: 'product/:id', component: () => import('pages/ProductDetailsPage.vue') },

      // Cart / Wishlist
      { path: 'cart', component: () => import('pages/CartPage.vue') },
      { path: 'wishlist', component: () => import('pages/WishlistPage.vue') },

      // Footer pages
      { path: 'about', component: () => import('pages/AboutPage.vue') },
      { path: 'contact', component: () => import('pages/ContactPage.vue') }
    ]
  },

  {
    path: '/',
    component: () => import('layouts/AuthLayout.vue'),
    children: [
      { path: 'login', component: () => import('pages/auth/LoginPage.vue') },
      { path: 'signup', component: () => import('pages/auth/SignupPage.vue') }
    ]
  },

  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]