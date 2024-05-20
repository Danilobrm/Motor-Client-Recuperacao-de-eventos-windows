<script setup>
import TableRow from './TableRow.vue'

defineProps({
  colaboradores: {
    type: Array,
  },
})
// import colaboradores from '../data/websocket.js';


</script>

<template>
  <div class="table_colaborators">
    <table>
      <thead>
        <tr>
          <th>Colaborador</th>
          <th>Status</th>
          <th>IPv4</th>
          <th>Atividade</th>
        </tr>
      </thead>
      <tbody>
        <tr class="table-row" v-for="(colaborador, index) in colaboradores" :key="index">
          <TableRow :colaborador="colaborador" />
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style>
.table_colaborators {
  min-height: 200px;
  overflow: hidden;
}

tr {
  overflow-y: scroll;
}

.table_colaborators table {
  width: 100%;
  font-family: 'montserrat';
}

.row {
  height: 19px;
  border-top: 2px solid #f2f2f2;
}

th:nth-child(1) {
  padding-bottom: 19px;
}

th:nth-child(1) {
  text-align: left;
}

th {
  text-align: center;
}
</style>
