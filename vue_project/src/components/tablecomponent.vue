<!-- table component -->
<script setup>
import { computed, ref , defineEmits} from 'vue';
import { More } from '@element-plus/icons-vue';
import deleteGt from './deleteGt.vue';
import { StretchHorizontal } from 'lucide-vue-next';
import { Trash2 } from 'lucide-vue-next';
import { Eye } from 'lucide-vue-next';
const { gateways, value } = defineProps({
  gateways: Array,
  value: String
})
const deleteRefs={}
const tableRef = ref()
const toUpdateList=ref(0)

const formatter = (row, column) => {
  return row.location
}

const filteredgateways = computed(() => {
  if (!value) return gateways
  return gateways.filter(gt => gt.status && gt.status.toLowerCase() === value.toLowerCase())
})
const emit = defineEmits(['updatelistDelete'])
function handleUpdateList() {
  emit('updatelistDelete') 
}
</script>

<template>
  <el-table ref="tableRef" row-key="name" :data="filteredgateways" style="width: 100%" :header-cell-style="{ fontSize: '18px', fontWeight: 'bold', padding: '20px 10px'}" class="rounded-table">
    <el-table-column prop="name" label="Gateway Name" align="center" header-align="center" >
      
        <template #default="scope">
          <div class="iconName">
            <!-- <span class="iconWrapper">
              <StretchHorizontal />

            </span> -->
            
            <router-link
              
                class="namelink"
                :to="{ name: 'gatewaydetail', params: { id: scope.row.id } }"
            >
            <!-- <div class="iconWrapper">
              <StretchHorizontal />

            </div> -->
              
                {{ scope.row.name }}
            </router-link>

          </div>
            
            
      
        
          
       
      
       
     
        </template>
        
    </el-table-column>    


    <el-table-column align="center" header-align="center" prop="ipAddress" label="IP Address"  />
    <el-table-column align="center" header-align="center" prop="status" label="Status" >
      <template #default="scope">
        <el-tag
          :type="scope.row.status && scope.row.status.trim().toLowerCase() === 'active' ? 'success' : 'danger'"
          disable-transitions
        >
          {{ scope.row.status }}
        </el-tag>
      </template>
    </el-table-column>
    <el-table-column align="center" header-align="center" prop="location" label="Location" :formatter="formatter"  />
    <el-table-column align="center" header-align="center" label="Actions">
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
              <Eye />View Details
            </router-link>
            </template>
          </el-dropdown-item>
          <el-dropdown-item @click="()=>deleteRefs[scope.row.id].open()"> 
            <!-- <template #default={row}> -->
              <delete-gt   @updatelist="handleUpdateList" :id="Number(scope.row.id)" :ref="el => deleteRefs[scope.row.id]=el"  />
                
                
              
              
            <!-- call delete component -->
             <span class="dropdownItems2"><Trash2 />Delete</span>
            <!-- </template> -->
          
          </el-dropdown-item>
        </el-dropdown-menu>
      </template>
    </el-dropdown>
      </template>

    </el-table-column>
  </el-table>
  
</template>
<style scoped>
.rounded-table {
  border: 1px solid #E4E7EC; 
  border-radius: 8px;    
  overflow: hidden;       
}

.iconWrapper {
  
 display: flex; 
}
.iconName{
  display: flex;
  justify-content: center; 
  gap: 8px;
 
  align-items: center; 
}
.iconName:hover,
.iconName:visited:hover
{
  color:#5065C0;
  text-decoration: none;

}
.namelink{
    font-size: large;
    color: black;
    text-decoration: none;
    text-align: center;
    display: flex;
    align-items: center;
    
    
}
.namelink:hover,
.namelink:visited:hover 
{
    text-decoration: none;
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
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 5px;
  
}
.dropdownItems2{
  color:red;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  text-decoration: none;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 5px;
  
}

</style>