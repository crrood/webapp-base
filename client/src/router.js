import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from './components/LandingPage.vue'
import Entity from './components/Entity.vue'
import EntityList from './components/EntityList.vue'

const routes = [
  {
    path: '/',
    name: 'LandingPage',
    component: LandingPage
  },
  {
    path: '/entities/:id',
    name: 'Entity',
    component: Entity
  },
  {
    path: '/entities',
    name: 'EntityList',
    component: EntityList
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
