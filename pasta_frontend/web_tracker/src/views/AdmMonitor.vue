<script>
import MonitorHeading from '../components/MonitorHeading.vue'
import MonitorSubheading from '../components/MonitorSubheading.vue'
import ColaboratorsTable from '../components/ColaboratorsTable.vue'

export default {
  components: {
    MonitorHeading,
    MonitorSubheading,
    ColaboratorsTable
  },
  data() {
    return {
      colaboradores: JSON.parse(localStorage.getItem("colaboradores")) || [],
      amount: 0
    }
  },
}
</script>

<template>
  <div class="monitor">
    <MonitorHeading heading="Colaboradores" />
    <MonitorSubheading :amount="colaboradores.length" />
    <ColaboratorsTable :colaboradores="colaboradores" />
  </div>
</template>

<style>
.monitor {
  /* margin: 52px 26px 52px calc(132px + 26px); */
  display: flex;
  flex-direction: column;
  width: 100%;
}
</style>
