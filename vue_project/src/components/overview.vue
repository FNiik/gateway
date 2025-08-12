<script setup>
import { ref } from 'vue';
let gatewayinformation= defineProps({
    gatewayinfo:Object
})

</script>
<template>
<div class="headerAndContainer">
    <div class="header">
        <h1>
            Gateway Information
        </h1>

    </div>
    <div class="container">
        <div class="twocard">
            <div class="card">
            <h3>Gateway ID</h3>
            {{ gatewayinfo.id }}

        </div>
        <div class="card">
            <h3>IP Address</h3>
            {{ gatewayinfo.ipAddress }}
        </div>

        </div>
        <div class="twocard">
            <div class="card">
            <h3>Gateway Name</h3>
            {{ gatewayinfo.name }}
        </div>
        <div class="card">
            <h3>Port Number</h3>
            {{ gatewayinfo.portNumber }}
        </div>

        </div>
        <div class="twocard">
            <div class="card">
            <h3>Status</h3>
            {{ gatewayinfo.status }}
        </div>

        </div>
        

        

    </div>
</div>    

</template>
<style scoped>
.container{
    display: flex;
    flex-direction: column;
    background-color: #FDFEFE;

}
.twocard{
    display: flex;
    

}
.card{
    flex-basis: 50%;
    border:1px solid #F2F3F7;
    border-radius: 8px;
    padding: 20px;
    margin: 15px;
    background-color: #FFFFFF;


}
.header{
    border:1px solid #F2F3F7;
    padding: 10px;
    margin: 10px; 
    border-radius: 8px;
    margin-bottom: 0px;
    margin-top: 20px;
}
.headerAndContainer{
    display: flex;
    flex-direction: column;
}
</style>