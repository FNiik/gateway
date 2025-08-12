// index.js
import {createRouter, createWebHistory} from 'vue-router'
import gatewaylist from '@/pages/gatewaylist.vue'
import gatewaydetail from '@/pages/gatewaydetail.vue'


const routes = [
    {path:'/', name:'gatewaylist', component:gatewaylist},
    // {path:'gateway/:id', name:'gatewaydetail', component:gatewaydetail}
    

]

 const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes
  })
export default router  