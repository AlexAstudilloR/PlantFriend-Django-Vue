import apiClient from './axios';

// Obtener el jardín del usuario autenticado
export const fetchUserGarden = async () => {
  return await apiClient.get('/auth/garden/');
};

// Agregar una planta al jardín
export const addPlantToGarden = async (plantId) => {
  return await apiClient.post('/auth/garden/add/', { plant_id: plantId });
};

// Eliminar una planta del jardín
export const removePlantFromGarden = async (plantId) => {
  return await apiClient.delete(`/auth/garden/remove/${plantId}/`);
};
