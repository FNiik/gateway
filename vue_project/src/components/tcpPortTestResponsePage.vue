<!-- ping response component -->
<script setup>
import { ref,watch, onMounted, defineProps } from 'vue';
const tcpPortTestResponse=ref('')
const wait=ref(false)
const props=defineProps({
    executeCounter: Number,
    targetIp:String,
    port:String

})  
const emit=defineEmits(['updateWait'])
function callTcpPortTest(){
    wait.value=true
   let query=`
   mutation{
  TcpPortTest(ip:"${props.targetIp}", port:${props.port})
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
    tcpPortTestResponse.value=data.error
    wait.value=false
  }
    else if(data.data.TcpPortTest.response){
        tcpPortTestResponse.value=data.data.TcpPortTest.response
        wait.value=false
        
    }
    else if(data.data.TcpPortTest.message){
        tcpPortTestResponse.value=data.data.TcpPortTest.message
        wait.value=false
        
    }
    else{
        wait.value=false
        tcpPortTestResponse.value='failed'
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
    callTcpPortTest()
  }, 2000)
  
})
</script>
<template>
    <div class="grpcResponse">
        
        <span v-if="wait"> Executing gRPC command...</span>
        
        <pre v-if="!wait">{{ JSON.stringify(tcpPortTestResponse, null, 2) }}</pre>
        

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
