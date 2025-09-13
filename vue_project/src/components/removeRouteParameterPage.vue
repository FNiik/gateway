<!-- removeroute parameter component -->
<script setup>
import { ref, defineEmits, watch } from 'vue';
const destIndex=ref(1)
const destIp=ref('')
const destMask=ref('')
const destGateway=ref('')
const gatewayIp=ref('')
const metric=ref(10)
const interfaceName=ref('')
const interfaceIndex=ref(1)
const emit=defineEmits(['removeRouteParameters'])

watch([destIndex,destIp, destMask, destGateway, gatewayIp, metric, interfaceName, interfaceIndex],([newdestIndex,newdestIp, newdestMask, newdestGateway, newgatewayIp, newmetric, newinterfaceName, newinterfaceIndex])=>{
  if (
    newdestIndex?.trim() &&
    newdestIp?.trim() &&
    newdestMask?.trim() &&
    newdestGateway?.trim() &&
    newgatewayIp?.trim() &&
    newmetric?.trim() &&
    newinterfaceName?.trim() &&
    newinterfaceIndex?.trim()
  ) {
    emit('removeRouteParameters', {
      destIndex: Number(newdestIndex),
      destIp: newdestIp,
      destMask: newdestMask,
      destGateway: newdestGateway,
      gatewayIp: newgatewayIp,
      metric: Number(newmetric),
      interfaceName: newinterfaceName,
      interfaceIndex: Number(newinterfaceIndex)
    })
  }
})




</script>
<template>
    <div class="commandRequirment">
        <div class="twocard">
            <div class="inputEdit">
                <h4>Destination IP</h4>
                <input v-model="destIp" placeholder="192.168.1.0"></input>
            </div>
            <div class="inputEdit">
                <h4>Destination Subnet Mask</h4>
                <input v-model="destMask" placeholder="255.255.255.0"></input>
            </div>
        </div>
        <div class="twocard">
            <div class="inputEdit">
                <h4>Gateway IP</h4>
                <input v-model="gatewayIp" placeholder="192.168.1.1" ></input>
            </div>
            
            <div class="inputEdit">
                <h4>Destination Gateway</h4>
                <input v-model="destGateway" placeholder="192.168.1.10"></input>
            </div>

            
        </div>
        <div class="twocard">
            <div class="inputEdit">
                <h4>Interface Index</h4>
                <input v-model="interfaceIndex" placeholder="1"></input>
            </div>
            <div class="inputEdit">
                <h4>Interface Name</h4>
                <input v-model="interfaceName" placeholder="Ethernet0"></input>

            </div>
            
        </div>
        <div class="twocard">
            <div class="inputEdit">
                <h4>Destination Index</h4>
                <input v-model="destIndex" placeholder="1"></input>
            </div>
            <div class="inputEdit">
                <h4>Metric</h4>
                <input v-model="metric" placeholder="10"></input>
            </div>

        </div>


    </div>

</template>
<style scoped>
.commandRequirment{
    display: flex;
    flex-direction: column;
    /* border-top: 1px solid #F3F4F7; */
    border-bottom:1px solid #F3F4F7 ;
    /* padding: 20px; */

    
}
.twocard {
  display: flex;
  gap: 35px; 
  
}

.inputEdit {
  flex: 1; 
  padding: 15px;
}

.inputEdit input {
  width: 100%; 
  height: 20px;
  border:1px solid #E3E3E3;
  border-radius: 5px;
  padding: 10px;
  margin-top: 5px;
  
}
h4{
    margin-bottom: 5px;
    margin-top: 0px;
}
</style>