<template>
    <div class="plant-card" :data-category="plant.category">
      <img :src="plantImage" :alt="plant.nombre" />
      <h3>{{ plant.nombre }}</h3>
      <p>Categoría: {{ plant.categoria }}</p>
      <button class="boton-guia" @click="viewGuide(plant.guideId)">Ver Guía</button>
      <button @click="addToGarden">
        <font-awesome-icon :icon="['fas', 'circle-plus']" />
      </button>
    </div>
  </template>
  
  <script setup>
  import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
  import { faCirclePlus } from '@fortawesome/free-solid-svg-icons';
  import { library } from '@fortawesome/fontawesome-svg-core';
  import { computed, defineProps, defineEmits } from 'vue';
  
  // Añadir el icono a la librería de FontAwesome localmente en este componente
  library.add(faCirclePlus);
  
  // Definir propiedades y eventos
  const props = defineProps({
    plant: {
      type: Object,
      required: true,
    },
  });
  
  const emit = defineEmits(['view-guide', 'add-to-garden']);
  
  // Computed para la imagen de la planta
// Cambia esto a la URL de tu backend en producción

const plantImage = computed(() => {
  // Si la imagen es una ruta relativa, construye la URL completa
  return props.plant.imagen ? props.plant.imagen : console.log("Hola");
});
  
  // Métodos para los eventos
  const viewGuide = (guideId) => {
    emit("view-guide", guideId);
  };
  
  const addToGarden = () => {
    emit("add-to-garden", props.plant.id);
  };
  </script>
  
  <style scoped>
  /* Estilos generales */
body {
    font-family: 'Poppins', sans-serif;
    margin: 0;
    padding: 0;
    
}

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
  