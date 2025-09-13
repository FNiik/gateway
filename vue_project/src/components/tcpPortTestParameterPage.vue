<!-- tcpPortTest parameter component -->
<script setup>
import { ref, watch,defineEmits } from 'vue';
const targetIp=ref('')
const port=ref('')
const emit=defineEmits(['tcpPortTestParameter'])
function isValidIP(ip) {
  const regex = /^(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}$/;
  return regex.test(ip);
}
// pass parameters to parent
watch([targetIp, port],([newIp,newPort])=>{
  if(newIp?.trim() && isValidIP(newIp)&&newPort?.trim()){
    emit('tcpPortTestParameter',{ip:(newIp), port:Number(newPort)})
  }
})
</script>
<template>
    <div class="twocard">
        <div class="inputEdit">
            <h4>Target IP Address</h4>
            <input v-model="targetIp" placeholder="8.8.8.8"></input>
        </div>
        <div class="inputEdit">
            <h4>Port Number</h4>
            <input v-model="port" placeholder="80"></input>
        </div>

    </div>

</template>
<style scoped>
.twocard {
  display: flex;
  gap: 35px; 
  padding: 20px;
  padding-top: 0px;
}

.inputEdit {
  flex: 1; 
  padding:15px ;
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