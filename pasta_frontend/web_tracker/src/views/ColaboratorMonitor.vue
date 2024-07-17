<script setup>
import router from '@/router';



// import MonitorHeading from "../components/MonitorHeading.vue"
// import MonitorSubheading from "../components/MonitorSubheading.vue"
// import ColaboratorsTable from "../components/ColaboratorsTable.vue"

// defineProps({
//   colaborador: {
//     type: Object,
//     required: true
//   }
// })
console.log(router.options.history.state)
const colaborador = JSON.parse(localStorage.getItem("colaborador"))
// localStorage.removeItem(colaborador)

// JSON.parse()
</script>

<template>
  <div class="colaboratorMonitor">
    <div class="top-info">
      <span class="profile">
        <div class="pfp"></div>
        <div class="profile-info">
          <h1>{{colaborador.username}}</h1>
        </div>
      </span>
      <span class="program-in-use"></span>
      <span class="start-time"></span>
    </div>
  </div>
</template>

<style>
.colaboratorMonitor {
  /* margin: 52px 26px 52px calc(132px + 26px); */
  display: flex;
  flex-direction: column;
  width: 100%;
}

.top-info {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  border: 1px solid red;
  gap: 29px;
}

.profile {
  width: 440px;
  height: 109px;
  border-radius: 36px;
  background-color: '#EDEDED';
  border: 1px solid red;
  display: flex;
  align-items: center;
}

.pfp {
  width: 81px;
  height: 81px;
  background-color: black;
  border-radius: 100px;
  margin-left: 23px;
}

.program-in-use {
  width: 354px;
  height: 109px;
  border-radius: 36px;
  background-color: '#EDEDED';
  border: 1px solid red;
}

.start-time {
  width: 296px;
  height: 109px;
  border-radius: 36px;
  background-color: '#EDEDED';
  border: 1px solid red;
}
</style>
