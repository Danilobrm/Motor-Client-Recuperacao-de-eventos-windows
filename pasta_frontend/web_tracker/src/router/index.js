// import Vue from "vue";
import { createRouter, createMemoryHistory } from 'vue-router'
import AdmMonitor from '../views/AdmMonitor.vue'
import AdmConfig from '../views/AdmConfig.vue'
import ColaboratorMonitor from '../views/ColaboratorMonitor.vue'

const routes = [
  {
    path: `/`,
    component: AdmMonitor
  },
  {
    path: `/colaborador/:username`,
    name: 'colaborador',
    component: ColaboratorMonitor,
    props: true
  },
  {
    path: `/config`,
    component: AdmConfig
  }
  // {
  //   path: `/under-construction`,
  // },
]

const router = createRouter({
  history: createMemoryHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  localStorage.setItem('rota-atual', to.path)
  console.log(to.params)
  next()
  // localStorage.removeItem('colaboradores')
  // console.log(JSON.parse(localStorage.getItem('colaboradores')))
})

export default router
