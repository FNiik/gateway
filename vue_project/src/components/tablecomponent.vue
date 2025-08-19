<script setup>
import { computed, ref } from 'vue';
import { More } from '@element-plus/icons-vue';
import deleteGt from './deleteGt.vue';
const { gateways, value } = defineProps({
  gateways: Array,
  value: String
})
const deleteRefs={}
const tableRef = ref()

const formatter = (row, column) => {
  return row.location
}

const filteredgateways = computed(() => {
  if (!value) return gateways
  return gateways.filter(gt => gt.status && gt.status.toLowerCase() === value.toLowerCase())
})
</script>

<template>
  <el-table ref="tableRef" row-key="name" :data="filteredgateways" style="width: 100%">
    <el-table-column prop="name" label="Gateway Name" width="180" >
        <template #default="scope">
            <router-link
                class="namelink"
                :to="{ name: 'gatewaydetail', params: { id: scope.row.id } }"
            >
                {{ scope.row.name }}
            </router-link>
            
      
        
          
       
      
       
     
        </template>
        
    </el-table-column>    


    <el-table-column prop="ipAddress" label="IP Address" width="180" />
    <el-table-column prop="status" label="Status" width="100">
      <template #default="scope">
        <el-tag
          :type="scope.row.status && scope.row.status.trim().toLowerCase() === 'active' ? 'success' : 'danger'"
          disable-transitions
        >
          {{ scope.row.status }}
        </el-tag>
      </template>
    </el-table-column>
    <el-table-column prop="location" label="Location" :formatter="formatter" />
    <el-table-column label="Actions">
      <template #default="scope">
        <el-dropdown>
      <el-button >
        <el-icon><More /></el-icon>
      </el-button>
      
      <template #dropdown>
        <el-dropdown-menu>
          <el-dropdown-item  > 
            <template #default={row}>
            <router-link class="dropdownItems" :to="{ name: 'gatewaydetail', params: { id: scope.row.id } }" >
              View Details
            </router-link>
            </template>
          </el-dropdown-item>
          <el-dropdown-item @click="()=>deleteRefs[scope.row.id].open()"> 
            <template #default={row}>
              <delete-gt :id="Number(scope.row.id)" :ref="el => deleteRefs[scope.row.id]=el"/>
              
            <!-- call delete component -->
             <span class="dropdownItems">Delete</span>
            </template>
          
          </el-dropdown-item>
        </el-dropdown-menu>
      </template>
    </el-dropdown>
      </template>

    </el-table-column>
  </el-table>
</template>
<style scoped>
.namelink{
    font-size: large;
    color: black;
    text-decoration: none;
    text-align: center;
    
}
.namelink:hover,
.namelink:visited:hover 
{
    text-decoration: underline;
    color:#5065C0;
}
.namelink:visited{
    color: black;
    text-decoration: none;
}
    
.dropdownItems{
  color: black;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  text-decoration: none;
  
}
.dropdownItems span{
  color: red;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  text-decoration: none;
}
</style>