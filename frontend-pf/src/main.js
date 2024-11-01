

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { createVfm } from 'vue-final-modal'
import Vue3Toastify from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';

import App from './App.vue'
import router from './router'

const app = createApp(App)
const vfm= createVfm()
app.use(createPinia())
app.use(router)
app.use(Vue3Toastify, {
    autoClose: 3000, // Opcional: Configuración de cierre automático en milisegundos
  });

app.use(vfm).mount('#app')
