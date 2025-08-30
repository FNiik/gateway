<script setup>
import { ref,watch, onMounted } from 'vue';
const showRouteresponse=ref('')
const wait=ref(false)
const props=defineProps({
    executeCounter: Number

})  
const emit=defineEmits(['updateWait'])
function callShowRoute(){
    wait.value=true
    let query=`
    {
  showRoute{
    allRouteInfo
    routeInfo{
      destinationInterface {
        index
        ip
        mask
        gateway
      }
      gatewayIp
      metric
      interfaceName
      interfaceIndex
    }
  }
}
    `
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
    showRouteresponse.value=data.error
  }
    if(data.data.showRoute){
        showRouteresponse.value=data.data.showRoute
        wait.value=false
        
    }
    

   
})    
.catch(err => console.error("Error:", err))
    
}
watch(wait, (newVal) => {
  emit('updateWait', newVal)
})
watch(() => props.executeCounter, () => {
    setTimeout(() => {
    callShowRoute()
  }, 2000)
  
})
</script>
<template>
    <div class="grpcResponse">
        
        <span v-if="wait"> Executing gRPC command...</span>
        
        <pre v-if="!wait">{{ JSON.stringify(showRouteresponse, null, 2) }}</pre>
        

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
