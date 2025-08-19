<script setup>
import { ref, computed, watch } from 'vue';
const gateway_name=ref('')
const gateway_ip=ref('')
const gateway_status=ref('')
const gateway_port=ref('')
const gateway_location=ref('')
const gateway_description=ref('')
// const dialogFormVisible=ref(true)
// 
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
    if(gateway_name.value!==''&& gateway_ip.value!==''&& gateway_port.value!==''){
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
        gateway_port.value=''
        gateway_status.value=''

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
    if (data.errors) {
    alert("GraphQL Error:", data.errors)
    return
  }
    if(data.data.createGateway.ok){
        alert("Gateway created successfully")
        dialogFormVisible.value=false
        gateway_name.value=''
        gateway_ip.value=''
        gateway_location.value=''
        gateway_description.value=''
        gateway_port.value=''
        gateway_status.value=''
    }
    else{
        alert("Create gateway failed")
    }

   
})    
.catch(err => console.error("Error:", err))
    
}


</script>
<template>
     <div class="forButtom">
              <button class="buttoms" @click="dialogFormVisible = true"> Add Gateway</button>
              
              <el-dialog v-model="dialogFormVisible" title="Add New Gateway" width="450">
                <div class="dialog">
                  <div class="inputEdit">
                    <h4>Gateway Name </h4>
                    <input v-model="gateway_name" :placeholder="'e.g.,'" ></input>
                  </div>  
            

                    
                  <div class="inputEdit">
                    <h4>IP Address </h4>
                    <input v-model="gateway_ip" :placeholder="'e.g.,'" ></input>
                  </div>
                  <div class="twocard">
                    <div class="inputEdit">
                        <h4>Port</h4>
                        <input v-model="gateway_port" :placeholder="'e.g.,'"   ></input>
                    </div>
                    <div class="inputEdit">
                        <h4>Status</h4>
                        <el-select v-model="gateway_status" :placeholder="'Active'"     >
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
                        <input v-model="gateway_location" :placeholder="''"   ></input>
                    
                    </div>
                    <div class="inputEdit">
                        <h4>Description</h4>
                        <textarea v-model="gateway_description" :placeholder="''"   ></textarea>
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
.buttoms{
    display: flex;
    flex-direction: row-reverse;
    padding: 20px;
    justify-content: center;
    align-items: center;


}
button{
    background-color:#4567E3 ;
    height:40px ;
    width:120px ;
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

</style>