<template>
  <div class="bg-parchment">
    <EntityListEntry v-for="playerCharacter in state.playerCharacters" :key="playerCharacter._id.$oid"
      :playerCharacter="playerCharacter" />
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
import { reactive, inject, watch } from 'vue';
import EntityListEntry from './EntityListEntry.vue';

const state = reactive({
  playerCharacters: [],
  pageNumber: 0
})

watch(() => state.pageNumber, () => {
  if (state.pageNumber < 0) {
    state.pageNumber = 0;
  }
  getPlayerCharacterList(state.pageNumber);
});

const axios = inject('axios');
function getPlayerCharacterList(pageNumber) {
  const path = '/playerCharacters?page=' + pageNumber
  axios.get(path)
    .then(res => {
      state.playerCharacters = res.data;
    })
    .catch(error => {
      console.error(error);
    })
}

getPlayerCharacterList(state.pageNumber);

</script>