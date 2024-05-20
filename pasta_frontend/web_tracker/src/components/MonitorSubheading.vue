<script setup>
import { ref } from 'vue'
// import colaboradores from '../data/WebsocketConnection.vue'
// import ColaboratorsTable from './ColaboratorsTable.vue';

const tags = ['Favoritos', 'Todos', 'Arquivados']
const selectedTag = ref(tags[0])

const selectTag = (tag) => {
  selectedTag.value = tag
}

defineProps({
  amount: {
    type: Number,
  },
})

</script>

<template>
  <div class="subheading">
    <div class="tag-selector">
      <p
        v-for="(tag, index) in tags"
        :key="index"
        :class="{ selected: selectedTag === tag }"
        @click="selectTag(tag)"
      >
        {{ tag }}
      </p>
    </div>
    <div>
      <p class="colaborators-amount">Colaboradores Registrados: <label>{{ amount || 0 }}</label></p>
    </div>
  </div>
</template>

<style>
.subheading {
  display: flex;
  justify-content: space-between;
  margin: 26px 0 30px 0;
}

.tag-selector {
  display: flex;
  gap: 37px;
}

.tag-selector p {
  cursor: pointer;
  font-family: 'montserrat-italic';
  color: #bcbcbc;
}

.tag-selector p.selected {
  position: relative;
}

.tag-selector p.selected::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 48px;
  height: 3px;
  border-radius: 1px;
  background-color: #6153b9;
  bottom: -5px;
}

.colaborators-amount {
  font-family: "montserrat-italic";
  font-weight: 600;
  color: #BCBCBC;
  display: flex;
}

.colaborators-amount label {
  font-weight: 700;
  color: #5D595A;
  margin-left: 5px;
}
</style>
