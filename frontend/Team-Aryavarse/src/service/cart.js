import { api } from 'boot/axios'

const getAuthData = () => {
  const rawUserId = localStorage.getItem('user_id')
  const guestUuid = localStorage.getItem('guest_uuid')

  return {
    user_id: rawUserId ? Number(rawUserId) : null,
    guest_uuid: guestUuid || null,
  }
}

export const ensureGuestUuid = async () => {
  const existingGuestUuid = localStorage.getItem('guest_uuid')
  const rawUserId = localStorage.getItem('user_id')

  if (rawUserId) {
    return null
  }

  if (existingGuestUuid) {
    return existingGuestUuid
  }

  const res = await api.post('/cart/guest')
  const guestUuid = res?.data?.guest_uuid || null

  if (!guestUuid) {
    throw new Error('Guest UUID not returned from backend')
  }

  localStorage.setItem('guest_uuid', guestUuid)
  return guestUuid
}

const getAuthPayload = async () => {
  const auth = getAuthData()

  if (auth.user_id) {
    return {
      user_id: auth.user_id,
      guest_uuid: null,
    }
  }

  let guestUuid = auth.guest_uuid

  if (!guestUuid) {
    guestUuid = await ensureGuestUuid()
  }

  return {
    user_id: null,
    guest_uuid: guestUuid,
  }
}

export const addToCart = async (payload) => {
  if (!payload || !payload.variant_id) {
    throw new Error('variant_id is required')
  }

  const quantity = Number(payload.quantity || 1)

  if (quantity <= 0) {
    throw new Error('quantity must be greater than 0')
  }

  const authPayload = await getAuthPayload()

  const body = {
    variant_id: Number(payload.variant_id),
    quantity,
    ...authPayload,
  }

  const res = await api.post('/cart/add', body)
  return res.data
}

export const getCartItems = async () => {
  const auth = getAuthData()

  if (auth.user_id) {
    const res = await api.get('/cart/', {
      params: { user_id: auth.user_id },
    })
    return res.data
  }

  let guestUuid = auth.guest_uuid

  if (!guestUuid) {
    guestUuid = await ensureGuestUuid()
  }

  const res = await api.get('/cart/', {
    params: { guest_uuid: guestUuid },
  })

  return res.data
}

export const updateCartQty = async (cartItemId, quantity) => {
  if (!cartItemId) {
    throw new Error('cartItemId is required')
  }

  const qty = Number(quantity)

  if (qty <= 0) {
    throw new Error('quantity must be greater than 0')
  }

  const authPayload = await getAuthPayload()

  const body = {
    cart_item_id: Number(cartItemId),
    quantity: qty,
    ...authPayload,
  }

  const res = await api.put('/cart/update', body)
  return res.data
}

export const removeCartItem = async (cartItemId) => {
  if (!cartItemId) {
    throw new Error('cartItemId is required')
  }

  const authPayload = await getAuthPayload()

  const res = await api.delete('/cart/remove', {
    data: {
      cart_item_id: Number(cartItemId),
      ...authPayload,
    },
  })

  return res.data
}

export const mergeGuestCart = async () => {
  const rawUserId = localStorage.getItem('user_id')
  const guestUuid = localStorage.getItem('guest_uuid')

  if (!rawUserId || !guestUuid) {
    return null
  }

  const res = await api.post('/cart/merge', {
    user_id: Number(rawUserId),
    guest_uuid: guestUuid,
  })

  localStorage.removeItem('guest_uuid')
  return res.data
}

export const getCartCount = async () => {
  const data = await getCartItems()
  const items = data?.items || []

  if (!Array.isArray(items)) {
    return 0
  }

  return items.reduce((sum, item) => sum + Number(item.quantity || 0), 0)
}

export const addToCartApi = addToCart
export const getCartApi = getCartItems
export const updateCartApi = updateCartQty
export const updateCartItemApi = updateCartQty
export const removeCartItemApi = removeCartItem
export const deleteCartItemApi = removeCartItem
export const createGuest = ensureGuestUuid
export const mergeCartApi = mergeGuestCart

export default {
  ensureGuestUuid,
  createGuest,
  addToCart,
  addToCartApi,
  getCartItems,
  getCartApi,
  updateCartQty,
  updateCartApi,
  updateCartItemApi,
  removeCartItem,
  removeCartItemApi,
  deleteCartItemApi,
  mergeGuestCart,
  mergeCartApi,
  getCartCount,
}
