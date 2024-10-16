import axios from 'axios';

const API_URL = '/api/auth/plantas/';
const API_URL_CATEGORIES='/api/auth/plantas/categoria/' 
export const getPlants = () => {
  return axios.get(API_URL);
};

export const getPlantById = (id) => {
  return axios.get(`${API_URL}${id}/`);
};

export const createPlant = (plantData) => {
  return axios.post(API_URL, plantData);
};

export const updatePlant = (id, plantData) => {
  return axios.put(`${API_URL}${id}/`, plantData);
};

export const deletePlant = (id) => {
  return axios.delete(`${API_URL}${id}/`);
};

export const getCategories = () => axios.get(API_URL_CATEGORIES);