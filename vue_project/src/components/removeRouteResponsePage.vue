<!-- add route response component-->
<script setup>
import { ref,watch, onMounted ,defineProps} from 'vue';
import { stringifyQuery } from 'vue-router';
const removeRouteResponse=ref('')
const wait=ref(false)
const props=defineProps({
    executeCounter: Number,
    newDestIp:String,
    newDestMask:String,
    newDestGateway:String,
    newGatewayIp:String,
    newMetric:Number,
    newInterfaceName:String,
    newInterfaceIndex:Number,
    newDestIndex:Number



})  
const emit=defineEmits(['updateWait'])
function callRemoveRoute(){
    wait.value=true
    let query=`
    mutation{
  RemoveRoute(destinationIndex: ${props.newDestIndex},
    destinationIp:"${props.newDestIp}" ,
    destinationMask: "${props.newDestMask}",
    destinationGateway: "${props.newDestGateway}",
    gatewayIp: "${props.newGatewayIp}",
    metric: ${props.newMetric},
    interfaceName: "${props.newInterfaceName}",
    interfaceIndex: ${props.newInterfaceIndex}
  )
  {
    ok
    message
  }
}
    `
   
console.log("Query sent:", query)
   

fetch('http://127.0.0.1:8000/gateway/graphql/',{
    method: 'post',
    headers: 
        {'content-type': 'application/json'},
    body: JSON.stringify({query: query})

})

.then(function(response) {
    return response.json();
})
.then(function(data){
    if (data.errors) {
    removeRouteResponse.value=data.error
    wait.value=false
  }
    else if(data.data.RemoveRoute.message){
        removeRouteResponse.value=data.data.RemoveRoute.message
        wait.value=false
        
    }
    else{
        wait.value=false
    }
    

   
})    
.catch(err => console.error("Error:", err))
    
}
watch(wait, (newVal) => {
  emit('updateWait', newVal)
})
watch(() => props.executeCounter, () => {
    wait.value=true
    setTimeout(() => {
    callRemoveRoute()
  }, 2000)
  
})
</script>
<template>
    <div class="grpcResponse">
        
        <span v-if="wait"> Executing gRPC command...</span>
        
        <pre v-if="!wait">{{ JSON.stringify(removeRouteResponse, null, 2) }}</pre>
        

    </div>

</template>
<style scoped>
.grpcResponse{
    background-color: black;
    color: #81CA8D;
    padding: 20px;
}
pre {
white-space: pre-wrap;    
  word-break: break-word;     
  max-width: 600px;           
  overflow-x: auto;          
}
</style>
