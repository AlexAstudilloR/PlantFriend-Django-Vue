import { defineStore } from 'pinia';
import { ref } from 'vue';
import { getUserGarden, addPlantToGarden, removePlantFromGarden } from '../services/axios.garden';

export const useGardenStore = defineStore('garden', () => {
    const garden = ref([]);

    const fetchUserGarden = async () => {
        try {
            const response = await getUserGarden();
            garden.value = response.data;
        } catch (error) {
            console.log(error);
        }
    };

    const addPlant = async (plantaId) => {
        try {
            await addPlantToGarden(plantaId);  // Aquí envías el plantaId
            await fetchUserGarden();  // Refrescar el jardín
        } catch (error) {
            console.log(error);
        }
    };

    const removePlant = async (plantaId) => {
        try {
            await removePlantFromGarden(plantaId);
            await fetchUserGarden();  // Refrescar el jardín
        } catch (error) {
            console.log(error);
        }
    };

    return {
        garden,
        fetchUserGarden,
        addPlant,
        removePlant,
    };
});
