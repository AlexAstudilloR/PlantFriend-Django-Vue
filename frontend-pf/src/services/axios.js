import axios from 'axios';

// Crear instancia de axios
const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api', // Asegúrate de que sea la URL correcta de tu API
  timeout: 10000,
});

// Interceptor de solicitudes para incluir el token JWT
apiClient.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  console.log(localStorage.getItem('token'));
  if (token) {
    config.headers['Authorization'] = `Bearer ${token}`; // Incluye el token en cada solicitud
  }
  return config;
}, (error) => {
  return Promise.reject(error);
});

export default apiClient;
