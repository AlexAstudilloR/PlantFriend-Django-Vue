// src/store/usePlantsStore.js
import { defineStore } from 'pinia';
import { 
  getPlants, 
  getPlantById, 
  createPlant, 
  updatePlant, 
  deletePlant, 
  getCategories, 
  searchPlantsByName, 
  filterPlantsByCategory 
} from '../services/axios.plants';

export const usePlantsStore = defineStore('plants', {
  state: () => ({
    plants: [],
    plant: null,
    categories: [],
    loading: false,
    error: null,
  }),
  actions: {
    async fetchPlants() {
      this.loading = true;
      try {
        const response = await getPlants();
        this.plants = response.data;
      } catch (error) {
        this.error = error;
      } finally {
        this.loading = false;
      }
    },
    async fetchPlantById(id) {
      this.loading = true;
      try {
        const response = await getPlantById(id);
        this.plant = response.data;
      } catch (error) {
        this.error = error;
      } finally {
        this.loading = false;
      }
    },
    async fetchCategories() {
      this.loading = true;
      try {
        const response = await getCategories();
        this.categories = response.data;
      } catch (error) {
        this.error = error;
      } finally {
        this.loading = false;
      }
    },
    async createPlant(plantData) {
      try {
        await createPlant(plantData);
        await this.fetchPlants();
      } catch (error) {
        this.error = error;
      }
    },
    async updatePlant(id, plantData) {
      try {
        await updatePlant(id, plantData);
        await this.fetchPlants();
      } catch (error) {
        this.error = error;
      }
    },
    async deletePlant(id) {
      try {
        await deletePlant(id);
        await this.fetchPlants();
      } catch (error) {
        this.error = error;
      }
    },

    // Nueva acción para buscar plantas por nombre
    async searchPlantsByName(name) {
      this.loading = true;
      try {
        const response = await searchPlantsByName(name);
        this.plants = response.data;  // Actualiza el estado con las plantas filtradas por nombre
      } catch (error) {
        this.error = error;
      } finally {
        this.loading = false;
      }
    },

    // Nueva acción para filtrar plantas por categoría
    async filterPlantsByCategory(categoryId) {
      this.loading = true;
      try {
        const response = await filterPlantsByCategory(categoryId);
        this.plants = response.data;  // Actualiza el estado con las plantas filtradas por categoría
      } catch (error) {
        this.error = error;
      } finally {
        this.loading = false;
      }
    }
  },
});
