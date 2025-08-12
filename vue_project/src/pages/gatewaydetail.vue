<script setup>
import { useRoute } from 'vue-router';
import { ref, watch , reactive } from 'vue';
import { onMounted } from 'vue';
const route=useRoute()
// let id=ref(route.params.id)
// fetch data
let gatewayinformation=reactive({})
function loadGatewayDetail(id){
    let query=`{
  gateway(id:${id}){
    id
    name
    ipAddress
    portNumber
    description
    
  }
}`
fetch('http://127.0.0.1:8000/gateway/graphql/',{
    method: 'post',
    headers: 
        {'content-type': 'application/json'},
    body: JSON.stringify({query: query})

})
.then(function(response){
    return response.json();
})
.then(function(data){
    if (!data.data.gateway) {
        throw new Error("Gateway not found");
    }
    // gatewayinformation=data.data.gateway
    Object.assign(gatewayinformation,data.data.gateway)
    })  
}
onMounted(()=>{
    loadGatewayDetail(route.params.id)
})
watch(()=>route.params.id,
    (newid)=>{
    loadGatewayDetail(newid)
})
</script>

<template>
    <div>
        
    </div>

</template>

<style scoped>
</style>