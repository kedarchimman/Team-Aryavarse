<template>
  <div class="card">

    <h3>Sign Up</h3>
    <p class="sub">Create your account to start shopping</p>

    <input placeholder="Full Name" />
    <input type="Phone" placeholder="Phone Number" />
    <input type="email" placeholder="Email Address" />
    <input type="password" placeholder="Password" />
    

    <button class="btn">CREATE ACCOUNT</button>

    <p class="switch">
      Already have an account?
      <span @click="$router.push('/login')">Login</span>
    </p>

  </div>
</template>

<style lang="scss">
@import 'src/css/sign.scss';
</style>