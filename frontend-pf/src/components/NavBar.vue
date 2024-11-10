<template>
  <nav class="navbar" v-if="!isAuthRoute">
    <div class="navbar-container">
      <router-link to="/home" class="navbar-logo">
        <img src="../assets/imgs/LogoPf.png" alt="PlantFriend" class="img-logo">
      </router-link>
      <ul class="navbar-menu" :class="{ 'is-open': isMenuOpen }">
        <li><router-link to="/home">Home</router-link></li>
        <li><router-link to="/plants">Plantas</router-link></li>
        <li><router-link to="/my-garden">Mi Jardín</router-link></li>
        <li><router-link to="/map">Mapa</router-link></li>
        <li><router-link to="/scan">Escaneo de Planta</router-link></li>
      </ul>
      <div class="navbar-login">
  <router-link v-if="!user" to="/login" class="login-btn">
     Iniciar Sesión
  </router-link>
  <div v-else class="user-info">
    <img :src="profileImage" alt="Foto de perfil" class="profile-pic" v-if="profileImage" />
    <span class="username">{{ user.username }}</span>
    <button @click="logout" class="login-btn">
      <FontAwesomeIcon icon="sign-out-alt" /> Cerrar Sesión
    </button>
  </div>
</div>
      <div class="hamburger" @click="toggleMenu">
        <FontAwesomeIcon icon="bars" />
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref, computed, watch } from 'vue';
import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { faUser, faSignOutAlt, faBars } from '@fortawesome/free-solid-svg-icons';
import { useRoute } from 'vue-router';
import { useUserStore } from '@/stores/userStore';
import noProfilePicture from '../assets/imgs/noProfilePicture.jpg'
library.add(faUser, faSignOutAlt, faBars);

const isMenuOpen = ref(false);
const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value;
};

const userStore = useUserStore();
const user = computed(() => userStore.user);

// Observa cambios en el estado del usuario para actualizar el navbar
watch(user, (newUser) => {
  if (newUser) {
    return
  }
});
const profileImage = computed(() => {
  return user.value?.imagen 
    ? `http://localhost:8000${user.value.imagen}`
    : noProfilePicture;
});

const logout = () => {
  userStore.logout();
};

const route = useRoute();
const isAuthRoute = computed(() => ['login', 'register'].includes(route.name));
</script>
<style scoped>
@import url('../assets/css/navbarHome.css');

.profile-pic {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin-right: 8px;
  box-shadow: rgba(0, 0, 0, 0.12) 0px 1px 3px, rgba(0, 0, 0, 0.24) 0px 1px 2px;
}
.user-info {
  display: flex;
  align-items: center;
  color: green;
}
.username{
  margin-right: 10px;
}
</style>