import axios from 'axios';

// Crear instancia de axios
const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api', // Asegúrate de que sea la URL correcta de tu API
  timeout: 10000,
});

// Interceptor de solicitudes para incluir el token JWT
apiClient.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  console.log("Token en localStorage:", token);

  // Evitar agregar el token en rutas de registro o inicio de sesión
  const authRoutes = ['/auth/usuario/register/', '/auth/usuario/login/','/auth/plantas/','/auth/plantas/categoria/'];
  if (token && !authRoutes.includes(config.url)) {
    config.headers['Authorization'] = `Bearer ${token}`; // Incluye el token en cada solicitud excepto en las rutas de autenticación
  }
  return config;
}, (error) => {
  return Promise.reject(error);
});

export default apiClient;