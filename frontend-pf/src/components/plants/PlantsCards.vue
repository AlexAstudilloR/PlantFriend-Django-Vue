<script setup>
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { faCirclePlus } from '@fortawesome/free-solid-svg-icons';
import { library } from '@fortawesome/fontawesome-svg-core';
import { computed, defineProps, defineEmits } from 'vue';

library.add(faCirclePlus);

const props = defineProps({
  plant: {
    type: Object,
    required: true,
  },
});

const emit = defineEmits(['view-guide', 'add-to-garden']);

const plantImage = computed(() => {
  return props.plant.imagen || '/path/to/default-image.jpg';
});

const viewGuide = () => {
  const guideId = props.plant.guia;  // Asegúrate de que props.plant tenga el campo guia
  console.log(guideId);  // Esto ayudará a verificar si el guideId es correcto
  if (guideId) {
    emit("view-guide", guideId);
  } else {
    console.error('La guía no está disponible para esta planta.');
  }
};

const addToGarden = () => {
  emit("add-to-garden", props.plant.id);
};
</script>


<template>
    <div class="plant-card" :data-category="plant.category">
      <img :src="plantImage" :alt="plant.nombre" />
      <h3>{{ plant.nombre }}</h3>
      <p>Categoría: {{ plant.categoria }}</p>
      <button class="boton-guia" @click="viewGuide(plant.guideId)">Ver más</button>
      <button @click="addToGarden">
        <font-awesome-icon class="plus" :icon="['fas', 'circle-plus']" />
      </button>
    </div>
  </template>
  
  
  
  <style scoped>



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
    margin-left: 10px;
    margin-right: 10px;
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
  