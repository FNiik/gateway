<!-- set date time parameters -->
<script setup>
import { ref, watch, onMounted, defineEmits } from 'vue';
const datePicked=ref('')
const timePicked=ref('')
const makeRange = (start, end) => {
  const result = []
  for (let i = start; i <= end; i++) {
    result.push(i)
  }
  return result
}

const disabledHours = () => {
  return makeRange(0, 16).concat(makeRange(19, 23))
}

const disabledMinutes = (hour) => {
  if (hour === 17) {
    return makeRange(0, 29)
  }
  if (hour === 18) {
    return makeRange(31, 59)
  }
}

const disabledSeconds = (hour, minute) => {
  if (hour === 18 && minute === 30) {
    return makeRange(1, 59)
  }
}
function formatTime(dateObj) {
  if (!(dateObj instanceof Date)) return dateObj  
  const hh = String(dateObj.getHours()).padStart(2, '0')
  const mm = String(dateObj.getMinutes()).padStart(2, '0')
  const ss = String(dateObj.getSeconds()).padStart(2, '0')
  return `${hh}:${mm}:${ss}`
}

const emit=defineEmits(['selectedDateTime'])
// pass parameters to parent
watch([datePicked,  timePicked],([newDate, newTime])=>{
  if(newDate && newTime){
    emit('selectedDateTime',{date:newDate, time: formatTime(newTime)})
  }
})
</script>
<template>
    <div class="commandRequirment">
        <div class="selectDate">
            <h4>New Date</h4>
            <div class="demo-date-picker">
                <el-date-picker
                v-model="datePicked"
                type="date"
                style="width: 500px;"
                placeholder="Pick a day"
                format="YYYY/MM/DD"
                value-format="YYYY/MM/DD"
                >
                    <template #default="cell">
                        <div class="cell" :class="{ current: cell.isCurrent }">
                            <span class="text">{{ cell.text }}</span>
                        </div>
                    </template>
                </el-date-picker>

            </div>
        </div>
       
    
        <div class="timeSelect">
          <h4>New Time</h4>
          <div class="example-basic">
            <el-time-picker
            v-model="timePicked"
            :disabled-hours="disabledHours"
            :disabled-minutes="disabledMinutes"
            :disabled-seconds="disabledSeconds"
            style="width: 500px;"
            placeholder="Arbitrary time"
            />

          </div>

        </div>


    </div>

</template>
<style scoped>
.timeSelect{
  flex-basis: 50%;
  flex-grow: 1;
  padding: 10px;
  padding-bottom: 30px;
}
.selectDate{
  padding: 10px;
  flex-basis: 50%;
  flex-grow: 1;
  padding-bottom: 30px;
}
.commandRequirment{
    display: flex;
    flex-direction: row;
    /* border-top: 1px solid #F3F4F7; */
    border-bottom:1px solid #F3F4F7 ;
    padding: 20px;
    padding-top: 0px;

    
}
.demo-date-picker {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}

.demo-date-picker > * {
  margin: 0 !important;
}

.cell {
  height: 30px;
  padding: 3px 0;
  box-sizing: border-box;
}

.cell .text {
  width: 24px;
  height: 24px;
  display: block;
  margin: 0 auto;
  line-height: 24px;
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  border-radius: 50%;
}

.cell.current .text {
  background: #626aef;
  color: #fff;
}

.cell .holiday {
  position: absolute;
  width: 6px;
  height: 6px;
  background: var(--el-color-danger);
  border-radius: 50%;
  bottom: 0px;
  left: 50%;
  transform: translateX(-50%);
}

@media screen and (max-width: 768px) {
  .demo-date-picker {
    gap: 1.5rem;
  }
}
h4{
    margin-bottom: 5px;
    margin-top: 0px;
}
</style>