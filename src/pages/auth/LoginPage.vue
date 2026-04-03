<template>
  <div class="card">

    <h3>Login</h3>
    <p class="sub">Welcome back! Login to continue shopping</p>

    <input type="email" placeholder="Email Address" />
    <input type="password" placeholder="Password" />

    <button class="btn">LOGIN</button>

    <p class="switch">
      Don’t have an account?
      <span @click="$router.push('/signup')">Sign Up</span>
    </p>

  </div>
</template>

<style lang="scss">
@import 'src/css/login.scss';
</style>
