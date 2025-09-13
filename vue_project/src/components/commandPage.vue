<!--parent command page  -->
<script setup>
import { reactive,ref ,watch} from 'vue';

import NetAdapterInfoPage from './netAdapterInfoPage.vue';
import netAdapterInfoResponsePage from './netAdapterInfoResponsePage.vue';
import arpResponsePage from './arpResponsePage.vue';
import showRouteResponsePage from './showRouteResponsePage.vue';
import getDateTimeResponse from './getDateTimeResponse.vue';
import setDateTimeParameterPage from './setDateTimeParameterPage.vue';
import setDateTimeResponsePage from './setDateTimeResponsePage.vue';
import addRouteParameterPage from './addRouteParameterPage.vue';
import addRouteResponsePage from './addRouteResponsePage.vue';
import pingParameterPage from './pingParameterPage.vue';
import pingResponsePage from './pingResponsePage.vue';
import removeRouteParameterPage from './removeRouteParameterPage.vue';
import removeRouteResponsePage from './removeRouteResponsePage.vue';
import traceRouteParameterPage from './traceRouteParameterPage.vue';
import traceRouteResponsePage from './traceRouteResponsePage.vue';
import tcpPortTestParameterPage from './tcpPortTestParameterPage.vue';
import tcpPortTestResponsePage from './tcpPortTestResponsePage.vue';
import { Play } from 'lucide-vue-next';
const isWaiting = ref(false)
const clickCounter=ref(0)
const items= reactive({
    NetAdapterInfo: false,
    Arp: false,
    ShowRoute:false,
    GetDateTime:false,
    SetDateTime:false,
    AddRoute:false,
    RemoveRoute:false,
    Ping:false,
    TraceRoute:false,
    TcpPortTest:false


})
function selectItem(selectedItem){
    for( let key in items){
        if(key===selectedItem){
            items[key]=true
        }
        else{
            items[key]=false
        }

    }
    clickresponse.value=false


}

const value = ref('NetAdapterInfo')
items[value.value]=true


const options = [
  {
    value: 'NetAdapterInfo',
    label: 'NetAdapterInfo',
  },
  {
    value: 'Arp',
    label: 'Arp',
  },
  {
    value: 'ShowRoute',
    label: 'ShowRoute',
  },
  {
    value: 'GetDateTime',
    label: 'GetDateTime',
  },
  {
    value: 'SetDateTime',
    label: 'SetDateTime',
  },
  {
    value: 'AddRoute',
    label: 'AddRoute',
  },
  {
    value: 'RemoveRoute',
    label: 'RemoveRoute',
  },
  {
    value: 'Ping',
    label: 'Ping',
  },
  {
    value: 'TraceRoute',
    label: 'TraceRoute',
  },
  {
    value: 'TcpPortTest',
    label: 'TcpPortTest',
  },

]

