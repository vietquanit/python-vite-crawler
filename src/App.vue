<script setup>
  import Header from "./components/Header.vue"
  import UpButton from "./components/UpButton.vue"
  import Footer from "./components/Footer.vue"
</script>
<template>
  <!-- <div> -->
    <Header></Header>
    <UpButton />
    <router-view></router-view>
    <Footer />
  <!-- </div> -->
</template>

<style scoped>
</style>
