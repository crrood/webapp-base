<template>
  <div class="bg-primary">
    <EntityListEntry v-for="entity in state.entities" :key="entity._id.$oid"
      :entity="entity" />
  </div>
  <!-- Previous / next page buttons -->
  <!-- Icons from https://www.flaticon.com/uicons/get-started -->
  <!-- Need to be attributed if I end up releasing this -->
  <div class="flex grow justify-center gap-10">
    <button @click="state.pageNumber = 0">
      <img  class="w-10" src="../assets/icons/uicons-regular-straight/svg/fi-rs-arrow-to-left.svg">
    </button>
    <button @click="state.pageNumber = state.pageNumber - 1">
      <img  class="w-10" src="../assets/icons/uicons-regular-straight/svg/fi-rs-arrow-left.svg">
    </button>
    <button @click="state.pageNumber = state.pageNumber + 1">
      <img  class="w-10" src="../assets/icons/uicons-regular-straight/svg/fi-rs-arrow-right.svg">
    </button>
    <button @click="state.pageNumber = 0">
      <img  class="w-10" src="../assets/icons/uicons-regular-straight/svg/fi-rs-arrow-to-right.svg">
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
  const path = '/entity?page=' + pageNumber
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