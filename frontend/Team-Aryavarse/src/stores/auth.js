import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: localStorage.getItem('token') || null,
    user: JSON.parse(localStorage.getItem('user')) || null,
    id_token: localStorage.getItem('id_token') || null
  }),

  actions: {
    setAuth(token, userData) {
      this.token = token
      this.user = userData
      this.id_token = userData.id_token

      // ✅ STORE IN LOCALSTORAGE
      localStorage.setItem('token', token)
      localStorage.setItem('user', JSON.stringify(userData))
      localStorage.setItem('id_token', userData.id_token)
    },

    logout() {
      this.token = null
      this.user = null
      this.id_token = null

      // ✅ CLEAR STORAGE
      localStorage.removeItem('token')
      localStorage.removeItem('user')
      localStorage.removeItem('id_token')
    }
  }
})