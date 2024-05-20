<script setup>
defineProps({
  iconClass: {
    type: String,
    required: true
  },
  route: {
    type: String,
    required: true
  }
})
</script>

<template>
  <RouterLink class="menu-item" :to="route">
    <i :class="iconClass"></i>
  </RouterLink>
</template>

<style scoped>
.menu-item {
  width: 70px;
  height: 70px;
  border-radius: 100px;
  background-color: #DDDCDC;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: inset 0px 4px 6.9px rgba(0, 0, 0, 0.07);
  cursor: pointer;
  text-decoration: none;
}

.menu-item i {
  font-size: 33px; /* Adjust the icon size as needed */
  color: #5D595A;
}
</style>
