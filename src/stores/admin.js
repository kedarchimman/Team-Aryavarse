import { ref } from 'vue'

const role = ref(null)

export function useAdmin() {

  const setRole = (r) => {
    role.value = r
    localStorage.setItem('admin_role', r)
  }

  const getRole = () => {
    if (!role.value) {
      role.value = localStorage.getItem('admin_role')
    }
    return role.value
  }

  const clearRole = () => {
    role.value = null
    localStorage.removeItem('admin_role')
  }

  return { role, setRole, getRole, clearRole }
}