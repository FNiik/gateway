<!-- App.vue -->
 <script setup>
 import Sidebar from './components/sidebar.vue';
 </script>
 
 <template>
   <div class="sidebarPage">
    <div class="layout">
      <Sidebar />
     <div class="page">
       <RouterView />
     </div>
   </div>


   </div>
 </template>
 
  <style scoped>
 .layout {
   display: flex;
   min-height: 100vh; 
   background-color: #F9FAFC;
   width: 100%;
    
 }
 
 .page {
  flex-grow: 1;
   display: flex;
   /* flex-direction: column; */
   background-color: #F9FAFC; 
   /* padding: 20px; */
   /* margin-left: 150px; */
   margin-left: 120px;
    overflow-x: hidden;
   
  
   
   
   
 }
 .sidebarPage{
  display: flex;
 }
 @media (max-width: 768px) {
  
  .page{
    margin-left: 0px;
  }
 }
 </style>
  