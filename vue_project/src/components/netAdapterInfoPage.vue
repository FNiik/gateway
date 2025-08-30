<script setup>
</script>
<template>
    <div class="commandRequirment">
        <div class="nothing">
            <span style="color:gray ;">No parameters required for this command.</span>
        </div>
    </div>
    <!-- <div class="executeButton">
        <button @click="">Execute NetAdapterInfo</button>

    </div>
    <div class="commandResponse">

    </div> -->

</template>
<style scoped>
.commandRequirment{
    display: flex;
    flex-direction: column;
    border-top: 1px solid #F3F4F7;
    border-bottom:1px solid #F3F4F7 ;

    
}
.nothing{
    padding: 20px;
    margin: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    
}
button{
    background-color:#579F55 ;
    height:40px ;
    width:150px ;
    color: white;
    border:none ;
    border-radius:5px ;
}
.executeButton{
    padding: 30px;
}
button:disabled{
    background-color:#98c496 ;
    cursor: not-allowed;
}
</style>
