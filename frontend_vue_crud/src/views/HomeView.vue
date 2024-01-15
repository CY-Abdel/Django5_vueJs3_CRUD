<template>
  <img src="../assets/vue.svg" alt="vue logo">
  <div class="home">
    <HelloWorld msg="Bienvenue dans Vue.Js" />
  </div>
</template>

<script setup>
import HelloWorld from '../components/HelloWorld.vue';
</script>

<style scoped>
.home {
  height: 80vh;
  display: flex;
  flex-direction: column;
  align-items: start;
  justify-content: start;
}
</style>
