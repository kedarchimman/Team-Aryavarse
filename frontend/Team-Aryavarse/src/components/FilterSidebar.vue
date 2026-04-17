<template>
  <div class="filter-wrapper">
    <!-- DESKTOP: Normal sidebar (visible >= 1001px) -->
    <aside class="filters-sidebar desktop-filters">
      <h2>Filters</h2>

      <div class="filter-group">
        <p>Category</p>
        <label v-for="c in filterCategories" :key="c" class="filter-label">
          <input type="checkbox" :value="c" :checked="selectedCategories.includes(c)" @change="toggle('categories', c)" />
          {{ c }}
        </label>
      </div>

      <div class="filter-group">
        <p>Fabric</p>
        <label v-for="f in fabrics" :key="f" class="filter-label">
          <input type="checkbox" :value="f" :checked="selectedFabrics.includes(f)" @change="toggle('fabrics', f)" />
          {{ f }}
        </label>
      </div>

      <div class="filter-group">
        <p>Style</p>
        <label v-for="s in sleeves" :key="s" class="filter-label">
          <input type="checkbox" :value="s" :checked="selectedSleeves.includes(s)" @change="toggle('sleeves', s)" />
          {{ s }}
        </label>
      </div>

      <div class="filter-group">
        <p>Color</p>
        <label v-for="color in colors" :key="color" class="filter-label">
          <input type="checkbox" :value="color" :checked="selectedColors.includes(color)" @change="toggle('colors', color)" />
          {{ color }}
        </label>
      </div>
    </aside>

    <!-- MOBILE: Bottom sticky bar + drawer (visible <= 1000px) -->
<div class="mobile-filter-bar">

  <button class="mobile-action-btn" @click="drawerOpen = !drawerOpen">
    <span>⚙</span>
    Filter
    <span v-if="activeCount > 0" class="active-badge">{{ activeCount }}</span>
  </button>

  <div class="divider"></div>

  <div class="mobile-sort-slot">
    <slot name="sort-btn" />
  </div>

</div>

    <!-- MOBILE Overlay -->
    <div class="filter-overlay" :class="{ open: drawerOpen }" @click="drawerOpen = false" />

    <!-- MOBILE Drawer -->
    <div class="filter-drawer" :class="{ open: drawerOpen }">
      <div class="drawer-header">
        <span class="drawer-title">Filters</span>
        <button class="drawer-close" @click="drawerOpen = false">✕</button>
      </div>

      <div class="drawer-body">
        <div class="filter-group">
          <p>Category</p>
          <label v-for="c in filterCategories" :key="c" class="filter-label">
            <input type="checkbox" :value="c" :checked="selectedCategories.includes(c)" @change="toggle('categories', c)" />
            {{ c }}
          </label>
        </div>

        <div class="filter-group">
          <p>Fabric</p>
          <label v-for="f in fabrics" :key="f" class="filter-label">
            <input type="checkbox" :value="f" :checked="selectedFabrics.includes(f)" @change="toggle('fabrics', f)" />
            {{ f }}
          </label>
        </div>

        <div class="filter-group">
          <p>Style</p>
          <label v-for="s in sleeves" :key="s" class="filter-label">
            <input type="checkbox" :value="s" :checked="selectedSleeves.includes(s)" @change="toggle('sleeves', s)" />
            {{ s }}
          </label>
        </div>

        <div class="filter-group">
          <p>Color</p>
          <label v-for="color in colors" :key="color" class="filter-label">
            <input type="checkbox" :value="color" :checked="selectedColors.includes(color)" @change="toggle('colors', color)" />
            {{ color }}
          </label>
        </div>
      </div>

      <div class="drawer-footer">
        <button class="clear-btn" @click="clearAll">Clear All</button>
        <button class="apply-btn" @click="drawerOpen = false">Apply Filters</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  filterCategories: { type: Array, default: () => [] },
  fabrics:          { type: Array, default: () => [] },
  sleeves:          { type: Array, default: () => [] },
  colors:           { type: Array, default: () => [] },
  selectedCategories: { type: Array, default: () => [] },
  selectedFabrics:    { type: Array, default: () => [] },
  selectedSleeves:    { type: Array, default: () => [] },
  selectedColors:     { type: Array, default: () => [] },
})

const emit = defineEmits([
  'update:selectedCategories',
  'update:selectedFabrics',
  'update:selectedSleeves',
  'update:selectedColors',
])

const drawerOpen = ref(false)

const activeCount = computed(() =>
  props.selectedCategories.length +
  props.selectedFabrics.length +
  props.selectedSleeves.length +
  props.selectedColors.length
)

function toggle(type, value) {
  const map = {
    categories: { arr: props.selectedCategories, event: 'update:selectedCategories' },
    fabrics:    { arr: props.selectedFabrics,    event: 'update:selectedFabrics'    },
    sleeves:    { arr: props.selectedSleeves,    event: 'update:selectedSleeves'    },
    colors:     { arr: props.selectedColors,     event: 'update:selectedColors'     },
  }
  const { arr, event } = map[type]
  const updated = arr.includes(value)
    ? arr.filter(v => v !== value)
    : [...arr, value]
  emit(event, updated)
}

function clearAll() {
  emit('update:selectedCategories', [])
  emit('update:selectedFabrics', [])
  emit('update:selectedSleeves', [])
  emit('update:selectedColors', [])
}
</script>

<style scoped lang="scss">
@import 'src/css/filters.scss';
</style>