<script>
// import AdmMonitor from './views/AdmMonitor.vue';
import SideMenu from './components/SideMenu.vue'
import webSocketConnection from './data/webSocketConnection'

export default {
  components: {
    SideMenu
  },
  data() {
    return {
      colaboradores: []
    }
  },
  created() {
    webSocketConnection(this.colaboradores);
  }
}
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
  overflow-x: hidden;
  padding: 52px 26px 52px calc(132px + 26px);
}
</style>
