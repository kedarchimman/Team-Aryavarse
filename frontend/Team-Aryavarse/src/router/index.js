import { defineRouter } from '#q-app/wrappers'
import {
  createRouter,
  createMemoryHistory,
  createWebHistory,
  createWebHashHistory,
} from 'vue-router'
import routes from './routes'
import { useAuthStore } from 'src/stores/auth'

export default defineRouter(function () {

  const createHistory = process.env.SERVER
    ? createMemoryHistory
    : createWebHistory          // ← keep as createWebHistory (not hash)

  const Router = createRouter({
    scrollBehavior: () => ({ left: 0, top: 0 }),
    routes,
    history: createHistory(process.env.VUE_ROUTER_BASE),
  })

  Router.beforeEach((to) => {
    const auth = useAuthStore()

    // ← CRITICAL: let the callback page through unconditionally
    if (to.path.startsWith('/auth/')) return true

    if (to.path === '/profile' && !auth.token) {
      return '/login'
    }

    if ((to.path === '/login' || to.path === '/signup') && auth.token) {
      return '/profile'
    }
  })

  return Router
})