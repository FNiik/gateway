<!-- create component -->
<script setup>
import { ref, computed, watch, defineEmits } from 'vue';
const gateway_name=ref('')
const gateway_ip=ref('')
const gateway_status=ref('active')
const gateway_port=ref(22)
const gateway_location=ref('')
const gateway_description=ref('')
import { Plus } from 'lucide-vue-next';
// const dialogFormVisible=ref(true)
// 
const emit=defineEmits(['updatelist'])
const counter=ref(0)
watch(counter, (newVal) => {
  emit('updatelist', newVal)
})
const dialogFormVisible = ref(false)
const formLabelWidth = '140px'
const options = [
  {
    value: 'active',
    label: 'Active',
  },
  {
    value: 'inactive',
    label: 'Inactive',
  },
]
const disable= computed(()=>{
    if(gateway_name.value!==''&& gateway_ip.value!==''&& isValidIP( gateway_ip.value) ){
        return false
    }
    else{
        return true
    }
})
watch (dialogFormVisible, (newval)=>{
    if(newval===false){
        dialogFormVisible.value=false
        gateway_name.value=''
        gateway_ip.value=''
        gateway_location.value=''
        gateway_description.value=''
        gateway_port.value=22
        gateway_status.value='active'

    }

});


function createGateway(){
    let query=`
    mutation {
  createGateway(
    name: "${gateway_name.value}"
    ipAddress: "${gateway_ip.value}"
    portNumber: ${parseInt(gateway_port.value)}
    description: "${gateway_description.value}"
    status:"${gateway_status.value}"
    location:"${gateway_location.value}"
    
  ) {
    gateway {
      id
      name
      ipAddress
      portNumber
      description
      status
      location
      
    }
    ok
  }
}

    `;
    fetch("http://127.0.0.1:8000/gateway/graphql/",{
    method: 'post',
    headers: 
        {'content-type': 'application/json'},
    body: JSON.stringify({query: query})

})
.then(function(response){
    return response.json();
})
.then(function(data){
    if (data.errors) {
    alert("GraphQL Error:", data.errors)
    return
  }
    if(data.data.createGateway.ok){
        alert("Gateway created successfully")
        counter.value++
        dialogFormVisible.value=false
        gateway_name.value=''
        gateway_ip.value=''
        gateway_location.value=''
        gateway_description.value=''
        gateway_port.value=2
        gateway_status.value='active'
    }
    else{
        alert("Create gateway failed")
    }

   
})    
.catch(err => console.error("Error:", err))
    
}
function isValidIP(ip) {
  
  const regex = /^(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)){3}$/;
  return regex.test(ip.trim());
}
const borderColor = computed(() => {
  if (!gateway_ip.value) return "#E3E3E3";
  return isValidIP(gateway_ip.value) ? "#E3E3E3" : "red";
});
</script>
<template>
     <div class="forButtom">
              <button class="buttons" @click="dialogFormVisible = true"> <Plus />Add Gateway</button>
              
              <el-dialog v-model="dialogFormVisible" title="Add New Gateway" width="450">
                <div class="dialog">
                  <div class="inputEdit">
                    <h4>Gateway Name * </h4>
                    <input v-model="gateway_name" :placeholder="'Main Office Gateway'" ></input>
                  </div>  
            

                    
                  <div class="inputEdit">
                    <h4>IP Address *</h4>
                    <!-- <input  v-if="isValidIP(gateway_ip) || gateway_ip===''" v-model="gateway_ip" :placeholder="'192.168.1.1'" ></input>
                    <input  v-else v-model="gateway_ip" :placeholder="'192.168.1.1'"  style="border-color: red;"></input> -->
                    <input 
                      v-model="gateway_ip" 
                      :placeholder="'192.168.1.1'"
                      :class="{ 'invalid-input': gateway_ip && !isValidIP(gateway_ip) }"
                    />
                  </div>
                  <div class="twocard">
                    <div class="inputEdit">
                        <h4>Port *</h4>
                        <input v-model="gateway_port" :placeholder="'22'"   ></input>
                    </div>
                    <div class="inputEdit">
                        <h4>Status</h4>
                        <el-select v-model="gateway_status" :placeholder="'Active'" size="large"    >
                            <el-option 
                        
                            v-for="item in options"
                        
                            :key="item.value"
                            :label="item.label"
                            :value="item.value"/>
                        </el-select>
                  </div>
                  

                  </div>  
                    <!--this is for two card  -->
                    
                    <div class="inputEdit">
                        <h4>Location</h4>
                        <input v-model="gateway_location" :placeholder="'Main Office Bilding A'"   ></input>
                    
                    </div>
                    <div class="inputEdit">
                        <h4>Description</h4>
                        <textarea v-model="gateway_description" :placeholder="'Optional description or notes '"   ></textarea>
                    </div>
                    <div class="forButtom">
                        <button class="buttoms" @click="createGateway" :disabled="disable">Create Gateway</button>

                    </div>
                    
                        

                    
                         



                </div>
                <!-- for dialog -->

                  

                 
               </el-dialog>
                


        </div>
        <!-- for for button -->
       

    

    
             
              
              


</template>
<style scoped>
:deep(.el-dialog__header .el-dialog__title) {
  font-size: 20px;   
  font-weight: 700;  
}
input {
  border: 1px solid #E3E3E3;
  padding: 5px;
  border-radius: 5px;
  outline: none;
}

input:focus {
  border-color: inherit;
  box-shadow: none;
}

.invalid-input {
  border-color: red !important;
}
.buttons{
    display: flex;
    /* flex-direction: row-reverse; */
    padding: 20px;
    justify-content: center;
    align-items: center;


}
button{
    background-color:#4567E3 ;
    height:32px ;
    width:130px ;
    color: white;
    border:none ;
    border-radius:5px ;
    
}
.forButtom{
  display: flex;
  flex-direction: row-reverse;
}
.dialog{
    display: flex;
    flex-direction: column;
}
.twocard {
  display: flex;
  gap: 35px; 
}

.inputEdit {
  flex: 1; 
  
}

.inputEdit input {
  width: 100%; 
  height: 40px;
  border:1px solid #E3E3E3;
  border-radius: 5px;
  padding-left: 5px;
  
  
  
}
.inputEdit textarea {
  width: 100%; 
  height: 60px;
  border:1px solid #F2F3F7;
  border-radius: 5px;
  
}
button:disabled{
    background-color:#A1B3F1 ;
    cursor: not-allowed;
}
@media (max-width: 768px) {
  .forButtom{
  display: flex;
  flex-direction: row;
}
}
</style>