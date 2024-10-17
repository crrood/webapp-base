<template>
  <div class="flex place-items-center space-x-6 m-4 p-4 hover:bg-parchment-dark cursor-pointer" 
      @click="router.push({ 
      name: 'PlayerProfile',
      params: { id: playerCharacter._id.$oid, playerCharacter: JSON.stringify(playerCharacter) }})">
    <img class="rounded-full w-32" :src='playerCharacter.photo.thumbnail'>
    <p class="font-beyond-wonderland text-center text-5xl">{{ playerCharacter.name }}</p>
    <div class="flex grow place-items-center justify-end space-x-6 font-black-chancery">
      <p class="text-center text-2xl">{{ playerCharacter.details.race }}</p>
      <p class="text-center text-2xl">{{ playerCharacter.details.class }}</p>
    </div>
  </div>
</template>

<script setup>
import router from '../router';

defineProps(['playerCharacter']);
</script>