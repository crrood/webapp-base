<template>
  <div class="flex place-items-center space-x-6 m-4 p-4" 
      @click="router.push({ 
      name: 'Entity',
      params: { id: entity._id.$oid, entity: JSON.stringify(entity) }})">
      <div class="text-white">
        <div class="text-bold">EntityListEntry:</div>
        {{ entity }}
      </div>
  </div>
</template>

<script setup>
import router from '../router';

defineProps(['entity']);
</script>