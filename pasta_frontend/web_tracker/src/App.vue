<script setup>
// import AdmMonitor from './views/AdmMonitor.vue';
import SideMenu from './components/SideMenu.vue'
</script>

<template>
    <div id="container">
      <SideMenu />
    </div>
</template>

<style scoped>
  #container {
    display: flex;
    flex-direction: row;
    height: 100vh;
    overflow-x: hidden
  }
</style>
