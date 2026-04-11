<template>
  <div class="sort-wrapper">

    <div class="sort-box" @click="toggle">
      <span>SORT BY: {{ label }}</span>
      <span class="arrow" @click.stop="toggle">▼</span>
    </div>

    <div v-if="open" class="sort-dropdown">
      
      <div @click="select('bestseller')">BEST SELLING</div>
      <div @click="select('low')">LOW PRICE</div>
      <div @click="select('high')">HIGH PRICE</div>
    </div>

  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  modelValue: String
})

const emit = defineEmits(['update:modelValue'])

const open = ref(false)

const toggle = () => {
  open.value = !open.value
}

const select = (val) => {
  emit('update:modelValue', val)
  open.value = false
}

const label = computed(() => {
  if (props.modelValue === 'low') return 'LOW PRICE'
  if (props.modelValue === 'high') return 'HIGH PRICE'
  if (props.modelValue === 'bestseller') return 'BEST SELLING'
  return 'MOST POPULAR'
})
</script>

<style scoped>
.sort-box {
  cursor: pointer;
  display: flex;
  gap: 6px;
  align-items: center;
}

.arrow {
  cursor: pointer;
}

.sort-wrapper {
  position: relative;
}

.sort-dropdown {
  position: absolute;
  right: 0;
  top: 25px;
  background: white;
  border: 1px solid #ddd;
  width: 180px;
  border-radius: 6px;
  z-index: 1000;
}

.sort-dropdown div {
  padding: 10px;
  cursor: pointer;
}

.sort-dropdown div:hover {
  background: #f5f5f5;
}
</style>