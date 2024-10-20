import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import LoginView from '@/views/LoginView.vue'
import SignUpView from '@/views/SignUpView.vue'
import HomeView from '@/views/HomeView.vue'
import PlantView from '@/views/PlantView.vue'
import MapView from '@/views/MapView.vue'
import GardenView from '@/views/GardenView.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/register',
      name: 'register',
      component: SignUpView
    },
    {
      path: '/home',
      name: 'home',
      component: HomeView
    },
    {
      path: '/plants',
      name: 'plants',
      component: PlantView
    },
    {
      path: '/map',
      name: 'map',
      component: MapView
    },
    {
      path: '/my-garden',
      name: 'garden',
      component: GardenView
    }
  ]
})

export default router
