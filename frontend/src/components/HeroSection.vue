<template>
  <div class="hero">

    <div class="overlay">
      <h2>Professional Medical Apparel</h2>
      <p>Premium quality hospital wear</p>
      <q-btn label="Shop Now" color="primary" />
    </div>

  </div>
</template>

<style>
.hero {
  height: 400px;
  background: url('https://via.placeholder.com/1200x400') center/cover;
  position: relative;
}

.overlay {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
  text-align: center;
}
</style>