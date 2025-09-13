<script setup>
import { ref } from 'vue';
import { StretchHorizontal } from 'lucide-vue-next';
import { Hash } from 'lucide-vue-next';
import { Shield } from 'lucide-vue-next';
import { Waypoints } from 'lucide-vue-next';
import { Network } from 'lucide-vue-next';
import { MapPin } from 'lucide-vue-next';
import { ShieldBan } from 'lucide-vue-next';
let gatewayinformation= defineProps({
    gatewayinfo:Object
})

</script>
<template>
<div class="headerAndContainer">
    <div class="header">
        <div class="logoicon">
            <StretchHorizontal  />

        </div>
        <div class="text">
            <h2>
            Gateway Information
            </h2>
        </div>
        

    </div>
    <div class="container">
        <div class="twocard">
            <div class="card">
               <div class="icon">
                <Hash  color="#4769E0"/>
                
                <span class="headerinfocard">Gateway ID</span>


               </div> 
            
            <h4>{{ gatewayinfo.id }}</h4>

        </div>
        <div class="card">
            <div class="icon">
                <Waypoints  color="#D5612F"/>
                
                <span class="headerinfocard">IP Address</span>


               </div> 
            
            <h4>{{ gatewayinfo.ipAddress }}</h4>
        </div>

        </div>
        <div class="twocard">
            <div class="card">
                <div class="icon">
                    <StretchHorizontal color="#8649D4"  />
                    <span class="headerinfocard">Gateway Name</span>
                </div>
            
                <h4>{{ gatewayinfo.name }}</h4>
            </div>
        <div class="card">
            <div class="icon">
                    <Network color="#5A50D5"  />
                    <span class="headerinfocard">Port Number</span>
                </div>
            
            
            <h4>{{ gatewayinfo.portNumber }}</h4>
        </div>

        </div>
        <div class="twocard">
            <div class="card">
                
                <div  class="icon">
                    <Shield v-if="gatewayinfo.status==='ACTIVE'" color="#649A60"  />
                    <ShieldBan v-else color="red"/>
                    <span class="headerinfocard">Status</span>
                </div>
                <h4>{{ gatewayinfo.status }}</h4>
            </div>
            <di class="card">
                <div class="icon">
                    <MapPin color="#538B7E"  />
                    <span class="headerinfocard">location</span>
                </div>
                
                <h4>{{ gatewayinfo.location }}</h4>
            </di>


        </div>
        

        

    </div>
</div>    

</template>
<style scoped>
.card h4{
    margin-top: 15px;
    
}
.headerinfocard{
    color: #697488;
    font-weight:bold ;
    
}

.logoicon{
  background-color: #4E73E8; 
  border-radius: 10px;
  width: 48px;
  height: 48px;
  margin-right: 15px;
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  font-weight: bold;
  font-size: 24px;
  margin-top: 20px;
  margin-left: 15px;
  margin-bottom: 15px;
}
.container{
    display: flex;
    flex-direction: column;
   
}
.twocard{
    display: flex;
    

}
.card{
    flex-basis: 50%;
    border:1px solid #F3F4F7;
    border-radius: 8px;
    padding: 20px;
    margin: 15px;
    background-color: #FFFFFF;
    /* height: 70px; */
    justify-content: center;
    height: 50px;
    align-items: center;
    


}
.card h3{
    margin-bottom: 10px;
    margin-top: 5px;
}
.header{
    border:1px solid #F2F3F7;
    padding: 10px;
    margin: 10px; 
    border-radius: 8px;
    margin-bottom: 0px;
    margin-top: 20px;
    background-color: #FFFFFF;
    display: flex;
    align-items: center;

}
.headerAndContainer{
    display: flex;
    flex-direction: column;
    border:1px solid #E5E5E7;
    border-radius: 8px;
    padding: 20px;
    margin: 15px;
    background-color: #FCFDFF;

    
}
.icon{
    display: flex;
    gap: 7px;
    align-items: center;
}
</style>