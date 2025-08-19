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
    for( let item in items){
        if(String(item)===selectItem){
            item=true
        }
        else{
            item=false
        }

    }


}
</script>
<template>
    <div class="page">
        <!--  -->
        <div class="twoCard">
            <div class="card">
                <div class="headerItemCard" style="background-color: powderblue;">
                    <span>Network Information</span>

                </div>
                <!-- netAdapterInfo -->
                <div class="itemCard" @click="selectItem('netAdapterInfo')">
                    <h4>NetAdapterInfo</h4>
                    <span>Get network adapter information</span>

                </div>
                <!-- arp -->
                <div class="itemCard" @click="selectItem('arp')">
                    <h4>Arp</h4>
                    <span>Display Arp table</span>


                </div>
                <!-- showRoute -->
                <div class="itemCard" @click="selectItem('showRoute')">
                    <h4>ShowRoute</h4>
                    <span>Show routing table</span>

                </div>
            </div>
            <div class="card">
                <div class="headerItem" style="background-color: blueviolet;">
                    <span>Time management</span>
                </div>
                <div class="itemcard">

                </div>

            </div>
        </div>
    </div>

</template>
<style scoped>
</style>