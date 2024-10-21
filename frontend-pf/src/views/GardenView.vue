<template>
    <div>
      <h1>Mi Jardín</h1>
      <ul>
        <li v-for="plant in gardenStore.garden" :key="plant.id">
          {{ plant.nombre }}
          <button @click="removePlant(plant.id)">Eliminar</button>
        </li>
      </ul>
  
      <form @submit.prevent="addPlant">
        <input v-model="newPlantId" placeholder="ID de la planta" />
        <button type="submit">Agregar Planta</button>
      </form>
    </div>
  </template>
  
  <script>
  import { useGardenStore } from '@/stores/gardenStore';
  import { ref, onMounted } from 'vue';
  
  export default {
    setup() {
      const gardenStore = useGardenStore();
      const newPlantId = ref('');
  
      onMounted(() => {
        gardenStore.fetchUserGarden();
      });
  
      const addPlant = () => {
  gardenStore.addPlant(newPlantId.value);  // Pasar directamente el ID de la planta
  newPlantId.value = '';  // Limpiar el campo después de agregar
};
  
      const removePlant = (plantaId) => {
        gardenStore.removePlant(plantaId);
      };
  
      return {
        gardenStore,
        newPlantId,
        addPlant,
        removePlant,
      };
    },
  };
  </script>
  