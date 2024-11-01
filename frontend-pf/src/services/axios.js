import axios from 'axios';

// Crear instancia de axios
const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api', // Asegúrate de que sea la URL correcta de tu API
  timeout: 10000,
});

// Interceptor de solicitudes para incluir el token JWT
apiClient.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  

  // Evitar agregar el token en rutas de registro o inicio de sesión
  const authRequiredRoutes = [ '/auth/garden/']; // Agrega aquí las rutas que necesitan token

  if (token && authRequiredRoutes.some(route => config.url.startsWith(route))) {
    config.headers['Authorization'] = `Bearer ${token}`; // Incluye el token solo en las rutas que requieren autenticación
  }
  return config;
}, (error) => {
  return Promise.reject(error);
});

export default apiClient;