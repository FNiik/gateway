<script setup>
import { PanelsLeftBottom, LayoutDashboard } from 'lucide-vue-next';
import { RouterLink, useRoute } from 'vue-router';

const route = useRoute();
</script>

<template>
    <div class="sidebar">
        <div class="sidebar-header">
            <div class="logoicon">
                <PanelsLeftBottom />
            </div>
            <div class="text">
                <h4>Keyhan</h4>
                <span>Management System</span>
            </div>
        </div>

        <nav class="sidebar-nav">
            <div :class="['divNav', { active: route.path === '/' }]">
                <LayoutDashboard />
                <RouterLink to="/" class="navLink">Gateway</RouterLink>
            </div>
        </nav>
    </div>
</template>

<style scoped>
.sidebar {
    width: 200px;       
    height: 100vh;
    background-color:#FAFAFA;
    padding: 20px;
    display: flex;
    flex-direction: column;
    border-right: 1px solid #ddd;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    position: fixed;
}
.sidebar-header {
    display: flex;
    align-items: center;
    padding-bottom: 40px;
    border-bottom: 1px solid #F5F5F7;
}
.divNav{
    display: flex;
    padding: 7px;
    margin-top: 15px;
    border-radius: 10px;
    gap: 10px;
    align-items: center;
    transition: all 0.2s;
    cursor: pointer;
}
.divNav:hover{
    background-color: #F1F5FE;
    color: #3F5BBD;
}
.divNav.active{
    background-color: #F1F5FE;
    color: #3F5BBD;
    border: 2px solid #E2E7FB;
}
.navLink{
    text-decoration: none;
    color: inherit;
}
.navLink:hover,
.navLink:visited:hover {
    text-decoration: none;
}
.navLink:visited{
    color: inherit;
}
.text h4{
    margin-bottom: 3px;
}
.text span{
    color: #747D87;
    font-size: small;
}
.sidebar-nav h5{
    margin-bottom: 5px;
    color: #747D87;
}
.sidebar-nav{
    display: flex;
    flex-direction: column;
}
.logoicon{
  background-color: #4E73E8; 
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
  margin-top: 20px;
}
@media (max-width: 768px) {
    .sidebar{
        display: none;
    }
}
</style>
