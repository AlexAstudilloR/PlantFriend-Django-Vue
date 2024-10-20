<template>
  <div v-if="loading">Cargando...</div>
  <div v-else>
    <h3>Buscar Plantas:</h3>

    <!-- Campo de búsqueda por nombre -->
    <div class="search-section">
      <input 
        v-model="searchQuery" 
        type="text" 
        placeholder="Escribe el nombre de la planta" 
        @keyup.enter="searchPlants" 
      />
      <button @click="searchPlants">Buscar</button>

      <!-- Lista desplegable de categorías -->
      <select v-model="selectedCategory" @change="filterByCategory">
        <option value="">Selecciona una categoría</option>
        <option v-for="category in categories" :key="category.id" :value="category.id">
          {{ category.name }}
        </option>
      </select>
    </div>

    <h3>Plantas:</h3>
    <div class="plant-grid">
      <div v-for="plant in plants" :key="plant.id" class="plant-card">
        <h4>{{ plant.nombre }}</h4>
        <p >{{ plant.categoria }}</p>
        <img v-if="plant && plant.imagen" :src="plant.imagen" alt="Imagen de la planta" loading="lazy" />
        <p v-else>No hay imagen disponible</p>
        <button @click="viewGuide(plant.guia)">Ver Guía</button>
      </div>
    </div>
  </div>
  <div v-if="error">{{ error.message }}</div>
</template>

<script>
import { usePlantsStore } from '../stores/PlantsStore';
import { computed, onMounted, ref } from 'vue';

export default {
  setup() {
    const plantsStore = usePlantsStore();
    const searchQuery = ref('');  // Campo de búsqueda
    const selectedCategory = ref('');  // Selección de categoría

    onMounted(() => {
      plantsStore.fetchPlants();
      plantsStore.fetchCategories();
    });

    const searchPlants = async () => {
      if (searchQuery.value) {
        await plantsStore.searchPlantsByName(searchQuery.value);
      } else {
        await plantsStore.fetchPlants();  // Si no hay búsqueda, listar todas las plantas
      }
    };

    const filterByCategory = async () => {
      if (selectedCategory.value) {
        await plantsStore.filterPlantsByCategory(selectedCategory.value);
      } else {
        await plantsStore.fetchPlants();  // Si no hay categoría seleccionada, listar todas las plantas
      }
    };
    
    const viewGuide = (guideId) => {
      // Implementa la lógica para ver la guía, por ejemplo, navegar a una página de guía o abrir un modal
      console.log(`Ver guía con ID: ${guideId}`);
    };

    return {
      plants: computed(() => plantsStore.plants),
      categories: computed(() => plantsStore.categories),
      loading: computed(() => plantsStore.loading),
      error: computed(() => plantsStore.error),
      searchQuery,
      selectedCategory,
      searchPlants,
      filterByCategory,
      viewGuide,
    };
  },

};
</script>

<style>
.search-section {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
  align-items: center;
}

.search-section input {
  padding: 8px;
  width: 200px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.search-section button {
  padding: 8px 12px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.search-section button:hover {
  background-color: #45a049;
}

.search-section select {
  padding: 8px;
  border-radius: 4px;
  border: 1px solid #ccc;
}

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
