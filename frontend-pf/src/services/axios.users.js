import apiClient from './axios'; // La instancia configurada de axios con el token y CORS

const API_URL = '/auth/usuario/';



export const registerUser = async (FormData) => {
  return await apiClient.post(`${API_URL}register/`, FormData);
};
export const loginUser = (userData) => {
  return apiClient.post(`${API_URL}login/`, userData);
};
