import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '@/views/LoginView.vue'
import SignUpView from '@/views/SignUpView.vue'
import HomeView from '@/views/HomeView.vue'
import PlantView from '@/views/PlantView.vue'
import MapView from '@/views/MapView.vue'
import GardenView from '@/views/GardenView.vue'
import ScanView from '@/views/ScanView.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/home'
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
    },
    {
      path: '/scan',
      name: 'scan',
    component: ScanView    }

  ]
})

export default router
