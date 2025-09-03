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
// for(let i in newparameters){
//     if(newparameters[i]!==''){
//         changedParameters.value.push(i)
//     }
// }
watch(newparameters, (val) => {
  changedParameters.value = Object.entries(val)
    .filter(([_, v]) => v !== '')
    .map(([k, v]) => ({ field: k, value: v }))
}, { deep: true })

// function updateData(){
//     if(changedParameters.value.length===0){
//         console.log('error. no data to fetch')
//     }
//     else{
//         let fields = changedParameters.value.map(item => {
//             const isNumber = typeof item.value === 'number';
//             return isNumber 
//                 ? `${item.field}: ${item.value}` 
//                 : `${item.field}: "${item.value}"`;
//         })
//   .join(' ');
//         let query=
//         `mutation{
//             updateGateway(
//                 id:${gatewayinformation.gatewayinfo.id}
//                 ${fields}
//             )  {
//                 gateway{
//                     name
//                     ipAddress
//                     portNumber
//                     id
//                     status
//                     location
//                     description
//                     }
//                 ok
//                 message
//                 }
//         }`
//         fetch('http://127.0.0.1:8000/gateway/graphql/',{
//             method: 'post',
//             headers: 
//             {'content-type': 'application/json'},
//             body: JSON.stringify({query: query})

//         })
//        .then(function(response){
//             return response.json();
//         })
//         .then(function(data){
//             if (!data.data.gateway) {
//                 throw new Error("Gateway not found");
//             }
//             else{

//             }
//         })
//         newparameters={
//             name:'',
//             ipAddress:'',
//             portNumber:'',
//             status:'',
//             location:'',
//             description:'',

//         }      
            


            
    

//     }
// }    
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
    if(changedParameters.value.length===0){
        return true
    }
    else{
        return false
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
            <input v-model="newparameters.ipAddress" :placeholder="gatewayinfo.ipAddress" ></input>


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
  margin-bottom: 5px;
}
</style>