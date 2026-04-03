import { ref, watch } from 'vue'

// cart data
export const cart = ref(JSON.parse(localStorage.getItem('cart') || '[]'))

// wishlist data
export const wishlist = ref(JSON.parse(localStorage.getItem('wishlist') || '[]'))

// save cart
watch(cart, (val) => {
  localStorage.setItem('cart', JSON.stringify(val))
}, { deep: true })

// save wishlist
watch(wishlist, (val) => {
  localStorage.setItem('wishlist', JSON.stringify(val))
}, { deep: true })

// add to cart
export const addToCart = (product) => {
  const existing = cart.value.find(item => item.id === product.id)

  if (existing) {
    existing.qty += 1
    alert(`${product.title} quantity increased in cart`)
  } else {
    cart.value.push({ ...product, qty: 1 })
    alert(`${product.title} added to cart`)
  }
}

// remove cart item
export const removeFromCart = (id) => {
  cart.value = cart.value.filter(item => item.id !== id)
}

// quantity update
export const updateQty = (id, type) => {
  const item = cart.value.find(i => i.id === id)
  if (!item) return

  if (type === 'inc') item.qty++
  if (type === 'dec' && item.qty > 1) item.qty--
}

// wishlist toggle
export const toggleWishlist = (product) => {
  const exists = wishlist.value.find(item => item.id === product.id)

  if (exists) {
    wishlist.value = wishlist.value.filter(item => item.id !== product.id)
    
  } else {
    wishlist.value.push(product)
    
  }
}

// remove wishlist item
export const removeFromWishlist = (id) => {
  wishlist.value = wishlist.value.filter(item => item.id !== id)
}

// check if in wishlist
export const isInWishlist = (id) => {
  return wishlist.value.some(item => item.id === id)
}

  // total selected products only
  export const cartCount = () => {
    return cart.value.length
}
