<template>
  <div>
    <h1>Mi Jardín</h1>

    <div v-if="loading">Cargando...</div>

    <div v-else-if="garden && garden.length === 0">
      <p>No tienes plantas en tu jardín.</p>
    </div>

    <div v-else class="plant-container">
      <div v-for="plant in garden" :key="plant.id" class="plant-card" :data-category="plant.categoria">
        <img :src="plant.imagen || 'ruta/default-image.png'" :alt="plant.nombre" />
        <h3>{{ plant.nombre }}</h3>
        <p>Categoría: {{ plant.categoria }}</p>
        <button class="boton-guia" @click="viewGuide(plant.guideId)">Ver Guía</button>
        <button @click="removeFromGarden(plant.id)">
          <font-awesome-icon class="plus" :icon="['fas', 'circle-minus']" />
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { faCircleMinus } from '@fortawesome/free-solid-svg-icons';
import { library } from '@fortawesome/fontawesome-svg-core';
import { onMounted } from 'vue';
import { useGardenStore } from '@/stores/gardenStore';

// Añadir el icono a la librería de FontAwesome
library.add(faCircleMinus);

const gardenStore = useGardenStore();
const { garden, loading, getGarden, removePlant } = gardenStore;

// Métodos de la vista
const viewGuide = (guideId) => {
  console.log(`Ver guía con ID: ${guideId}`);
};

const removeFromGarden = async (plantId) => {
  await removePlant(plantId);
  console.log(`Planta con ID: ${plantId} eliminada del jardín`);
};

// Cargar el jardín cuando se monta el componente
onMounted(() => {
  getGarden();
});
</script>

<style scoped>
.plant-container {
  display: flex;
  flex-wrap: wrap;
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
  font-size: 16px;
  border-radius: 4px;
  cursor: pointer;
  margin-left: 10px;
  margin-right: 10px;
}

.boton-guia {
  margin-bottom: 5px;
}
</style>
