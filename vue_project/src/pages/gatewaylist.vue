<!-- gatewaylist.vue -->
<script setup>
import { onMounted, watch } from 'vue';
import { ref } from 'vue';
import tablecomponent from '@/components/tablecomponent.vue';
import { Search } from '@element-plus/icons-vue'
import { useSidebarStore } from '@/stores/sidebar';
import Create from '@/components/create.vue';
import { Rows2 } from 'lucide-vue-next';

const sidebar = useSidebarStore()
const input1 = ref('')
const value = ref('')
const page1 = ref(1)
const totalCount1 = ref(0)
const pageSize1 = ref(20)
const hasNext1 = ref(false)
const hasPrevious1 = ref(false)
const loadPerPage=ref(10)
const num=ref(5)
const options = [
  { value: 'active', label: 'Active' },
  { value: 'inactive', label: 'Inactive' },
  { value:'', label:"All Status" }
]
const toUpdateList=ref(0)
let gateways = ref([])

function loadGateways(page = page1.value, pagesize = pageSize1.value){
    page = Number(page) || 1
    pagesize = Number(pagesize) || 10
    let query = `{
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
        headers: {'content-type': 'application/json'},
        body: JSON.stringify({query: query})
    })
    .then(res => res.json())
    .then(data => {
        const pg = data?.data?.paginatedGateways
        if(pg){
          gateways.value = pg.gateways || []
          page1.value = Number(pg.page) || page
          pageSize1.value = Number(pg.pageSize) || pagesize
          hasNext1.value = !!pg.hasNext
          hasPrevious1.value = !!pg.hasPrevious
          totalCount1.value = Number(pg.totalCount) || 0
        }
    })
    .catch(err => console.error("Error loading gateways:", err))
}

onMounted(() => {
  loadGateways(1, loadPerPage)
})
watch(loadPerPage, (newval)=>{
  loadGateways(page1,newval)
})
watch(toUpdateList, (newval)=>{
  loadGateways(page1,loadPerPage)
})
</script>

<template>
  <div class="page">
    <!-- <div class="headerpageSidebarIcon">
      <div class="sidebarIcon">
        <button class="sidebarIconButton" @click="sidebar.toggle">
          <Rows2 />
        </button>
      </div>
      <div class="headerpage">
        <h2>Gateways</h2>
        <span> Gateway Management Console</span>
      </div>
    </div> -->

    <div class="tablesearch">
      <h1>Gateways</h1>
      <div class="searchfilter">
        <el-input
          v-model="input1"
          style="width: 700px;"
          size="large"
          placeholder="Search gateways by name, IP, or location"
          :suffix-icon="Search"
        />    
        <el-select v-model="value" placeholder="All Status" size="large" style="width: 240px;">
          <el-option 
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          />
        </el-select> 
        <create  @updatelist="(val)=>toUpdateList=val"/>
      </div>

      <div class="headerbody">
        <tablecomponent :gateways="gateways" :value="value" @updatelistDelete="loadGateways(page1, loadPerPage)" />
        <span class="pageInfo">Page {{ page1 }} of {{ Math.max(1, Math.ceil(totalCount1 / pageSize1)) }}</span>

        <div class="pagination">
          <span>Rows:</span>
          <el-input-number v-model="loadPerPage" :step="5" />
          
          <button 
            class="pageBtn" 
            :disabled="page1 <= 1"
            @click="loadGateways(1, loadPerPage)">
            «
          </button>

          <button 
            class="pageBtn" 
            :disabled="!hasPrevious1"  
            @click="loadGateways(page1 - 1, loadPerPage)">
            ‹
          </button>

          <button 
            class="pageBtn"
            v-if="hasPrevious1"
            @click="loadGateways(page1 - 1, loadPerPage)">
            {{ page1 - 1 }}
          </button>

          <button class="pageBtn active">
            {{ page1 }}
          </button>

          <button 
            class="pageBtn" 
            v-if="hasNext1"
            @click="loadGateways(page1 + 1, loadPerPage)">
            {{ page1 + 1 }}
          </button>

          <button 
            class="pageBtn" 
            :disabled="!hasNext1"  
            @click="loadGateways(page1 + 1, loadPerPage)">
            ›
          </button>

          <button 
            class="pageBtn"
            :disabled="Math.ceil(totalCount1 / pageSize1) <= page1"
            @click="loadGateways(Math.max(1, Math.ceil(totalCount1 / pageSize1)), loadPerPage)">
            »
          </button>

          
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.headerpageSidebarIcon{
  display: flex;
}
.page {
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
.sidebarIconButton{
  background-color: #FFFFFF ;
  border-style: none;
  margin-top: 30px;
  margin-left: 15px;
}
.sidebarIconButton:hover{
  background-color: #F9FAFC;
}
.sidebarIcon{
  background-color: #FFFFFF;
  border-bottom:  1px solid #F2F3F7;
  display: none;
}
.headerpage {
  background-color: #FFFFFF;
  padding:20px;
  border-bottom:  1px solid #F2F3F7;
  flex-grow: 1;
  flex-basis: 100%;
  width: 100%;
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
  border:1px solid #F2F3F7;
  border-radius: 8px;
  justify-content: space-evenly;
  margin-bottom: 15px;
  margin-top: 15px;
  padding-top: 15px;
  padding-bottom: 15px;
  margin-left: 15px;
  margin-right: 15px;
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
  padding: 20px;
  height: 30px;
  border-radius: 8px;
  padding-bottom: 30px;
}
.headerbody{
  /* border: 1px solid #F2F3F7; */
  border-radius: 8px;
  margin-top: 30px;
  margin-left: 15px;
  margin-right: 15px;
}
.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 6px;
  /* padding: 15px; */
}
.pageInfo {
  /* margin-right: 700px; */
  font-size: 14px;
  color: #333;
  margin-top: 20px;
  margin-left: 15px;
}
.pageBtn {
  background: white;
  color: black;
  border: 1px solid #ccc;
  width: 32px;
  height: 32px;
  font-size: 14px;
  border-radius: 2px;
  cursor: pointer;
  transition: all 0.2s;
}
.pageBtn:hover:not(:disabled) {
  background: #eee;
}
.pageBtn:disabled {
  background: #f9f9f9;
  color: #aaa;
  cursor: not-allowed;
}
.pageBtn.active {
  background: black;
  color: white;
  font-weight: bold;
}
@media (max-width: 768px) {
  .searchfilter{
    gap: 15px;
  }
  .tablesearch span{
    margin-bottom: 20px;
  }
}
</style>
