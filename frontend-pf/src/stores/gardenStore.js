// gardenStore.js
import { defineStore } from 'pinia';
import { ref } from 'vue';
import { fetchUserGarden, addPlantToGarden, removePlantFromGarden } from '../services/axios.garden';

export const useGardenStore = defineStore('garden', () => {
  const garden = ref([]);
  const loading = ref(false);

  // Obtener el jardín del usuario
  const getGarden = async () => {
    loading.value = true;
    try {
      const response = await fetchUserGarden();
      garden.value = response.data.plants; // Asigna las plantas en el jardín al estado
    } catch (error) {
      console.error('Error al obtener el jardín:', error);
    } finally {
      loading.value = false;
    }
  };

  // Agregar una planta al jardín
  const addPlant = async (plantId) => {
    try {
      await addPlantToGarden(plantId);
      await getGarden(); // Recargar el jardín después de agregar la planta
    } catch (error) {
      console.error('Error al agregar la planta:', error);
    }
  };

  // Eliminar una planta del jardín
  const removePlant = async (plantId) => {
    try {
      await removePlantFromGarden(plantId);
      await getGarden(); // Recargar el jardín después de eliminar la planta
    } catch (error) {
      console.error('Error al eliminar la planta:', error);
    }
  };

  return { garden, loading, getGarden, addPlant, removePlant };
});
