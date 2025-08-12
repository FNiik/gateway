<script setup>
import sidebar from './components/sidebar.vue';
</script>

<template>
  <div class="layout">
    <sidebar />
    <RouterView />
  </div>
</template>


<style scoped>
.layout {
  display: flex;
}
</style>


