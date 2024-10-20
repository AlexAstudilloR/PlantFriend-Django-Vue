import axios from 'axios';

const API_URL = '/api/auth/plantas/';
const API_URL_CATEGORIES = '/api/auth/plantas/categoria/';

// Obtener todas las plantas
export const getPlants = () => {
  return axios.get(API_URL);
};

// Obtener una planta por su ID
export const getPlantById = (id) => {
  return axios.get(`${API_URL}${id}/`);
};

// Crear una nueva planta
export const createPlant = (plantData) => {
  return axios.post(API_URL, plantData);
};

// Actualizar una planta existente
export const updatePlant = (id, plantData) => {
  return axios.put(`${API_URL}${id}/`, plantData);
};

// Eliminar una planta por su ID
export const deletePlant = (id) => {
  return axios.delete(`${API_URL}${id}/`);
};

// Obtener todas las categorías
export const getCategories = () => axios.get(API_URL_CATEGORIES);

// Buscar plantas por nombre
export const searchPlantsByName = (name) => {
  return axios.get(`${API_URL}buscar/`, { params: { search: name } });
};

// Filtrar plantas por categoría
export const filterPlantsByCategory = (categoryId) => {
  return axios.get(`${API_URL}filtrar/`, { params: { category: categoryId } });
};
