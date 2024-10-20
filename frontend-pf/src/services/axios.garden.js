import axios from 'axios';

const API_URL = '/api/auth/garden/';

// Obtener el jardín del usuario autenticado
export const getUserGarden = () => {
  return axios.get(API_URL, {
    headers: {
      Authorization: `Bearer ${localStorage.getItem('token')}`
    }
  });
};

// Agregar una planta al jardín
export const addPlantToGarden = (plantaId) => {
    return axios.post(`${API_URL}add/${plantaId}/`, {}, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`
      }
    });
  };

// Eliminar una planta del jardín
export const removePlantFromGarden = (plantaId) => {
  return axios.delete(`${API_URL}remove/${plantaId}/`, {
    headers: {
      Authorization: `Bearer ${localStorage.getItem('token')}`
    }
  });
};
