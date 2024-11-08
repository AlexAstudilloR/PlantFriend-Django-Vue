import { defineStore } from 'pinia';
import { ref } from 'vue';
import { getGuides,getGuideById} from '../services/axios.guides';

export const useGuideStore = defineStore('guide', () => {
  // Estado del store
  const guides = ref([]);
  const loading = ref(false);
  const error = ref(null);
  const guide = ref(null);

  // Acción para obtener todas las guías
  const fetchGuides = async () => {
    loading.value = true;
    error.value = null;
    try {
      const response = await getGuides();
      guides.value = response.data; // Almacena las guías en el estado
    } catch (err) {
      error.value = 'Error al obtener las guías';
      console.error(err);
    } finally {
      loading.value = false;
    }
  };
  // Acción para obtener una guía específica por ID
  const fetchGuideById = async (guideId) => {
    loading.value = true;
    error.value = null;
    try {
      const response = await getGuideById(guideId);
      guide.value = response.data; // Almacena la guía específica en el estado
    } catch (err) {
      error.value = 'Error al obtener la guía';
      console.error(err);
    } finally {
      loading.value = false;
    }
  };


  // Retorna el estado y las acciones para usar en los componentes
  return {
    guide,
    guides,
    loading,
    error,
    fetchGuides,
    fetchGuideById
  };
});