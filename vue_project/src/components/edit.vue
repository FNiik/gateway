<script setup>
import { computed, reactive, ref } from 'vue';
import { watch } from 'vue';

let gatewayinformation= defineProps({
    gatewayinfo:Object
})

let changedParameters=ref([])
let newparameters=reactive({
   name:'',
   ipAddress:'',
   portNumber:'',
   status:'',
   location:'',
   description:'',

})

watch(newparameters, (val) => {
  changedParameters.value = Object.entries(val)
    .filter(([_, v]) => v !== '' )
    .map(([k, v]) => ({ field: k, value: v }))
}, { deep: true })


function updateData() {
  if (!changedParameters.value || changedParameters.value.length === 0) {
    console.log('Error: no data to update');
    return;
  }

  
  let fields = changedParameters.value
  .map(item => {
    if (item.field === 'portNumber') {
      return `${item.field}: ${item.value}`; 
    }
    return `${item.field}: "${item.value}"`;
  })
  .join(' ');


  let query = `
    mutation {
      updateGateway(
        id: ${gatewayinformation.gatewayinfo.id}
        ${fields}
      ) {
        gateway {
          name
          ipAddress
          portNumber
          status
          location
          description
        }
        ok
        message
      }
    }
  `;

  fetch('http://127.0.0.1:8000/gateway/graphql/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query }),
  })
    .then(res => res.json())
    .then(data => {
      if (data.errors) {
        console.error('GraphQL errors:', data.errors);
      } else if (data.data.updateGateway.ok) {
        console.log('Update successful:', data.data.updateGateway.gateway);

        
        for (let key in newparameters) {
          newparameters[key] = '';
        }
        
        changedParameters.value = [];
      } else {
        console.warn('Update failed:', data.data.updateGateway.message);
      }
    })
    .catch(err => console.error('Fetch error:', err));
}

const disable= computed(()=>{
    if(changedParameters.value.length!==0 && (isValidIP(newparameters.ipAddress)|| newparameters.ipAddress==='')){
        return false
    }
    else{
        return true
    }
})
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
function isValidIP(ip) {
  
  const regex = /^(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)){3}$/;
  return regex.test(ip.trim());
}

</script>

<template>
<div class="editcontainer">
    <h2>Edit Gateway Configuration</h2>
    <div class="twocard">
        <div class="inputEdit">
            <h4>Gateway Name </h4>
            <input v-model="newparameters.name" :placeholder="gatewayinfo.name" ></input>

        </div>
        <div class="inputEdit">
            <h4>IP Address </h4>
            <!-- <input v-if="isValidIP(newparameters.ipAddress)||newparameters.ipAddress===''" v-model="newparameters.ipAddress" :placeholder="gatewayinfo.ipAddress" ></input>
            <input v-else v-model="newparameters.ipAddress" :placeholder="gatewayinfo.ipAddress" style="border-color: red;"></input> -->
            <input 
              v-model="newparameters.ipAddress" 
              :placeholder="gatewayinfo.ipAddress"
              :style="{ borderColor: newparameters.ipAddress && !isValidIP(newparameters.ipAddress) ? 'red' : '#E3E3E3' }"
            />


        </div>
    </div>
    <div class="twocard">
        <div class="inputEdit">
            <h4>Port</h4>
            <input v-model="newparameters.portNumber" :placeholder="gatewayinfo.portNumber"   ></input>

        </div>
        <div class="inputEdit">
            <h4>Status</h4>
            <el-select v-model="newparameters.status" :placeholder="gatewayinfo.status"     >
                    <el-option 
                        v-for="item in options"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value"
                    />
                
                </el-select> 
    
                


        </div>
       

        
    </div>
    <div class="twocard">
            <div class="inputEdit">
            <h4>Location</h4>
            <input v-model="newparameters.location" :placeholder="gatewayinfo.location"   ></input>

        </div>
    </div>    
    <div class="twocard">
            <div class="inputEdit">
            <h4>Description</h4>
            <textarea v-model="newparameters.description" :placeholder="gatewayinfo.description"   ></textarea>

        </div>
    </div>    
    <div class="buttoms">
        <button 
             
            :disabled="disable" 
            @click="updateData()"
        >
         Save Changes
        </button>

        

    </div>

</div>

</template>

<style scoped>

.twocard {
  display: flex;
  gap: 35px; 
  padding-left: 15px;
  padding-right: 15px;
}

.inputEdit {
  flex: 1; 
  
}

.inputEdit input {
  width: 100%; 
  height: 30px;
  border:1px solid #E3E3E3;
  border-radius: 5px;
  padding: 5px;
  
}
.inputEdit textarea {
  width: 100%; 
  height: 80px;
  border:1px solid #F2F3F7;
  border-radius: 5px;
  padding: 5px;
  
}
.buttoms{
    display: flex;
    flex-direction: row-reverse;
    padding: 20px;
}
button{
    background-color:#4567E3 ;
    height:40px ;
    width:100px ;
    color: white;
    border:none ;
    border-radius:5px ;
}
button:disabled{
    background-color:#A1B3F1 ;
    cursor: not-allowed;
}
h4{
  margin-bottom: 6px;
}
</style>