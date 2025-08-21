<script setup>
import { useRoute } from 'vue-router';
import { ref, watch , reactive } from 'vue';
import { onMounted } from 'vue';
import { Switch } from '@element-plus/icons-vue'
import { Edit } from '@element-plus/icons-vue'
import overview from '@/components/overview.vue';
import Overview from '@/components/overview.vue';
import edit from '@/components/edit.vue';
import commandPage from '@/components/commandPage.vue';
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
    status
    location
    
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
    <div class="page">
        <div class="headerpage">
            <h2 >Gateways</h2>
            <span> Gateway Management Console</span> 
           
        </div>
        <div class="tablesearch">
            <h1>{{ gatewayinformation.name }}</h1>
            <span>{{ gatewayinformation.description }}</span>
            <br></br>
            <div class="scrollbarAndComponent">
                <div class="scrollbar">
                    <el-tabs type="border-card" class="demo-tabs">
                        <!-- overview tab -->
                        <el-tab-pane>
                            <template #label>
                                <span class="custom-tabs-label">
                                <el-icon><Switch /></el-icon>
                                <span>Overview</span>
                                </span>
                            </template>
                            <Overview :gatewayinfo="gatewayinformation" />
                            <!-- component call -->
      
                        </el-tab-pane>
                        <!-- edit tab -->
                        <el-tab-pane>
                            <template #label>
                                <span class="custom-tabs-label">
                                <el-icon><Edit /></el-icon>
                                <span>Edit</span>
                                </span>
                            </template>
                            <edit :gatewayinfo="gatewayinformation" />
                            <!-- component call -->
      
                        </el-tab-pane>
                        <!-- Network tab -->
                        <el-tab-pane>
                            <template #label>
                                <span class="custom-tabs-label">
                                <el-icon><Edit /></el-icon>
                                <span>Network</span>
                                </span>
                            </template>
                            <!-- component call -->
      
                        </el-tab-pane>
                        <!-- time tab -->
                        <el-tab-pane>
                            <template #label>
                                <span class="custom-tabs-label">
                                <el-icon><Edit /></el-icon>
                                <span>Time</span>
                                </span>
                            </template>
                            <!-- component call -->
      
                        </el-tab-pane>
                        <!-- commands tab -->
                        <el-tab-pane>
                            <template #label>
                                <span class="custom-tabs-label">
                                <el-icon><Edit /></el-icon>
                                <span>commands</span>
                                </span>
                            </template>
                            <!-- component call -->
                             <commandPage/>
      
                        </el-tab-pane>



                        
                        
                    </el-tabs>
                   

                </div>

            </div>

        </div>

    </div>

</template>

<style scoped>

.demo-tabs > .el-tabs__content {
  padding: 32px;
  color: #6B7484;
  font-size: 32px;
  font-weight: 600;
  
 
}
.demo-tabs > .el-tabs__content :active {
  padding: 32px;
  color: black;
  font-size: 32px;
  font-weight: 600;
 
}
.demo-tabs .custom-tabs-label .el-icon {
  vertical-align: middle;
}
.demo-tabs .custom-tabs-label span {
  vertical-align: middle;
  margin-left: 4px;
}

.page {
    display: flex;
    flex-direction: column;
    flex-grow: 1;
    /* padding: 20px; */
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
/* .searchfilter{
    display: flex;
    background-color:#FFFFFF;
    padding: 20px;
    border:1px solid #F2F3F7;
    border-radius: 8px;
    justify-content: space-evenly;
    margin: 15px;
} */
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
/* .headerbody{
    border: 1px solid #F2F3F7;
    border-radius: 8px;
} */
::v-deep(.el-tabs__nav) {
  display: flex !important;
  justify-content: space-between;
  width: 100%;
}

::v-deep(.el-tabs__item) {
  flex: 1 1 0;
  text-align: center;
}
/* .scrollbar{
    background-color: #FFFFFF;
    margin-bottom: 0px;
    border-bottom:1px solid #F2F3F7 ;
    padding: 15px;
    
    border-radius: 8px;
} */
/* رنگ تب فعال */
::v-deep(.el-tabs__item.is-active) {
  color: #333;
  background: #f1f1f1;
  border-radius: 6px;
}

/* تب‌ها */
::v-deep(.el-tabs__header) {
  background-color: #fff;
  border-radius: 8px;
  padding: 10px;
  margin-bottom: 15px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.05);
}

/* محتوای تب‌ها */
::v-deep(.el-tabs__content) {
  background-color: #fff;
  border-radius: 8px;
  padding: 20px;
}

</style>