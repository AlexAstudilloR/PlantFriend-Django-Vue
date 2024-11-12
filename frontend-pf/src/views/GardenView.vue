<template>
  <div>
    <h1 style="text-align: center;">Mi Jardín</h1>

    <!-- Muestra el mensaje de carga si está cargando -->
    <div v-if="loading" class="spinner-container">
      <self-building-square-spinner :animation-duration="3000" :size="40" color="#4CAF50" />
    </div>

    <!-- Verifica que `garden` esté definido y no esté vacío, y que tenga al menos una planta -->
    <div class="NoPlants" v-else-if="!garden || garden.length === 0 || !garden[0]?.plants?.length">
      <p style="text-align: center;">No has añadido plantas</p>
      <img src="../assets/imgs/NoPlantsAdded.jpg" alt="no plantas añadidas">
    </div>

    <!-- Muestra las plantas en el jardín si hay datos -->
    <div v-else class="plant-container">
      <div 
        v-for="plant in garden[0].plants" 
        :key="plant.id" 
        class="plant-card" 
        :data-category="plant.categoria"
      >
        <img :src="plant.imagen || 'ruta/default-image.png'" :alt="plant.nombre" />
        <h3>{{ plant.nombre }}</h3>
        <button class="boton-guia" @click="viewGuide(plant.guia)">Ver Guía</button>
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
import { onMounted, computed, watch } from 'vue';
import { SelfBuildingSquareSpinner } from 'epic-spinners';
import { useGardenStore } from '@/stores/gardenStore';
import {toast} from 'vue3-toastify'
import { useRouter } from 'vue-router';
library.add(faCircleMinus);

const gardenStore = useGardenStore();
const loading = computed(() => gardenStore.loading);
const garden = computed(() => gardenStore.garden);
const router = useRouter()
const viewGuide = (guideId) => {
  if (guideId) {
    router.push({ name: 'guide', params: { id: guideId } });
  } else {
    console.error('La guía no está disponible para esta planta.');
  }
};

const removeFromGarden = async (plantId) => {
  await gardenStore.removePlant(plantId);
  toast.success("Has eliminado correctamente la planta del jardín",{
    position: toast.POSITION.TOP_RIGHT,
    pauseOnHover: false
  })
};

onMounted(() => {
  gardenStore.getGarden();
});
watch(garden, (newGarden) => {
  console.log("Nuevos datos en garden:", newGarden);
});
</script>

<style scoped>
.spinner-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
.NoPlants{
  display: flex;
  flex-direction: column;
  align-items: center;
}
.NoPlants p{
  font-size: 26px;
}
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
  background-color: #4caf50;
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
