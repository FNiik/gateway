<!-- ping response component -->
<script setup>
import { ref,watch, onMounted, defineProps } from 'vue';
const pingResponse=ref('')
const wait=ref(false)
const props=defineProps({
    executeCounter: Number,
    targetIp:String

})  
const emit=defineEmits(['updateWait'])
function callPing(){
    wait.value=true
    let query=`
    mutation{
  Ping(ip:"${props.targetIp}")
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
    pingResponse.value=data.error
    wait.value=false
  }
    else if(data.data.Ping.response){
        pingResponse.value=data.data.Ping.response
        wait.value=false
        
    }
    else if(data.data.Ping.message){
        pingResponse.value=data.data.Ping.message
        wait.value=false
        
    }
    else{
        wait.value=false
        pingResponse.value='failed'
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
    callPing()
  }, 2000)
  
})
</script>
<template>
    <div class="grpcResponse">
        
        <span v-if="wait"> Executing gRPC command...</span>
        
        <pre v-if="!wait">{{ JSON.stringify(pingResponse, null, 2) }}</pre>
        

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
