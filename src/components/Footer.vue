<template>
  <footer class="flex px-4 py-8 bg-gray-800">
      <div class="basis-4/5 mx-auto">
          <router-link class="text-white px-4 py-2 mx-2 text-lg rounded bg-rose-500 hover:text-white hover:bg-amber-300" :to="'/the-loai/'+kind" v-for="kind, index in kinds" :key="'kind-' + index">{{kind}}</router-link>
          <p class="text-center text-white py-2 ">© Copyright 2023 Vite-Vue. All rights reserved.</p>
      </div>
  </footer>
</template>

<script setup>
    const kinds = ['aaa', 'bbb', 'ccc']
</script>

<style>

</style>