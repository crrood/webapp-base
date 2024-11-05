import { createRouter, createWebHistory } from 'vue-router'
import Entity from './components/Entity.vue'
import EntityList from './components/EntityList.vue'
import LandingPage from './components/LandingPage.vue'

const routes = [
  {
    path: '/',
    name: 'LandingPage',
    component: LandingPage
  },
  {
    path: '/entity/:id',
    name: 'Entity',
    component: Entity
  },
  {
    path: '/entity',
    name: 'EntityList',
    component: EntityList
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
