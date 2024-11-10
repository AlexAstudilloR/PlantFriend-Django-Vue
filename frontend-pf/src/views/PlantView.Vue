<script setup>
import PlantsCards from '../components/plants/PlantsCards.vue';
import { usePlantsStore } from '../stores/PlantsStore';
import { useGardenStore } from '../stores/gardenStore';
import { computed, onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { faFilter } from '@fortawesome/free-solid-svg-icons';
import { SelfBuildingSquareSpinner } from 'epic-spinners';

library.add(faFilter);

const plantsStore = usePlantsStore();
const gardenStore = useGardenStore();
const router = useRouter();
const isLoading = ref(true); // Estado para controlar la visualización del spinner
const searchQuery = ref('');
const selectedCategory = ref('');
const isDropdownOpen = ref(false);

onMounted(async () => {
  isLoading.value = true;
  await plantsStore.fetchPlants();
  await plantsStore.fetchCategories();
  isLoading.value = false; // Ocultar el spinner después de cargar
});

const toggleDropdown = () => {
  isDropdownOpen.value = !isDropdownOpen.value;
};

const selectCategory = async (category) => {
  selectedCategory.value = category;
  isDropdownOpen.value = false;
  await filterByCategory();
};

const searchPlants = async () => {
  if (searchQuery.value) {
    await plantsStore.searchPlantsByName(searchQuery.value);
  } else {
    await plantsStore.fetchPlants();
  }
};

const filterByCategory = async () => {
  if (selectedCategory.value) {
    await plantsStore.filterPlantsByCategory(selectedCategory.value);
  } else {
    await plantsStore.fetchPlants();
  }
};

const viewGuide = (guideId) => {
  if (guideId) {
    router.push({ name: 'guide', params: { id: guideId } });
  } else {
    console.error('La guía no está disponible para esta planta.');
  }
};

const addToGarden = async (plantId) => {
  try {
    await gardenStore.addPlant(plantId);
  } catch (error) {
    console.error('Error al añadir la planta al jardín:', error);
  }
};

const plants = computed(() => plantsStore.plants);
const categories = computed(() => plantsStore.categories);
</script>

<template>
  <div>
    <div class="search-filter-container">
      <input
        type="text"
        id="searchBar"
        placeholder="Buscar por nombre de planta..."
        v-model="searchQuery"
        @input="searchPlants"
      />
      <div class="filter-dropdown">
        <button class="filter-button" @click="toggleDropdown">
          Filtrar <font-awesome-icon class="icon" :icon="['fas', 'filter']" />
        </button>
        <div v-if="isDropdownOpen" class="dropdown-content">
          <span class="label" @click="selectCategory('')">Todas las Categorías</span>
          <span
            v-for="category in categories"
            :key="category.id"
            class="label"
            @click="selectCategory(category.name)"
          >
            {{ category.name }}
          </span>
        </div>
      </div>
    </div>

    <!-- Spinner de carga -->
    <div v-if="isLoading" class="spinner-container">
      <self-building-square-spinner :animation-duration="3000" :size="40" color="#4CAF50" />
    </div>

    <!-- Lista de Plantas -->
    <div v-else class="plant-container">
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
  </div>
</template>
<style scoped>
.spinner-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
a{
    text-decoration: none;
    color: white;
}

.plant-card {
    border: 1px solid #fffdfd;
    border-radius: 8px;
    box-shadow: rgba(50, 50, 93, 0.25) 0px 6px 12px -2px, rgba(0, 0, 0, 0.3) 0px 3px 7px -3px;
    margin: 10px;
    padding: 20px;
    text-align: center;
    padding-top: 10px;
}
.plants-list{
  display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    padding: 20px;
    position: relative;
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
button:hover{
  background-color: #459b48 ;
 
  
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

.filter-button .icono {
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

.dropdown-content .label {
    display: block;
    padding: 8px 16px;
    cursor: pointer;
}

.dropdown-content .label:hover {
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
