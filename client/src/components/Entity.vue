<template>
  <div class="grid justify-center mt-4 bg-parchment">
    <div class="grid grid-cols-12 gap-y-4 font-black-chancery max-w-5xl">
      <!-- Character Photo -->
      <div class="col-span-4 flex justify-center h-96">
        <img class="rounded-full max-w-full" :src='state.character.photo.fullsize'>
      </div>
      <div class="col-span-8 grid grid-cols-12 grid-rows-6">
        <input type="text" class="col-span-12 row-span-2 font-beyond-wonderland text-center text-7xl" v-model="
          state.character.name" disabled>
        <!-- Physical Details -->
        <div class="col-span-12 row-span-4 flex flex-wrap gap-x-12 justify-evenly p-5">
          <span v-for="(value, name) in state.character.details" :key="name">
            <label class="capitalize">{{ name }}: </label>
            <input type="text" class="text-center" size=15 v-model="state.character.details[name]" disabled>
          </span>
        </div>
      </div>
      <!-- Stats -->
      <div class="col-span-12 flex justify-evenly gap-x-12">
        <span v-for="(value, name) in state.character.stats"
          class="p-2 w-24 rounded-md border-2 border-black text-center">
          <input type="number" class="w-full oldstyle-nums font-bold text-xl text-center" max-length=2 size=2
            v-model="state.character.stats[name]" disabled>
          <hr class="invisible">
          <label class="font-semibold capitalize">{{ name }}</label>
        </span>
      </div>
      <!-- Personality and beliefs -->
      <div class="col-span-12 grid grid-cols-12 gap-4 p-3">
        <span v-for="(value, name) in state.character.personality" class="col-span-4 grid grid-cols-1">
          <label class="capitalize">{{ name }}: </label>
          <textarea class="resize-none border p-1 text-left focus:border-black focus:ring-0"
            v-model="state.character.personality[name]" disabled></textarea>
        </span>
      </div>
    </div>

    <!-- Edit / save -->
    <div class="flex justify-center py-2 gap-x-4">
      <button v-if="characterOwnedByUser" class='btn-primary w-24' @click='editBtnClicked'>
        {{ state.editing ? 'Save' : 'Edit' }}
      </button>
    </div>
  </div>
</template>

<script setup>
import { useAuth0 } from '@auth0/auth0-vue';
import { inject, reactive, computed } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const auth0 = useAuth0();

// reactive state
const state = reactive({
  editing: false,
  character: {
    photo: {
      thumbnail: '',
      fullsize: ''
    }
  },
  user: auth0.user
});

const characterOwnedByUser = computed(() => {
  return state.user && state.character.auth0Id === state.user.sub
});

// initialize
const axios = inject('axios');
if (route.params.playerCharacter) {
  state.character = JSON.parse(route.params.playerCharacter);
}
else {
  getCharacter(route.params.id);
}

// methods
function getCharacter(characterId) {
  const path = '/playerCharacters/' + characterId;
  axios.get(path)
    .then(res => {
      state.character = res.data;
    })
    .catch(error => {
      console.error(error);
    })
}

function editBtnClicked() {
  if (state.editing) {
    saveCharacter();
  }
  toggleInputs();
  state.editing = !state.editing;
}

function toggleInputs() {
  const inputs = document.querySelectorAll('input');
  inputs.forEach(input => {
    input.disabled = !input.disabled;
  });
  const textareas = document.querySelectorAll('textarea');
  textareas.forEach(textarea => {
    textarea.disabled = !textarea.disabled;
  });
}

function saveCharacter() {
  const path = '/playerCharacters/' + state.character._id.$oid;
  axios.put(path, state.character)
    .then(res => {
      console.log(res.data);
    })
    .catch(error => {
      console.error(error);
    })
}

</script>