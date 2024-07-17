<script setup>
import { ref } from 'vue'
const selected = ref(false)

defineProps({
  colaborador: {
    type: Object,
    required: true
  }
})
</script>

<template>
  <button
    @click="
      $router.push({
        name: `colaborador`,
        params: { username: colaborador.user.username }
      })
    "
    class="colaborator"
  >
    <td class="name">
      {{ colaborador.user.username }}
      <p>{{ colaborador.user.role || 'desenvolvedor' }}</p>
    </td>
  </button>
  <td class="status">
    <p :class="colaborador.status">{{ colaborador.status }}</p>
  </td>
  <td class="ip">{{ colaborador.user.ipv4_address }}</td>
  <td v-if="colaborador.programs[colaborador.programs.length - 1].name" class="activity">
    {{ colaborador.programs[colaborador.programs.length - 1].name }}
  </td>

  <td class="bookmark" @click="selected = !selected">
    <p><i :class="[selected ? 'fa fa-bookmark' : 'fa-regular fa-bookmark']"></i></p>
  </td>
</template>

<style>
.online {
  background-color: #abf6b2;
}

.idle {
  background-color: #f2f2f2;
}

.offline {
  background-color: #ffc4c4;
}

td {
  color: #5d595a;
  text-align: center;
  height: 48px;
}

.name {
  font-family: 'montserrat-italic';
  text-align: left;
  font-weight: 600;
}

.colaborator {
  text-decoration: none;
  background-color: transparent;
  border: none;
  cursor: pointer;
}

.status {
  color: #5d595a;
}

.bookmark {
  width: 100px;
  text-align: end;
}
/* 
.ip {
  width: fit-content;
}
*/

.activity {
  width: 300px;
}

.status p {
  width: 121px;
  height: 24px;
  border-radius: 205px;
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto;
}

td:nth-child(1) p {
  font-family: 'montserrat';
  font-style: italic;
  font-weight: 400;
}

p {
  color: #9f989a;
}
</style>
