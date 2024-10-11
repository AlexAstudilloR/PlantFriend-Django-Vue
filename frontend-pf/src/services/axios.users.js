import axios from 'axios';

const API_URL = '/api/auth/usuario/';

  export const registerUser= (userData) => {
    return axios.post(`${API_URL}register/`, userData);
  };
  
  export const loginUser= (userData) => {
    return axios.post(`${API_URL}login/`, userData);
  };
