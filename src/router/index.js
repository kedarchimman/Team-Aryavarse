import { defineRouter } from '#q-app/wrappers'
import {
  createRouter,
  createMemoryHistory,
  createWebHistory,
  createWebHashHistory,
} from 'vue-router'
import routes from './routes'

// ✅ IMPORT STORE
import { useAdmin } from 'src/stores/admin'

export default defineRouter(function () {

  const createHistory = process.env.SERVER
    ? createMemoryHistory
    : process.env.VUE_ROUTER_MODE === 'history'
      ? createWebHistory
      : createWebHashHistory

  const Router = createRouter({
    scrollBehavior: () => ({ left: 0, top: 0 }),
    routes,
    history: createHistory(process.env.VUE_ROUTER_BASE),
  })

  // ================= ROUTE GUARD =================
  Router.beforeEach((to, from, next) => {
    const { getRole } = useAdmin()
    const role = getRole()

    // 🔒 If trying to access admin without selecting role
    if (to.path.startsWith('/admin') && !role && to.path !== '/admin') {
      return next('/admin')
    }

    // 🎯 ROLE-BASED ACCESS CONTROL

    // Operations + Super → full access
    if (to.path.includes('/admin/products') && role !== 'operations' && role !== 'super') {
      return next('/admin/dashboard')
    }

    if (to.path.includes('/admin/inventory') && role !== 'operations' && role !== 'super') {
      return next('/admin/dashboard')
    }

    if (to.path.includes('/admin/delivery') && role !== 'operations' && role !== 'super') {
      return next('/admin/dashboard')
    }

    // Payment role → restricted (example)
    if (to.path.includes('/admin/products') && role === 'payment') {
      return next('/admin/dashboard')
    }

    next()
  })

  return Router
})