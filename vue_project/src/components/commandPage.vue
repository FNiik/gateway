<script setup>
import { reactive,ref } from 'vue';

import NetAdapterInfoPage from './netAdapterInfoPage.vue';
import netAdapterInfoResponsePage from './netAdapterInfoResponsePage.vue';
import arpResponsePage from './arpResponsePage.vue';
import showRouteResponsePage from './showRouteResponsePage.vue';
import getDateTimeResponse from './getDateTimeResponse.vue';

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
const clickresponse=ref(false)
 
</script>
<template>
    <div class="page">
        <!--  -->
        <div class="twoCard">
            
            <div class="card">
                <div class="headerItemCard" style="background-color: #DFEAFC; color: #3352A0;">
                    <span>Network Information</span>

                </div>
                <!-- netAdapterInfo -->
                <div class="blueItemCard" @click="selectItem('NetAdapterInfo')" :class="{ active: items.NetAdapterInfo }" >
                    <h4>NetAdapterInfo</h4>
                    
                
                    <span>Get network adapter information</span>

                </div>
                <!-- arp -->
                <div class="blueItemCard" @click="selectItem('Arp')" :class="{ active: items.Arp }">
                    <h4>Arp</h4>
                    <span>Display Arp table</span>


                </div>
                <!-- showRoute -->
                <div class="blueItemCard" @click="selectItem('ShowRoute')" :class="{ active: items.ShowRoute }">
                    <h4>ShowRoute</h4>
                    <span>Show routing table</span>

                </div>
            </div>
            <div class="card">
                <div class="headerItemCard" style="background-color: #F8F5FE; color: #5F349C;">
                    <span>Time management</span>
                </div>
                <!-- getDateTime -->
                <div class="pinkitemCard" @click="selectItem('GetDateTime')" :class="{ active: items.GetDateTime }">
                    <h4>GetDateTime</h4>
                    <span>Get current date and time</span>

                </div>
                <!-- setDateTime -->
                 <div class="pinkitemCard" @click="selectItem('SetDateTime')" :class="{ active: items.SetDateTime }">
                    <h4>SetDateTime</h4>
                    <span>Set system date and time</span>
                 </div>

            </div>
        </div>
        <div class="twoCard">
            <div class="card">
                <div class="headerItemCard" style="background-color: #F3FDF5;">
                    <span color="#326452">Routing Management</span>
                </div>
                <!-- addRoute -->
                <div class="greenItemCard" @click="selectItem('AddRoute')" :class="{ active: items.AddRoute }">
                    <h4>AddRoute</h4>
                    <span>Add a new route</span>
                </div>
                <!--removeRoute  -->
                <div class="greenItemCard" @click="selectItem('RemoveRoute')" :class="{ active: items.RemoveRoute }">
                    <h4>RemoveRoute</h4>
                    <span>Remove an existing route</span>
                </div>
            </div>
            <div class="card">
                <div class="headerItemCard" style="background-color: #FDFBEC; color: #724B27;">
                    <span>Network Testing</span>

                </div>
                <!-- ping -->
                <div class="yelowItemCard" @click="selectItem('Ping')" :class="{ active: items.Ping }">
                    <h4>Ping</h4>
                    <span>Test connectivity to Ip address</span>
                </div>
                <!-- traceRoute -->
                <div class="yelowItemCard" @click="selectItem('TraceRoute')" :class="{ active: items.TraceRoute }">
                    <h4>TraceRoute</h4>
                    <span>Trace route to destination</span>
                </div>
                <!-- tcpPortTest -->
                <div class="yelowItemCard" @click="selectItem('TcpPortTest')" :class="{ active: items.TcpPortTest }">
                    <h4>TcpPortTest</h4>
                    <span>Test TCP port connectivity </span>
                </div>
            </div>
        </div>
        <div class="commandExecute">
            <div class="headerCommand">
                <h4  v-for="key in Object.keys(items).filter(k => items[k])"
                    :key="key"> {{ key }}</h4>
                
            </div>
            <div class="commandExecutebody">
                <!-- callCommand function should be call -->
                <NetAdapterInfoPage  v-if="items.NetAdapterInfo"/>
                <NetAdapterInfoPage  v-if="items.Arp"/>
                <NetAdapterInfoPage  v-if="items.ShowRoute"/>
                <NetAdapterInfoPage  v-if="items.GetDateTime"/>
                
                
                <div class="executeButton">
                    <button @click="clickresponse=true, clickCounter++" :disabled="isWaiting" v-for="key in Object.keys(items).filter(k => items[k])" :key="key" >Execute {{key  }}</button>
                </div>
                
            
            </div>
            
            
        

    
          
        </div>
        <div class="commandResponse" v-if="clickresponse">
                <div class="headerCommand">
                    <h4  v-for="key in Object.keys(items).filter(k => items[k])"
                        :key="key"> {{ key }} Response</h4>
                
                
                </div>
                <!-- call responsecommand commponents -->
                 <net-adapter-info-response-page :execute-counter="clickCounter" @update-wait="(val)=>isWaiting=val" v-if="items.NetAdapterInfo"/>
                 <arp-response-page :execute-counter="clickCounter" @update-wait="(val)=>isWaiting=val" v-if="items.Arp"   />
                 <show-route-response-page :execute-counter="clickCounter" @update-wait="(val)=>isWaiting=val" v-if="items.ShowRoute"   />
                 <get-date-time-response :execute-counter="clickCounter" @update-wait="(val)=>isWaiting=val" v-if="items.GetDateTime"   />   
            </div>
    </div>

</template>
<style scoped>
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
.commandExecute{
    display: flex;
    flex-direction: column;
    margin: 15px;
    border:1px solid #F3F4F7;
    border-radius: 8px;
}
.headerCommand{
   
    padding: 10px;
}
.page{
    display: flex;
    flex-direction: column;
    /* padding: 20px; */
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

</style>