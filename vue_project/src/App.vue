<!-- <script setup>
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

 -->
 <script setup>
 import Sidebar from './components/sidebar.vue';
 </script>
 
 <template>
   <div class="layout">
     <Sidebar />
     <div class="page">
       <RouterView />
     </div>
   </div>
 </template>
 
 <style scoped>
 .layout {
   display: flex;
   min-height: 100vh; 
   background-color: #F9FAFC;
    
 }
 
 .page {
   flex-grow: 1;
   display: flex;
   flex-direction: column;
   background-color: #F9FAFC; 
   /* padding: 20px; */
   /* margin-left: 140px; */
 }

 </style>
 