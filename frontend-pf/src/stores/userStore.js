import { defineStore } from 'pinia';
import { ref } from 'vue';
import { registerUser, loginUser } from '../services/axios.users'; // Ajusta la ruta según tu estructura

export const useUserStore = defineStore('user', () => {
  const user = ref(null);
  const token = ref(localStorage.getItem('token'));

  // Verificar si el usuario está autenticado
  const isAuthenticated = () => {
    return token.value !== null;
  };

  const register = async (userData) => {
    try {
      const response = await registerUser(userData);
      user.value = response.data.user;
      token.value = response.data.token;
    } catch (error) {
      console.error('Error en el registro:', error);
      throw error;
    }
  };

  const login = async (userData) => {
    try {
      const response = await loginUser(userData);
      token.value = response.data.access;
      localStorage.setItem('token', token.value);
      user.value = response.data.user;
    } catch (error) {
      console.error('Error en el login:', error);
      throw error;
    }
  };

  const logout = () => {
    user.value = null;
    token.value = null;
    localStorage.removeItem('token');
  };

  return { user, token, isAuthenticated, register, login, logout };
});