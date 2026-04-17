<template>
  <div class="profile-page">
    <div class="profile-card">

      <!-- Avatar -->
      <div class="avatar-circle">
        {{ initials }}
      </div>

      <!-- User info -->
      <h2 class="profile-name">{{ displayName }}</h2>
      <p class="profile-email">{{ user?.email || '—' }}</p>

      <div class="profile-divider" />

      <!-- Details -->
      <div class="profile-details">
        <div class="detail-row">
          <q-icon name="person" size="18px" class="detail-icon" />
          <span class="detail-label">Name</span>
          <span class="detail-value">{{ displayName }}</span>
        </div>

        <div class="detail-row">
          <q-icon name="mail" size="18px" class="detail-icon" />
          <span class="detail-label">Email</span>
          <span class="detail-value">{{ user?.email || '—' }}</span>
        </div>

        <div class="detail-row">
          <q-icon name="verified_user" size="18px" class="detail-icon" />
          <span class="detail-label">Account</span>
          <span class="detail-value verified">Verified ✓</span>
        </div>
      </div>

      <div class="profile-divider" />

      <!-- Quick links -->
      <div class="profile-links">
        <div class="profile-link" @click="$router.push('/cart')">
          <span class="link-icon" style="background:#EEF3FF">
            <q-icon name="shopping_cart" size="18px" style="color:#5b8cde" />
          </span>
          <span>My Cart</span>
          <q-icon name="chevron_right" size="18px" class="chevron" />
        </div>
        <div class="profile-link" @click="$router.push('/wishlist')">
          <span class="link-icon" style="background:#FFF0F7">
            <q-icon name="favorite" size="18px" style="color:#e06aa0" />
          </span>
          <span>My Wishlist</span>
          <q-icon name="chevron_right" size="18px" class="chevron" />
        </div>
        <div class="profile-link" @click="$router.push('/')">
          <span class="link-icon" style="background:#FFF8E8">
            <q-icon name="storefront" size="18px" style="color:#e09040" />
          </span>
          <span>Continue Shopping</span>
          <q-icon name="chevron_right" size="18px" class="chevron" />
        </div>
      </div>

      <div class="profile-divider" />

      <!-- Logout -->
      <button class="logout-btn" @click="handleLogout">
        <q-icon name="logout" size="18px" />
        Logout
      </button>

    </div>
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from 'src/stores/auth'

const router = useRouter()
const authStore = useAuthStore()

// ✅ Protect route
onMounted(() => {
  if (!authStore.token) {
    router.push('/login')
  }
})

// ✅ user data
const user = computed(() => authStore.user)

// ✅ display name
const displayName = computed(() => {
  return user.value?.name
    || user.value?.email?.split('@')[0]
    || 'User'
})

// ✅ initials
const initials = computed(() => {
  const n = displayName.value
  const parts = n.trim().split(' ')
  if (parts.length >= 2) {
    return (parts[0][0] + parts[1][0]).toUpperCase()
  }
  return n.slice(0, 2).toUpperCase()
})

// ✅ logout
function handleLogout() {
  const idToken = authStore.id_token

  authStore.logout()

  if (idToken) {
    window.location.href =
      `http://localhost:8000/auth/logout?id_token_hint=${idToken}`
  } else {
    router.push('/login')
  }
}
</script>