const clickresponse=ref(false)
watch(value, (newVal) => {
    if (newVal!=='') {
    selectItem(newVal)
  }
})
// store given date and time parameters  
const dateTime=ref({date:'', time:''})
function handleSelectedDateTime(emittedval){
    dateTime.value=emittedval

}
const addRouteInfo=ref({destIndex:'',destIp:'',destMask:'',destGateway:'', gatewayIp:'',metric:'',interfaceName:'',interfaceIndex:'' })
function handleAddRouteInfo(emittedval){
  addRouteInfo.value=emittedval
}
const pingTargetIp=ref({ip:''})
function handlePing(emittedval){
  pingTargetIp.value=emittedval

}
const removeRouteInfo=ref({destIndex:'',destIp:'',destMask:'',destGateway:'', gatewayIp:'',metric:'',interfaceName:'',interfaceIndex:'' })
function handleRemoveRoute(emittedval){
  removeRouteInfo.value=emittedval
}
const traceRouteInfo=ref({ip:''})
function handleTraceRoute(emittedval){
  traceRouteInfo.value=emittedval
}
const tcpPortTestInfo=ref({ip:'', port:''})
function tcpPortTestHandler(emittedval){
  tcpPortTestInfo.value=emittedval
}
</script>
<template>
    <div class="page">
        <!--  -->
        <div class="selectParameterButton">
            <div class="headerCommand">
                <h3>gRPC Command Runner</h3>
            </div>
            <!-- start selectCommand -->
             
             <div class="selectDescription">
                <div class="selectcommand">
                    <h4>Select Command</h4>
                    <el-select
                    v-model="value"
                    :options="options"
                    placeholder="Select"
                    style="width: 500px"
                    
                    
                
                />

                </div>
                <div class="descriptionCommand">
                    <h4>Description</h4>
                    <div class="cardDescription" v-if="items.NetAdapterInfo">Get network adapter information</div>
                    <div class="cardDescription" v-if="items.Arp">Display ARP table</div>
                    <div class="cardDescription" v-if="items.ShowRoute">Show routing table</div>
                    <div class="cardDescription" v-if="items.GetDateTime">Get current date and time</div>
                    <div class="cardDescription" v-if="items.SetDateTime">Set system date and time</div>
                    <div class="cardDescription" v-if="items.AddRoute">Add a new route</div>
                    <div class="cardDescription" v-if="items.RemoveRoute">Remove an existing route</div>
                    <div class="cardDescription" v-if="items.Ping">Test connectivity to IP address</div>
                    <div class="cardDescription" v-if="items.TraceRoute">Trace route to destination</div>
                    <div class="cardDescription" v-if="items.TcpPortTest">Test TCP port connectivity</div>
                    
                </div>
                
                
    

             </div>
        
            <!-- end selectCommand -->

            <!-- start commandParameters -->
            <!-- <div class="commandExecute"> -->
                <div class="headerCommand" style="padding-left: 10px; padding-top: 5px;">
                    <h3  v-for="key in Object.keys(items).filter(k => items[k]===true && !['NetAdapterInfo', 'Arp', 'ShowRoute', 'GetDateTime'].includes(k))"
                     :key="key"> {{ key }} Parameters</h3>
        
                </div>
                <div class="commandExecutebody">
                    <!-- callCommand function should be call -->
                    
                    <set-date-time-parameter-page v-if="items.SetDateTime" @selected-date-time="handleSelectedDateTime"/>
                    <add-route-parameter-page v-if="items.AddRoute" @add-route-parameters="handleAddRouteInfo" />
                    <ping-parameter-page v-if="items.Ping" @ping-parameter="handlePing" />
                    <remove-route-parameter-page v-if="items.RemoveRoute" @remove-route-parameters="handleRemoveRoute"/>
                    <trace-route-parameter-page v-if="items.TraceRoute" @trace-route-parameter="handleTraceRoute"/>
                    <tcp-port-test-parameter-page v-if="items.TcpPortTest" @tcp-port-test-parameter="tcpPortTestHandler"/>
                    

                    
        
        
                    <div class="executeButton">
                        
                        <button class="buttonicon" @click="clickresponse=true, clickCounter++" :disabled="isWaiting" v-for="key in Object.keys(items).filter(k => items[k])" :key="key" > <Play size="20"/>Execute </button>
                    </div>
        
    
                </div>
    
    



  
            <!-- </div> -->
        
            <!-- end commandParameters -->

        </div>
        <!-- start commandResponse -->
        <div class="commandResponse" v-if="clickresponse">
                <div class="headerCommand">
                    <h3  v-for="key in Object.keys(items).filter(k => items[k])"
                        :key="key"> {{ key }} Response </h3>
                
                
                </div>
                <!-- call responsecommand commponents -->
                 <net-adapter-info-response-page :execute-counter="clickCounter" @update-wait="(val)=>isWaiting=val" v-if="items.NetAdapterInfo"/>
                 <arp-response-page :execute-counter="clickCounter" @update-wait="(val)=>isWaiting=val" v-if="items.Arp"   />
                 <show-route-response-page :execute-counter="clickCounter" @update-wait="(val)=>isWaiting=val" v-if="items.ShowRoute"   />
                 <get-date-time-response :execute-counter="clickCounter" @update-wait="(val)=>isWaiting=val" v-if="items.GetDateTime"   />
                 <!-- new date and time to the setdatetime response via props  -->
                 <set-date-time-response-page :execute-counter="clickCounter" @update-wait="(val)=>isWaiting=val" v-if="items.SetDateTime" :new-date-picked="dateTime.date" :new-time-picked="dateTime.time"  />   
                 <add-route-response-page :execute-counter="clickCounter" @update-wait="(val)=>isWaiting=val" v-if="items.AddRoute" 
                  :new-dest-index="addRouteInfo.destIndex"
                  :new-dest-ip="addRouteInfo.destIp"
                  :new-dest-mask="addRouteInfo.destMask"
                  :new-dest-gateway="addRouteInfo.destGateway"
                  :new-gateway-ip="addRouteInfo.gatewayIp"
                  :new-interface-index="addRouteInfo.interfaceIndex"
                  :new-interface-name="addRouteInfo.interfaceName"
                  :new-metric="addRouteInfo.metric"
                  />
                  
                  <ping-response-page :execute-counter="clickCounter" @update-wait="(val)=>isWaiting=val" v-if="items.Ping" :target-ip="pingTargetIp.ip" />
                  <remove-route-response-page :execute-counter="clickCounter" @update-wait="(val)=>isWaiting=val" v-if="items.RemoveRoute"
                    :new-dest-index="removeRouteInfo.destIndex"
                  :new-dest-ip="removeRouteInfo.destIp"
                  :new-dest-mask="removeRouteInfo.destMask"
                  :new-dest-gateway="removeRouteInfo.destGateway"
                  :new-gateway-ip="removeRouteInfo.gatewayIp"
                  :new-interface-index="removeRouteInfo.interfaceIndex"
                  :new-interface-name="removeRouteInfo.interfaceName"
                  :new-metric="removeRouteInfo.metric" 

                   />
                  <trace-route-response-page :execute-counter="clickCounter" @update-wait="(val)=>isWaiting=val" v-if="items.TraceRoute" :target-ip="traceRouteInfo.ip"/>
                  <tcp-port-test-response-page :execute-counter="clickCounter" @update-wait="(val)=>isWaiting=val" v-if="items.TcpPortTest" :target-ip="tcpPortTestInfo.ip" :port="tcpPortTestInfo.port"/>
                    
                  
                  

                       
            </div>
            <!-- end commandResponse -->
    </div>

