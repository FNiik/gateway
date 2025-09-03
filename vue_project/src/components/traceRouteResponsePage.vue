<!-- ping response component -->
<script setup>
import { ref,watch, onMounted, defineProps } from 'vue';
const traceRouteResponse=ref('')
const wait=ref(false)
const props=defineProps({
    executeCounter: Number,
    targetIp:String

})  
const emit=defineEmits(['updateWait'])
function callTraceRoute(){
    wait.value=true
    let query=`
    mutation{
  TraceRoute(ip:"${props.targetIp}")
  {
    response{
      response
    }
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
    traceRouteResponse.value=data.error
    wait.value=false
  }
    else if(data.data.TraceRoute.response){
        traceRouteResponse.value=data.data.TraceRoute.response
        wait.value=false
        
    }
    else if(data.data.TraceRoute.message){
        traceRouteResponse.value=data.data.TraceRoute.message
        wait.value=false
        
    }
    else{
        wait.value=false
        traceRouteResponse.value='failed'
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
    callTraceRoute()
  }, 2000)
  
})
</script>
<template>
    <div class="grpcResponse">
        
        <span v-if="wait"> Executing gRPC command...</span>
        
        <pre v-if="!wait">{{ JSON.stringify(traceRouteResponse, null, 2) }}</pre>
        

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
