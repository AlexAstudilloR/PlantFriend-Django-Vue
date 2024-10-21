import apiClient from './axios'; // Instancia configurada de axios con token y CORS

const API_URL = '/auth/garden/';

// Obtener el jardín del usuario autenticado
export const getUserGarden = () => {
  return apiClient.get(API_URL);
};

// Agregar una planta al jardín
export const addPlantToGarden = (plantaId) => {
  return apiClient.post(`${API_URL}add/${plantaId}/`, {});  // Pasar el plantaId en la URL
};

// Eliminar una planta del jardín
export const removePlantFromGarden = (plantaId) => {
  return apiClient.delete(`${API_URL}remove/${plantaId}/`);
};
