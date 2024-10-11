// src/stores/userStore.js
import { defineStore } from 'pinia';
import { ref } from 'vue';
import { registerUser, loginUser } from '../services/axios.users'; // Ajusta la ruta según tu estructura

export const useUserStore = defineStore('user', () => {
  const user = ref(null); // Estado para almacenar información del usuario
  const token = ref(null); // Estado para almacenar el token

  // Función para registrar un nuevo usuario
  const register = async (userData) => {
    try {
      const response = await registerUser(userData);
      user.value = response; // Almacena la información del usuario en el store
    } catch (error) {
      console.error('Error en el registro:', error);
      throw error; // Lanza el error para manejarlo en el componente
    }
  };

  // Función para iniciar sesión
  const login = async (userData) => {
    try {
      const response = await loginUser(userData);
      token.value = response.access; // Almacena el token de acceso
      user.value = response.user; // Almacena la información del usuario
    } catch (error) {
      console.error('Error en el login:', error);
      throw error; // Lanza el error para manejarlo en el componente
    }
  };

  // Función para cerrar sesión
  const logout = () => {
    user.value = null; // Limpia la información del usuario
    token.value = null; // Limpia el token
  };

  return { user, token, register, login, logout };
});
