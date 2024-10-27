<template>
  <div class="bg-primary">
    <EntityListEntry v-for="entity in state.entities" :key="entity._id.$oid"
      :entity="entity" />
  </div>
  <!-- Previous / next page buttons -->
  <!-- Icons from https://www.streamlinehq.com/icons/streamline-flat-free -->
  <div class="flex grow justify-center gap-4">
    <button @click="state.pageNumber = 0">
      <img src="../assets/icons/arrow-first.svg" class="">
    </button>
    <button @click="state.pageNumber = state.pageNumber - 1">
      <img src="../assets/icons/arrow-left.svg" class="">
    </button>
    <button @click="state.pageNumber = state.pageNumber + 1">
      <img src="../assets/icons/arrow-right.svg" class="">
    </button>
    <button @click="state.pageNumber = 0">
      <img src="../assets/icons/arrow-last.svg" class="">
    </button>
  </div>
</template>

<script setup>
import { inject, reactive, watch } from 'vue';
import EntityListEntry from './EntityListEntry.vue';

const state = reactive({
  entities: [],
  pageNumber: 0
})

watch(() => state.pageNumber, () => {
  if (state.pageNumber < 0) {
    state.pageNumber = 0;
  }
  getEntityList(state.pageNumber);
});

const axios = inject('axios');
function getEntityList(pageNumber) {
  const path = '/entities?page=' + pageNumber
  axios.get(path)
    .then(res => {
      state.entities = res.data;
    })
    .catch(error => {
      console.error(error);
    })
}

getEntityList(state.pageNumber);

</script>