<template>
  <div class="login-page">
    <div class="login-card">
      <h3 class="login-title">Login</h3>
      <p class="login-sub">Welcome back! Login to continue shopping</p>

      <input class="login-input" type="email" placeholder="Email Address" />
      <input class="login-input" type="password" placeholder="Password" />

      <button class="login-btn">LOGIN</button>

      <p class="login-switch">
        Don’t have an account?
        <span @click="$router.push('/signup')">Sign Up</span>
      </p>
    </div>
  </div>
</template>

<style scoped lang="scss">
@import 'src/css/login.scss';
</style>