<style scoped>
/* ══════════════════════════════════════
   CSS VARIABLES & PAGE BASE
══════════════════════════════════════ */
.profile-page {
  --teal:    #1a7a6e;
  --teal-lt: #e6f5f2;
  --border:  #e8e8e8;
  --text:    #1a1a1a;
  --muted:   #888;
  --r:       14px;
  --shadow:  0 2px 12px rgba(0,0,0,0.06);

  min-height: 80vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 16px;
  background: linear-gradient(160deg, #eaf6f3 0%, #f5fffd 50%, #f8f8f8 100%);

  animation: pageFadeIn 0.4s ease both;
}

@keyframes pageFadeIn {
  from { opacity: 0; transform: translateY(12px); }
  to   { opacity: 1; transform: translateY(0); }
}

/* ══════════════════════════════════════
   PROFILE CARD
══════════════════════════════════════ */
.profile-card {
  background: #fff;
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 40px 32px;
  width: 100%;
  max-width: 440px;
  box-shadow: var(--shadow);
  display: flex;
  flex-direction: column;
  align-items: center;

  animation: cardSlideUp 0.45s cubic-bezier(0.22, 1, 0.36, 1) both;
}

@keyframes cardSlideUp {
  from { opacity: 0; transform: translateY(24px) scale(0.98); }
  to   { opacity: 1; transform: translateY(0) scale(1); }
}

/* ══════════════════════════════════════
   AVATAR
══════════════════════════════════════ */
.avatar-circle {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: linear-gradient(135deg, #1a7a6e, #2dbbaa);
  color: #fff;
  font-size: 28px;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 16px;
  box-shadow: 0 6px 20px rgba(26,122,110,0.30);
  transition: transform 0.25s ease, box-shadow 0.25s ease;
  animation: avatarPop 0.5s cubic-bezier(0.34, 1.56, 0.64, 1) 0.15s both;
}

@keyframes avatarPop {
  from { opacity: 0; transform: scale(0.6); }
  to   { opacity: 1; transform: scale(1); }
}

.avatar-circle:hover {
  transform: scale(1.06);
  box-shadow: 0 10px 28px rgba(26,122,110,0.38);
}

/* ══════════════════════════════════════
   NAME & EMAIL
══════════════════════════════════════ */
.profile-name {
  font-size: 20px;
  font-weight: 700;
  color: var(--text);
  margin: 0 0 4px;
}

.profile-email {
  font-size: 14px;
  color: var(--muted);
  margin: 0;
}

/* ══════════════════════════════════════
   DIVIDER
══════════════════════════════════════ */
.profile-divider {
  width: 100%;
  height: 1px;
  background: var(--border);
  margin: 20px 0;
}

/* ══════════════════════════════════════
   DETAIL ROWS
══════════════════════════════════════ */
.profile-details {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.detail-row {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 14px;
  padding: 10px 12px;
  border-radius: var(--r);
  transition: background 0.15s;
}

.detail-row:hover { background: var(--teal-lt); }

.detail-icon { color: var(--muted); flex-shrink: 0; }

.detail-label {
  color: var(--muted);
  width: 60px;
  flex-shrink: 0;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.4px;
  text-transform: uppercase;
}

.detail-value {
  color: var(--text);
  font-weight: 500;
}

.detail-value.verified { color: #1a7a6e; font-weight: 600; }

/* ══════════════════════════════════════
   QUICK LINKS
══════════════════════════════════════ */
.profile-links {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.profile-link {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 12px 8px;
  border-radius: var(--r);
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
  color: var(--text);
  transition: background 0.15s, transform 0.15s;
}

.profile-link:hover {
  background: var(--teal-lt);
  transform: translateX(3px);
}

.link-icon {
  width: 34px;
  height: 34px;
  border-radius: 10px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.profile-link .chevron { margin-left: auto; color: #ccc; transition: transform 0.15s; }
.profile-link:hover .chevron { transform: translateX(3px); color: var(--teal); }

/* ══════════════════════════════════════
   LOGOUT BUTTON
══════════════════════════════════════ */
.logout-btn {
  margin-top: 4px;
  width: 100%;
  padding: 13px;
  border: none;
  border-radius: 12px;
  background: #fff0f0;
  color: #c0392b;
  font-size: 15px;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  transition: background 0.15s, transform 0.15s, box-shadow 0.15s;
}

.logout-btn:hover {
  background: #ffd7d7;
  transform: translateY(-1px);
  box-shadow: 0 4px 14px rgba(192,57,43,0.15);
}

.logout-btn:active {
  transform: scale(0.98);
}
</style>