<template>
  <nav class="navbar">
    <div class="navbar-brand">
      <font-awesome-icon :icon="['fas', 'seedling']" />
      <router-link to="/home" class="brand-link">PlantFriends</router-link>
    </div>
    <div class="navbar-main">
      <ul class="navbar-links" :class="{ 'active': isMenuOpen }">
        <li><router-link to="/home">Inicio</router-link></li>
        <li><router-link to="/plants">Plantas</router-link></li>
        <li><router-link to="/my-garden">Mi Jardín</router-link></li>
        <li><router-link to="/map">Viveros</router-link></li>
      </ul>
      <button class="navbar-toggle" @click="toggleMenu">
        <font-awesome-icon :icon="['fas', 'bars']" />
      </button>
    </div>

    <!-- Si el usuario está autenticado, mostramos su nombre -->
    <div class="navbar-auth" v-if="user">
      <span>Bienvenido, {{ user.username }}</span>
      <button @click="logout">Cerrar sesión</button>
    </div>

    <!-- Si el usuario NO está autenticado, mostramos los enlaces para iniciar sesión/registrarse -->
    <div class="navbar-auth" v-else>
      <router-link to="/login">Iniciar sesión</router-link>
      <span class="separator">o</span>
      <router-link to="/register">Registrarse</router-link>
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue';
import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { faSeedling, faBars } from '@fortawesome/free-solid-svg-icons';
import { useUserStore } from '@/stores/userStore'; // Asegúrate de ajustar la ruta del store según tu proyecto

library.add(faSeedling, faBars);

const isMenuOpen = ref(false);
const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value;
};

// Accedemos al store del usuario
const userStore = useUserStore();
const user = userStore.user; // El estado del usuario se almacena en userStore.user

// Función para cerrar sesión
const logout = () => {
  userStore.logout(); // Llama a la función logout del store de usuario
};
</script>

<style scoped>
/* Aquí puedes agregar estilos globales si es necesario */
/* Estilos de la NavBar */
.navbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 20px;
  background-color: #319b5d;
  color: #ecf0f1;
}

.navbar-brand {
  display: flex;
  align-items: center;
  font-size: 1.5em;
}

.navbar-brand .brand-link {
  color: #ecf0f1;
  text-decoration: none;
  margin-left: 5px;
}

/* Contenedor principal para las opciones */
.navbar-main {
  display: flex;
  align-items: center;
  flex-grow: 1;
}

/* Enlaces de navegación */
.navbar-links {
  list-style: none;
  display: flex;
  gap: 20px;
  margin: 0 20px; /* Añade un margen para separarlas del logo */
  padding: 0;
}

.navbar-links li {
  display: flex;
  align-items: center;
}

.navbar-links a {
  color: #ecf0f1;
  text-decoration: none;
  transition: color 0.3s;
}

.navbar-links a:hover {
  color: #006912;
}

/* Área de autenticación */
.navbar-auth {
  display: flex;
  align-items: center;
}

.navbar-auth a {
  color: #ecf0f1;
  text-decoration: none;
  margin: 0 5px;
  transition: color 0.3s;
}

.navbar-auth a:hover {
  color: #006912;
}

.separator {
  color: #ecf0f1;
  margin: 0 5px;
}

/* Estilos para dispositivos móviles */
@media (max-width: 768px) {
  .navbar-links {
    display: none;
    flex-direction: column;
    position: absolute;
    top: 60px;
    left: 0;
    background-color: #0ba34a;
    width: 100%;
    padding: 20px;
  }

  .navbar-links.active {
    display: flex;
  }

  .navbar-toggle {
    display: block;
  }
}

.navbar-toggle {
  display: none;
  background: none;
  border: none;
  color: #ecf0f1;
  font-size: 1.5em;
  cursor: pointer;
}
</style>
