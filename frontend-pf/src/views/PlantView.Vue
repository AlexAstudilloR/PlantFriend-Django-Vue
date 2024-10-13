<template>
    <div v-if="loading">Cargando...</div>
    <div v-else>
      <h3>Plantas:</h3>
      <div class="plant-grid">
        <div v-for="plant in plants" :key="plant.id" class="plant-card">
          <h4>{{ plant.nombre }}</h4>
          <p v-for="category in categories" :key="category.id">{{ category.name }}</p>
          <img v-if="plant && plant.imagen" :src="getImageUrl(plant.imagen)" alt="Imagen de la planta" />
          <p v-else>No hay imagen disponible</p>
          <button @click="viewGuide(plant.guia)">Ver Guía</button>
        </div>
      </div>
    </div>
    <div v-if="error">{{ error.message }}</div>
  </template>
  
  <script>
  import { usePlantsStore } from '../stores/PlantsStore';
  import { computed, onMounted } from 'vue';
  
  export default {
    setup() {
      const plantsStore = usePlantsStore();
  
      onMounted(() => {
        plantsStore.fetchPlants();
        plantsStore.fetchCategories();
      });
  
      const viewGuide = (guideId) => {
        // Implementa la lógica para ver la guía, por ejemplo, navegar a una página de guía o abrir un modal
        console.log(`Ver guía con ID: ${guideId}`);
      };
  
      return {
        plants: computed(() => plantsStore.plants),
        categories: computed(() => plantsStore.categories),
        loading: computed(() => plantsStore.loading),
        error: computed(() => plantsStore.error),
        viewGuide,
      };
    },
    methods: {
      getImageUrl(imagePath) {
        const backendBaseURL = 'http://localhost:8000'; // Cambia esto según sea necesario
        return imagePath ? `${backendBaseURL}${imagePath}` : '/ruta/a/placeholder.png';
      }
    }
  };
  </script>
  
  <style>
  .plant-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 20px;
  }
  
  .plant-card {
    border: 1px solid #ddd;
    padding: 15px;
    border-radius: 8px;
    text-align: center;
  }
  
  .plant-card img {
    max-width: 100%;
    height: auto;
    border-radius: 4px;
    margin-bottom: 10px;
  }
  
  .plant-card button {
    padding: 8px 12px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .plant-card button:hover {
    background-color: #45a049;
  }
  </style>
  