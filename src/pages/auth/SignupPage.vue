<template>
  <div class="signup-page">
    <div class="signup-card">
      <h3 class="signup-title">Sign Up</h3>
      <p class="signup-sub">Create your account to start shopping</p>

      <input class="signup-input" placeholder="Full Name" />
      <input class="signup-input" type="tel" placeholder="Phone Number" />
      <input class="signup-input" type="email" placeholder="Email Address" />
      <input class="signup-input" type="password" placeholder="Password" />

      <button class="signup-btn">CREATE ACCOUNT</button>

      <p class="signup-switch">
        Already have an account?
        <span @click="$router.push('/login')">Login</span>
      </p>
    </div>
  </div>
</template>

<style scoped lang="scss">
@import 'src/css/sign.scss';
</style>