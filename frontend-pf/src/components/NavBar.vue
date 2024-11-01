<template>
  <nav class="navbar" v-if="!isAuthRoute">
    <div class="navbar-container">
      <router-link to="/home" class="navbar-logo">
        <img src="../assets/imgs/LogoPf.png" alt="PlantFriend" class="img-logo">
      </router-link>
      <ul class="navbar-menu" :class="{ 'is-open': isMenuOpen }">
        <li><router-link to="/home"> Home</router-link></li>
        <li><router-link to="/plants"> Plantas</router-link></li>
        <li><router-link to="/my-garden"> Mi Jardín</router-link></li>
        <li><router-link to="/map"> Mapa</router-link></li>
        <li><router-link to="/scan">Escaneo de Planta</router-link></li>
      </ul>
      <div class="navbar-login">
        <router-link v-if="!user" to="/login" class="login-btn">
           Iniciar Sesión
        </router-link>
        <router-link v-if="!user" to="/register" class="register-btn">
          Registrarse
        </router-link>
        <button v-else @click="logout" class="logout-btn">
          <FontAwesomeIcon icon="sign-out-alt" /> Cerrar Sesión
        </button>
      </div>
      <div class="hamburger" @click="toggleMenu">
        <FontAwesomeIcon icon="bars" />
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref, computed } from 'vue';
import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import {  faUser, faSignOutAlt , faBars} from '@fortawesome/free-solid-svg-icons';
import { useRoute } from 'vue-router';
import { useUserStore } from '@/stores/userStore';

library.add( faUser, faSignOutAlt, faBars);

const isMenuOpen = ref(false);
const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value;
};

const userStore = useUserStore();
const user = computed(() => userStore.user);

const logout = () => {
  userStore.logout();
};

const route = useRoute();
const isAuthRoute = computed(() => ['login', 'register'].includes(route.name));
</script>


<style >
@import url('../assets/css/navbarHome.css');
</style>
