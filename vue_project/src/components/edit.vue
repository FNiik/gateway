<script setup>
import { ref } from 'vue';
let gatewayinformation= defineProps({
    gatewayinfo:Object
})
let newName=ref('')
let newIp=ref('')
let newport=ref()
let newdescription=ref('')
let newlocation=ref('')


</script>

<template>
<div class="editcontainer">
    <h2>Edit Gateway Configuration</h2>
    <div class="twocard">
        <div class="inputEdit">

        </div>
        <div class="inputEdit">

        </div>
    </div>

</div>

</template>

<style scoped>
</style>