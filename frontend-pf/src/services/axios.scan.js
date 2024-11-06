import apiClient from './axios'; // Instancia configurada de axios con token y CORS

const API_URL = '/auth/scan/';

export const scanPlantImage = async (imageFile) => {
    const formData = new FormData();
    formData.append('image', imageFile);
  
    // Enviar la solicitud a la API
    return await apiClient.post(`${API_URL}escanear/`, formData);
  };