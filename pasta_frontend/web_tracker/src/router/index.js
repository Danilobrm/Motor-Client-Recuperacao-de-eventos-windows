// import Vue from "vue";
import {createRouter, createMemoryHistory} from "vue-router"
import AdmMonitor from '../views/AdmMonitor.vue'
import AdmConfig from '../views/AdmConfig.vue'
import ColaboratorMonitor from '../views/ColaboratorMonitor.vue'

const routes = [
  {
    path: `/`,
    component: AdmMonitor
  },
  {
    path: `/colaborador/:id`,
    component: ColaboratorMonitor
  },
  {
    path: `/config`,
    component: AdmConfig
  },
  {
    path: `/under-construction`
  },
]

const router = createRouter({
  history: createMemoryHistory(),
  routes,
})

export default router;