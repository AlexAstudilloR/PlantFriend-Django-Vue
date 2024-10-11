<template>
    <div>
      <h1>Registro de Usuario</h1>
      <form @submit.prevent="handleRegister">
        <input type="text" v-model="username" placeholder="Nombre de usuario" required />
        <input type="text" v-model="nombre" placeholder="Nombre" required />
        <input type="email" v-model="email" placeholder="Email" required />
        <input type="tel" v-model="telefono" placeholder="Teléfono" required />
        <input type="password" v-model="password" placeholder="Contraseña" required />
        <button type="submit">Registrar</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { useUserStore } from '@/stores/userStore'; // Ajusta la ruta según tu estructura
  
  const userStore = useUserStore();
  const username= ref('')
  const nombre = ref('');
  const email = ref('');
  const telefono = ref('');
  const password = ref('');
  
  const handleRegister = async () => {
    try {
      await userStore.register({ nombre: nombre.value,username:username.value, email: email.value, telefono: telefono.value, password: password.value });
      alert('Registro exitoso');
    } catch (error) {
      alert('Error en el registro. Verifica tus datos.');
    }
  };
  </script>
  