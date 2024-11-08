// src/services/axios.guide.js
import apiClient from './axios'; // Importa la instancia configurada de axios

const API_URL = '/auth/guias/'; // Asegúrate de que esta sea la ruta correcta

// Obtener todas las guías
export const getGuides = async () => {
  return await apiClient.get(`${API_URL}`);
};

// Obtener una guía específica por ID
export const getGuideById = async (guideId) => {
  const response = await apiClient.get(`${API_URL}${guideId}/`);
  console.log("Respuesta de getGuideById:", response.data); // Verifica la respuesta aquí
  return response;
};

