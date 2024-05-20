<script setup>
defineProps({
  heading: {
    type: String,
    required: true
  }
})
</script>

<template>
  <header>
    <div>
      <h1>{{ heading }}</h1>
    </div>
    <div class="adm_profile_icon">
      <i class="fa-regular fa-user"></i>
      <div>
        <!-- <img :src="imageUrl" alt="Uploaded Image" /> -->
      </div>
    </div>
  </header>
</template>

<style>
header {
  display: flex;
  flex-direction: row;
  width: 100%;
  justify-content: space-between;
  align-items: flex-end;
}

h1 {
  font-size: 45px;
  font-family: 'montserrat-italic';
  color: #5d595a;
}

.adm_profile_icon {
  width: 150px;
  height: 67px;
  background-color: #F2F2F2;
  border-radius: 205px;
  display: flex;
  justify-content: flex-end;
  align-items: center;
}

.adm_profile_icon div {
  width: 48px;
  height: 48px;
  background-color: #000;
  border-radius: 100px;
  margin: 0 20px;
}

.adm_profile_icon i {
  font-size: 33px;
  color: #5D595A;
}
</style>
