<template>
  <div v-if="!loading && guide">
    <h1 class="title">{{guide.titulo}}</h1>
    <div class="container">
      <div class="grid">
        <!-- Mostrar la imagen de la planta si existe -->
        <div class="element img-container" v-if="plant && plant.imagen">
          <img :src="plant.imagen" :alt="plant.nombre" />
        </div>
        <!-- Descripción de la guía -->
        <div class="element box">
          <p>{{ guide.descripcion }}</p>
        </div>
      </div>
    </div>
    <div class="button-container">
      <button class="button" @click="goBack">Volver</button>
    </div>
  </div>
  <div v-else-if="loading">
    Cargando...
  </div>
  <div v-else>
    No se encontró la guía.
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useGuideStore } from '../stores/guideStore';
import { usePlantsStore } from '../stores/plantsStore';

const guideStore = useGuideStore();
const plantsStore = usePlantsStore();
const route = useRoute();
const router = useRouter();

const loading = ref(true);
const guide = ref(null);
const plant = ref(null);

const fetchGuideAndPlantData = async () => {
  const guideId = route.params.id;
  loading.value = true;

  // Obtener la guía desde el store de guías
  await guideStore.fetchGuideById(guideId);
  guide.value = guideStore.guide; // Confirma si esta línea asigna bien la guía

  // Agrega un console.log adicional para ver el resultado
  console.log("Guide data (after fetch):", guideStore.guide);
  console.log("Guide local reference:", guide.value);

  // Obtener la planta asociada usando el guideId
  await plantsStore.fetchPlantByGuideId(guideId);
  plant.value = plantsStore.plant;

  loading.value = false;
};

onMounted(fetchGuideAndPlantData);

const goBack = () => {
  router.back();
};
</script>

<style scoped>
.title {
  text-align: center;
  margin-top: 50px;
  font-weight: 500;
  color: #2e7d32;
  font-family: 'Poppins';
}

.container {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  padding: 20px;
}

.grid {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: flex-start;
  width: 100%;
  max-width: 1200px;
}

.box {
  background-color: #f2f2f2;
  padding: 15px;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  margin: 20px;
  max-width: 600px;
  flex: 1;
}

.img-container {
  margin: 20px;
  flex: 0 0 150px;
  display: flex;
  justify-content: flex-start;
}

img {
  width: 300px;
  height: 300px;
  border-radius: 10px;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 0px 5px 0px, rgba(0, 0, 0, 0.1) 0px 0px 1px 0px;
}

.button-container {
  text-align: center;
  margin-top: 30px;
  margin-bottom: 20px;
}

.button {
  width: 100px;
  height: 40px;
  border-radius: 5px;
  background-color: #105213;
  font-family: 'Poppins', sans-serif;
  border: none;
  cursor: pointer;
  color: #ffffff;
  text-decoration: none;
  display: inline-block;
}

.button:hover {
  background-color: #0a401d;
}

@media (max-width: 768px) {
  .grid {
    flex-direction: column;
    align-items: center;
  }
  
  .img-container, .box {
    margin: 10px 0;
  }

  img {
    width: 120px;
  }
}
</style>
