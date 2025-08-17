<!-- gatewaylist.vue -->
<script setup>
import { onMounted } from 'vue';
import { ref } from 'vue';
// import table from '@/components/tablecomponent.vue';
// import Table from '@/components/tablecomponent.vue';
import tablecomponent from '@/components/tablecomponent.vue';
import { Search } from '@element-plus/icons-vue'
const input1=ref('')

const value = ref('')

const options = [
  {
    value: 'active',
    label: 'Active',
  },
  {
    value: 'inactive',
    label: 'Inactive',
  },
  {
    value:'',
    label:"All Status",

  },
]
let gateways=ref([])
function loadGateways(page, pagesize){
    let query=`{
  paginatedGateways(page:${page}, pageSize:${pagesize}){
    gateways {
      id
      name
      ipAddress
      portNumber
      description
      status
      location
    }
    totalCount
    page
    pageSize
    hasNext
    hasPrevious
  }
 }`
fetch('http://127.0.0.1:8000/gateway/graphql/',{
    method: 'post',
    headers: 
        {'content-type': 'application/json'},
    body: JSON.stringify({query: query})

})

.then(function(response) {
    return response.json();
})
.then(function(data) {
    if (!data.data.paginatedGateways) {
        throw new Error('no data returned');
    }
    else{

        gateways.value = data.data.paginatedGateways.gateways;
    }
})
.catch(function(error) {
    console.error("Error loading gateways:", error);
});
}
onMounted(() => {
  loadGateways(1, 20)
})
// let filteredgateways=ref([])


</script>

<template>
    <div class="page">
        <div class="headerpage">
            <h2 >Gateways</h2>
            <span> Gateway Management Console</span> 
           
        </div>
        <div class="tablesearch">
            <h1>Gateway Management</h1>
            <span>Configure and monitor your network gateways</span>
            <button class=""> Add Gateway</button>
            <div class="searchfilter">
                <el-input
                    v-model="input1"
                    style="width: 700px"
                    size="large"
                    placeholder="Please Input"
                    :suffix-icon="Search"
                 />    
                <el-select v-model="value" placeholder="All Status" style="width: 240px  "  >
                    <el-option 
                        v-for="item in options"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value"
                    />
                
                </el-select> 
    
                
    

            </div>
            <div class="headerbody">
                <div class="headertable">
                    <h1>Gateways</h1>
                  
                </div>
        
                <tablecomponent  :gateways="gateways" :value="value" />


            </div>
            

        </div>
        
        
    
    </div>

</template>

<style scoped>
.page {
    display: flex;
    flex-direction: column;
    flex-grow: 1;
    padding: 20px;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;

}
.headerpage {
    background-color: #FFFFFF;
    padding:20px;
    border-bottom:  1px solid #F2F3F7;
}
.tablesearch{
    background-color:#F9FAFC ;
    flex-grow: 1;
    padding: 20px;
    margin: 0px;


}
.searchfilter{
    display: flex;
    background-color:#FFFFFF;
    padding: 20px;
    border:1px solid #F2F3F7;
    border-radius: 8px;
    justify-content: space-evenly;
    margin: 15px;
}
.headerpage span {
  display: block;
}
.headerpage h1,
.headerpage h2 {
  margin: 0;
}
.tablesearch span {
  display: block;
}
.tablesearch h1,
.tablesearch h2 {
  margin: 1px;
}
.headertable {
    background-color: #FFFFFF;
    margin-bottom: 0px;
    border-bottom:1px solid #F2F3F7 ;
    padding: 15px;
    height: 30px;
    border-radius: 8px;
   

}
.headerbody{
    border: 1px solid #F2F3F7;
    border-radius: 8px;
}

</style>