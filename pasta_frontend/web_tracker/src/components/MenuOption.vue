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
  <button class="menu-item" @click="`${$router.push(route)}`">
    <i :class="iconClass"></i>
  </button>
</template>

<style scoped>
.menu-item {
  width: 70px;
  height: 70px;
  border-radius: 100px;
  background-color: #dddcdc;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: inset 0px 4px 6.9px rgba(0, 0, 0, 0.07);
  cursor: pointer;
  text-decoration: none;
  border: none;
}

.menu-item i {
  font-size: 33px; /* Adjust the icon size as needed */
  color: #5d595a;
}
</style>
