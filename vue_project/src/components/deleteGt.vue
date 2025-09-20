<!-- delete component -->
<script setup>
import { ElMessage, ElMessageBox } from 'element-plus'
import { onMounted ,defineEmits, ref, watch} from 'vue';
const { id } = defineProps({ id: Number })

// const counter=ref(0)
// watch(counter, (newVal) => {
//   emit('updatelist', newVal)
// })
const emit = defineEmits(['updatelist'])
function deleteGateway(){
let query=`mutation{
  deleteGateway(id:${id}){
    ok
    message

  }
}`;
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
    alert("GraphQL Error:", data.errors)
    return
  }
    if(data.data.deleteGateway.ok){
        alert("Gateway deleted successfully")
        emit('updatelist')
        
    }
    else{
        alert("Delete gateway failed")
    }

   
})    
.catch(err => console.error("Error:", err))
    
}

const open = () => {
  ElMessageBox.confirm(
    'Are you sure you want to delete this gateway?',
    'Warning',
    {
      confirmButtonText: 'OK',
      cancelButtonText: 'Cancel',
      type: 'warning',
    }
  )
    .then(() => {
      deleteGateway()  
      ElMessage({
        type: 'success',
        message: 'Delete completed',
      })
    })
    .catch(() => {
      ElMessage({
        type: 'info',
        message: 'Delete canceled',
      })
    })
}
defineExpose({ open })
</script>
<template>
  <div style="display: none"></div>

</template>
<style scoped>
</style>
