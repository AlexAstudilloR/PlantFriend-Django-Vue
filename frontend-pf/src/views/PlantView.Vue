<template>
  <div>
    <!-- Campo de búsqueda y selección de categoría -->
    <div class="search-filter-container">
      <input
        type="text"
        id="searchBar"
        placeholder="Buscar por nombre de planta..."
        v-model="searchQuery"
        @input="searchPlants"
      />
      <div class="filter-dropdown">
        <button class="filter-button">
          Filtrar <font-awesome-icon :icon="['fas', 'filter']" /> 
        </button>
          <select class="dropdown-content" id="filterOptions" v-model="selectedCategory" @change="filterByCategory">
            <option value="">Todas las Categorías</option>
            <option v-for="category in categories" :key="category.id" :value="category.name">
              {{ category.name }}
            </option>
          </select>
      </div>
    </div>
    
    <!-- Lista de Plantas -->
    <div class="plants-list">
      <PlantsCards
        v-for="plant in plants"
        :key="plant.id"
        :plant="plant"
        @view-guide="viewGuide"
        @add-to-garden="addToGarden"
      />
    </div>
  </div>
</template>

<script setup>
import PlantsCards from '../components/plants/PlantsCards.vue';
import { usePlantsStore } from '../stores/PlantsStore';
import { computed, onMounted, ref } from 'vue';
import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import {faFilter} from '@fortawesome/free-solid-svg-icons'
// Store y propiedades de estado
library.add(faFilter)
const plantsStore = usePlantsStore();
const searchQuery = ref('');
const selectedCategory = ref('');

// Cargar las plantas y categorías al montar el componente
onMounted(() => {
  plantsStore.fetchPlants();
  plantsStore.fetchCategories();
});

// Función para buscar plantas
const searchPlants = async () => {
  if (searchQuery.value) {
    await plantsStore.searchPlantsByName(searchQuery.value);
  } else {
    await plantsStore.fetchPlants();
  }
};

// Función para filtrar por categoría
const filterByCategory = async () => {
  if (selectedCategory.value) {
    await plantsStore.filterPlantsByCategory(selectedCategory.value);
  } else {
    await plantsStore.fetchPlants();
  }
};

// Manejar eventos de guía y agregar al jardín
const viewGuide = (guideId) => {
  console.log(`Ver guía con ID: ${guideId}`);
};

const addToGarden = (plantId) => {
  console.log(`Agregar planta con ID: ${plantId} al jardín`);
  // Aquí podrías llamar a una función en la store o enviar una solicitud a la API para agregar la planta al jardín
};

// Computed properties para los datos de la store
const plants = computed(() => plantsStore.plants);
const categories = computed(() => plantsStore.categories);

</script>

<style>
a{
    text-decoration: none;
    color: white;
}

.plant-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    padding: 20px;
    position: relative;
}

.plant-card {
    border: 1px solid #fffdfd;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    margin: 10px;
    padding: 20px;
    text-align: center;
    padding-top: 10px;
}

.plant-card img {
    width: 250px;
    height: 240px;
    border-radius: 8px;
}

button {
    background-color: #4CAF50;
    color: white;
    border: none;
    padding: 10px 20px;
    text-align: center;
    text-decoration: none;
    font-size: 16px;
    border-radius: 4px;
    cursor: pointer;
}
.boton-guia{
    margin-bottom: 5px;
}
/* Estilos para la barra de búsqueda y el filtro */
.search-filter-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px;
    max-width: 800px;
    margin: 20px auto;
}

#searchBar {
    width: 60%;
    padding: 10px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

.filter-dropdown {
    position: relative;
    display: inline-block;
}

.filter-button {
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    font-size: 16px;
    border: none;
    cursor: pointer;
    border-radius: 4px;
}

.filter-button i {
    margin-right: 8px;
}

.dropdown-content {
    display: none;
    position: absolute;
    background-color: white;
    min-width: 200px;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    z-index: 1;
    padding: 10px;
    border-radius: 8px;
}

.dropdown-content label {
    display: block;
    padding: 8px 16px;
    cursor: pointer;
}

.dropdown-content label:hover {
    background-color: #f1f1f1;
}

.filter-dropdown:hover .dropdown-content {
    display: block;
}

/* Responsividad */
@media (max-width: 768px) {
    .search-filter-container {
        flex-direction: column;
        align-items: stretch;
    }

    #searchBar, .filter-button {
        width: 100%;
        margin-bottom: 10px;
    }

    .plant-container {
        flex-direction: column;
        align-items: center;
    }

    .plant-card {
        width: 100%;
    }
}

</style>
