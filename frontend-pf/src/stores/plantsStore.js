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
  filterPlantsByCategory,
  searchPlantsByScientificName,
  getPlantByGuideId
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
    async searchPlantsByName(name) {
      this.loading = true;
      try {
        const response = await searchPlantsByName(name);
        this.plants = response.data;
      } catch (error) {
        this.error = error;
      } finally {
        this.loading = false;
      }
    },
    async filterPlantsByCategory(categoryId) {
      this.loading = true;
      try {
        const response = await filterPlantsByCategory(categoryId);
        this.plants = response.data;
      } catch (error) {
        this.error = error;
      } finally {
        this.loading = false;
      }
    },
    async searchPlantsByScientificName(scientificName) {
      this.loading = true;
      try {
        const response = await searchPlantsByScientificName(scientificName);
        this.plants = response.data;
      } catch (error) {
        this.error = error;
      } finally {
        this.loading = false;
      }
    },
    async fetchPlantByGuideId(guideId) {
      this.loading = true;
      try {
        const response = await getPlantByGuideId(guideId);
        this.plant = response.data;
      } catch (error) {
        this.error = error;
      } finally {
        this.loading = false;
      }
    },
  },
});
