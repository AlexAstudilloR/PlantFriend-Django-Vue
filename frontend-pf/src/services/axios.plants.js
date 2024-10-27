import apiClient from './axios'; // Instancia configurada de axios con token y CORS

const API_URL = '/auth/plantas/';
const API_URL_CATEGORIES = '/auth/plantas/categoria/';

// Obtener todas las plantas
export const getPlants = () => {
  return apiClient.get(API_URL);
};

// Obtener una planta por su ID
export const getPlantById = (id) => {
  return apiClient.get(`${API_URL}${id}/`);
};

// Crear una nueva planta
export const createPlant = (plantData) => {
  return apiClient.post(API_URL, plantData);
};

// Actualizar una planta existente
export const updatePlant = (id, plantData) => {
  return apiClient.put(`${API_URL}${id}/`, plantData);
};

// Eliminar una planta por su ID
export const deletePlant = (id) => {
  return apiClient.delete(`${API_URL}${id}/`);
};

// Obtener todas las categorías
export const getCategories = () => apiClient.get(API_URL_CATEGORIES);

// Buscar plantas por nombre
export const searchPlantsByName = (name) => {
  return apiClient.get(`${API_URL}buscar/`, { params: { search: name } });
};

// Filtrar plantas por categoría
export const filterPlantsByCategory = (categoryId) => {
  return apiClient.get(`${API_URL}filtrar/${categoryId}/`);
};