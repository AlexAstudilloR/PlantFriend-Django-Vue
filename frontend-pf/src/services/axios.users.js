import apiClient from './axios'; // La instancia configurada de axios con el token y CORS

const API_URL = '/auth/usuario/';

export const registerUser = (userData) => {
  const formData = new FormData();
  formData.append('nombre', userData.nombre);
  formData.append('username', userData.username);
  formData.append('email', userData.email);
  formData.append('telefono', userData.telefono);
  formData.append('password', userData.password);
  
  // Agrega la imagen como archivo al FormData
  if (userData.imagen) {
    formData.append('imagen', userData.imagen);
  }

  return apiClient.post(`${API_URL}register/`, formData, {
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  });
};

export const loginUser = (userData) => {
  return apiClient.post(`${API_URL}login/`, userData);
};
