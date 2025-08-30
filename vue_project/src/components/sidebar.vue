<!-- sidebar.vue -->
<script setup>

</script>


<template>
    <div class="sidebar">
        <div class="sidebar-header">
            <div class="logoicon">
                <img src="" alt=""></img>
            </div>
            <div class="logo-text">
                <h2>Gateway</h2>
                <p>Management system</p>
            </div>

        </div>
        <nav class="sidebar-nav">
            <h4>Navigation</h4>
            <ul>
                <li> <RouterLink to="/"  class="navlink" >Gateways</RouterLink></li>
            </ul>
        </nav>


       
    </div>
</template>

<style scoped>
.sidebar {
    width: 230px;
    height: 100vh;
    background-color:#FAFAFA;
    padding: 20px;
    display: flex;
    flex-direction: column;
    /* position: fixed;  */
    
    border-right: 1px solid #ddd;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
   
}
.sidebar-header {
    display: flex;
    align-items: center;
    padding-bottom: 40px;
    
}
.logoicon{
  background-color: #3b4cca; 
  border-radius: 10px;
  width: 48px;
  height: 48px;
  margin-right: 15px;
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  font-weight: bold;
  font-size: 24px;
}

</style>