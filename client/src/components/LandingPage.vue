<template>
  <div>
    <p>{{ state.response }}</p>
  </div>
</template>

<script setup>
import { inject, onMounted, reactive } from 'vue';

// reactive state
const state = reactive({
  response: "Loading..."
});

// methods
const axios = inject('axios');
onMounted(() => {
  const path = '/';
  axios.get(path)
    .then(res => {
      state.response = res.data;
    })
    .catch(error => {
      console.error(error);
    })
})

// lifecycle hooks

</script>