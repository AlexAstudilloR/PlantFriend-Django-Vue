// En tu store `gardenStore.js`
import { defineStore } from 'pinia';
import { ref } from 'vue';
import { fetchUserGarden, addPlantToGarden, removePlantFromGarden } from '../services/axios.garden';

export const useGardenStore = defineStore('garden', () => {
  const garden = ref([]); // Aseguramos que `garden` sea un array
  const loading = ref(false);

  const getGarden = async () => {
    loading.value = true;
    try {
      const response = await fetchUserGarden();
      garden.value = response.data.length > 0 ? response.data : []; // Asegura que garden siempre tenga un array
    } catch (error) {
      console.error('Error al obtener el jardín:', error);
      garden.value = []; // Si hay un error, asigna un array vacío
    } finally {
      loading.value = false;
    }
  };

  const addPlant = async (plantId) => {
    try {
      await addPlantToGarden(plantId);
      await getGarden();
    } catch (error) {
      console.error('Error al agregar la planta al jardín:', error);
    }
  };

  const removePlant = async (plantId) => {
    try {
      await removePlantFromGarden(plantId);
      await getGarden();
    } catch (error) {
      console.error('Error al eliminar la planta del jardín:', error);
    }
  };
  const resetGarden = () => {
    garden.value = [];
  };

  return { garden, loading, getGarden, addPlant, removePlant, resetGarden};
});
