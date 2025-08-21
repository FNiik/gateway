<script setup>
import { reactive } from 'vue';
const items= reactive({
    netAdapterInfo: false,
    arp: false,
    showRoute:false,
    getDateTime:false,
    setDateTime:false,
    addRoute:false,
    removeRoute:false,
    ping:false,
    traceRoute:false,
    tcpPortTest:false


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


}
 function callCommand(){
    if(items.netAdapterInfo){
        // call netAdapterInfo component
    }
    else if(items.arp){
        // call arp component
    }
    else if(items.showRoute){
        // call showRoute component
    }
    else if(items.getDateTime){
        // call getDateTime component
    }
    else if(items.setDateTime){
        // call setDateTime component
    }
    else if(items.addRoute){
        // call addRoute componet
    }
    else if(items.removeRoute){
        // call removeRoute component
    }
    else if(items.ping){
        // call ping componet
    }
    else if(items.traceRoute){
        // call traceRoute component
    }
    else if(items.tcpPortTest){
        // call tcpPortTest component
    }
 }
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
                <div class="blueItemCard" @click="selectItem('netAdapterInfo')" :class="{ active: items.netAdapterInfo }" >
                    <h4>NetAdapterInfo</h4>
                    
                
                    <span>Get network adapter information</span>

                </div>
                <!-- arp -->
                <div class="blueItemCard" @click="selectItem('arp')" :class="{ active: items.arp }">
                    <h4>Arp</h4>
                    <span>Display Arp table</span>


                </div>
                <!-- showRoute -->
                <div class="blueItemCard" @click="selectItem('showRoute')" :class="{ active: items.showRoute }">
                    <h4>ShowRoute</h4>
                    <span>Show routing table</span>

                </div>
            </div>
            <div class="card">
                <div class="headerItemCard" style="background-color: #F8F5FE; color: #5F349C;">
                    <span>Time management</span>
                </div>
                <!-- getDateTime -->
                <div class="pinkitemCard" @click="selectItem('getDateTime')" :class="{ active: items.getDateTime }">
                    <h4>GetDateTime</h4>
                    <span>Get current date and time</span>

                </div>
                <!-- setDateTime -->
                 <div class="pinkitemCard" @click="selectItem('setDateTime')" :class="{ active: items.setDateTime }">
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
                <div class="greenItemCard" @click="selectItem('addRoute')" :class="{ active: items.addRoute }">
                    <h4>AddRoute</h4>
                    <span>Add a new route</span>
                </div>
                <!--removeRoute  -->
                <div class="greenItemCard" @click="selectItem('removeRoute')" :class="{ active: items.removeRoute }">
                    <h4>RemoveRoute</h4>
                    <span>Remove an existing route</span>
                </div>
            </div>
            <div class="card">
                <div class="headerItemCard" style="background-color: #FDFBEC; color: #724B27;">
                    <span>Network Testing</span>

                </div>
                <!-- ping -->
                <div class="yelowItemCard" @click="selectItem('ping')" :class="{ active: items.ping }">
                    <h4>Ping</h4>
                    <span>Test connectivity to Ip address</span>
                </div>
                <!-- traceRoute -->
                <div class="yelowItemCard" @click="selectItem('traceRoute')" :class="{ active: items.traceRoute }">
                    <h4>TraceRoute</h4>
                    <span>Trace route to destination</span>
                </div>
                <!-- tcpPortTest -->
                <div class="yelowItemCard" @click="selectItem('tcpPortTest')" :class="{ active: items.tcpPortTest }">
                    <h4>TcpPortTest</h4>
                    <span>Test TCP port connectivity </span>
                </div>
            </div>
        </div>
        <div class="commandExecute">
            <div class="headerCommand">
                
            </div>
            <div class="commandExecutebody">
                <!-- callCommand function should be call -->
                {{ callCommand() }}
            </div>
          
        </div>
    </div>

</template>
<style scoped>
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