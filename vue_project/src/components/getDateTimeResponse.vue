<script setup>
import { ref,watch, onMounted } from 'vue';
const gateDateTimeResponse=ref('')
const wait=ref(false)
const props=defineProps({
    executeCounter: Number

})  
const emit=defineEmits(['updateWait'])
function callGetDateTime(){
    wait.value=true
    let query=`
    {
  getDateTime{
    currentDate
    currentTime
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
    gateDateTimeResponse.value=data.error
    wait.value=false
  }
    else if(data.data.getDateTime){
        gateDateTimeResponse.value=data.data.getDateTime
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
    callGetDateTime()
  }, 2000)
  
})
</script>
<template>
    <div class="grpcResponse">
        
        <span v-if="wait"> Executing gRPC command...</span>
        
        <pre v-if="!wait">{{ JSON.stringify(gateDateTimeResponse, null, 2) }}</pre>
        

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