</template>
<style scoped>

.cardDescription{
  height: 15px;  
  display: flex;
  align-items: center;
  padding: 8px 12px;
  background-color: #F9FAFC;
  border: 1px solid #F3F4F7;
  border-radius: 5px;
  /* margin: 10px; */
  

}

.descriptionCommand{
    display: flex;
    flex-direction: column;
    flex-basis: 50%;
    margin: 7px;
    gap: 0px;

}
.selectcommand{
    display: flex;
    flex-direction: column;
    flex-basis: 50%;
    margin: 7px;
    gap: 0px;
}
.selectDescription{
    display: flex;
    flex-direction: row;
    border-top: 1px solid #F3F4F7;
    border-bottom:1px solid #F3F4F7 ;
    padding: 20px;
    align-items: stretch;

}
.selectParameterButton{
    display: flex;
    flex-direction: column;
    margin: 15px;
    border:1px solid #F3F4F7;
    border-radius: 8px;
}
.commandResponse{
    margin: 15px;
    border:1px solid #F3F4F7;
    border-radius: 8px;
}
button{
    background-color:#579F55 ;
    height:40px ;
    width:150px ;
    color: white;
    border:none ;
    border-radius:5px ;
    cursor: pointer;

}
button:disabled{
    background-color:#a0ca9e ;
    cursor: not-allowed;
}
.executeButton{
    padding: 30px;
    
  
}
.buttonicon{
  align-items: center;
    display: flex;
  justify-content: center;
  gap: 10px;  

}
.commandExecute{
    display: flex;
    flex-direction: column;
    margin: 15px;
    border:1px solid #F3F4F7;
    border-radius: 8px;
}
.headerCommand{
   
    padding-left: 15px;
    padding-top: 5px;
    padding-bottom: 5px;
}
.headerCommandParameter{
  /* padding: 15px; */
  
}
.headerCommandParameter h3{
  /* margin-bottom: 0px; */
}
/* .headerCommand h3{
  margin-bottom: 0px;
} */
.page{
    display: flex;
    flex-direction: column;
    /* padding: 20px; */
    /* margin-left: 0px; */
}
.twoCard{
    display: flex;
    flex-direction: row;
}
.card{
    flex-basis: 50%;
    border:1px solid #F3F4F7;
    border-radius: 8px;
    padding: 20px;
    margin: 15px;
    background-color: #FFFFFF;
}
.itemCard{
    border:1px solid #F3F4F7;
    border-radius: 8px;
}
.itemCard:hover{
    background-color:#F9FAFC;

}
.blueItemCard{
    border:1px solid #F3F4F7;
    border-radius: 8px;
    margin-bottom: 20px;
    display: flex;
    flex-direction: column;
    align-items:flex-start;
    justify-content: center;
    padding: 12px;
    cursor: pointer;

    

}
.blueItemCard h4 {
  margin: 0 0 4px 0;
  font-size: 16px;
}
.blueItemCard span {
  font-size: 14px;
  color: #555;
}
.blueItemCard:hover{
    background-color:#F9FAFC;
}
.blueItemCard:active{
    background-color: #DFEAFC;
}
.pinkitemCard{
    border:1px solid #F3F4F7;
    border-radius: 8px;
    margin-bottom: 20px;
    display: flex;
    flex-direction: column;
    align-items:flex-start;
    justify-content: center;
    padding: 12px;
    cursor: pointer;

}
.pinkitemCard:hover{
    background-color:#F9FAFC;
}
.pinkitemCard:active{
    background-color: #E6D9FF;
}
.greenItemCard{
    border:1px solid #F3F4F7;
    border-radius: 8px;
    margin-bottom: 20px;
    display: flex;
    flex-direction: column;
    align-items:flex-start;
    justify-content: center;
    padding: 12px;
    cursor: pointer;

}
.greenItemtemCard:hover{
    background-color:#F9FAFC;
}
.greenItemCard:active{
    background-color: #BFFFCC;
}
.yelowItemCard{
    border:1px solid #F3F4F7;
    border-radius: 8px;
    margin-bottom: 20px;
    display: flex;
    flex-direction: column;
    align-items:flex-start;
    justify-content: center;
    padding: 12px;
    cursor: pointer;

}
.yelowItemtemCard:hover{
    background-color:#F9FAFC;
}
.yelowItemCard:active{
    background-color: #FFF7BF;
}
.headerItemCard{
    height: 60px;
    /* border-radius: 8px; */
    align-items: center;
    display: flex;
    padding-left: 20px;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
    
}
.pinkitemCard h4 {
  margin: 0 0 4px 0;
  font-size: 16px;
}
.pinkitemCard span {
  font-size: 14px;
  color: #555;
}
.greenItemCard h4 {
  margin: 0 0 4px 0;
  font-size: 16px;
}
.greenItemCard span {
  font-size: 14px;
  color: #555;
}
.yelowItemCard h4 {
  margin: 0 0 4px 0;
  font-size: 16px;
}
.yelowItemCard span {
  font-size: 14px;
  color: #555;
}
.blueItemCard.active {
  background-color: #DFEAFC;
}

.pinkitemCard.active {
  background-color: #E6D9FF;
}

.greenItemCard.active {
  background-color: #BFFFCC;
}

.yelowItemCard.active {
  background-color: #FFF7BF;
}
h4{
    margin-top: 5px;
    margin-bottom: 9px;
}
.popper-class{
  background-color: #555;
  color:red;
}
</style>