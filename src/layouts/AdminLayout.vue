<template>
  <q-layout view="lHh Lpr lFf">

    <!-- Sidebar -->
    <q-drawer show-if-above bordered>
      <Sidebar />
    </q-drawer>

    <!-- Navbar -->
    <q-header elevated>
      <Navbar />
    </q-header>

    <!-- Page Content -->
    <q-page-container>
      <router-view />
    </q-page-container>

  </q-layout>
</template>

<script setup>
import Sidebar from '../components/admin/Sidebar.vue'
import Navbar from '../components/admin/Navbar.vue'
</script>