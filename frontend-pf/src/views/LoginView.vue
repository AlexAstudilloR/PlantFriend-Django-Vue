<template>
    <div>
      <h1>Iniciar Sesión</h1>
      <form @submit.prevent="handleLogin">
        <input type="text" v-model="username" placeholder="Nombre de usuario" required />
        <input type="password" v-model="password" placeholder="Contraseña" required />
        <button type="submit">Iniciar Sesión</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { useUserStore } from '@/stores/userStore'; // Ajusta la ruta según tu estructura
  
  const userStore = useUserStore();
  const username = ref('');
  const password = ref('');
  
  const handleLogin = async () => {
    try {
      await userStore.login({ username: username.value, password: password.value });
      alert('Inicio de sesión exitoso');
      // Redireccionar a la página de inicio o donde sea necesario
    } catch (error) {
      alert('Error en el inicio de sesión. Verifica tus credenciales.');
    }
  };
  </script>
  