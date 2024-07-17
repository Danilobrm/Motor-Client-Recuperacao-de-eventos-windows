<script setup>
import MenuOption from './MenuOption.vue';
import { RouterView } from 'vue-router'
</script>

<template>
  <aside class="sideMenu">
    <nav class="nav">
      <MenuOption iconClass="fa fa-users" route="/" />
      <MenuOption iconClass="fa fa-smile" route="/under-construction" />
    </nav>
    <MenuOption iconClass="fa fa-gear" route="/config" />
  </aside>
  <RouterView />
</template>

<style>
.sideMenu {
  width: 132px;
  height: 100%;
  background-color: #ededed;
  display: flex;
  flex-direction: column;
  align-items: center;
  left: 0;
  justify-content: space-between;
  padding: 43px 0;
  position: fixed;
  top: 0;
}

.nav {
  display: flex;
  flex-direction: column;
  gap: 30px;
  text-decoration: none;
}
</style>
