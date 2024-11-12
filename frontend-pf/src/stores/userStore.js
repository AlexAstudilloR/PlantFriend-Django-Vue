// userStore.js
import { defineStore } from 'pinia';
import { ref, computed } from 'vue';
import { registerUser, loginUser } from '../services/axios.users';

export const useUserStore = defineStore('user', () => {
  const user = ref(null);
  const token = ref(localStorage.getItem('token'));

  // Computed para verificar si está autenticado
  const isAuthenticated = computed(() => token.value !== null);

  const register = async (userData) => {
    try {
      const response = await registerUser(userData);
      user.value = response.data.user;
      token.value = response.data.token;
      localStorage.setItem('token', token.value);
    } catch (error) {
      console.error('Error en el registro:', error.response ? error.response.data : error);
      throw error;
    }
  };

  const login = async (userData) => {
    try {
      const response = await loginUser(userData);
      user.value = response.data.user;
      token.value = response.data.access;
      localStorage.setItem('token', token.value);
    } catch (error) {
      console.error('Error en el login:', error.response ? error.response.data : error);
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
