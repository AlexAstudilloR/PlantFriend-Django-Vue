<template>
  <main>
    <!-- Search section -->
    <div class="search-container">
      <input v-model= "searchQuery" type="text" placeholder="Buscar viveros cercanos..." id="searchBox" />
      <button @click="searchLocation">Buscar</button>
      <p class="explore-message">¡Explora los viveros más cercanos!</p>
    </div>
    <div id="map"></div>
  </main>
</template>

<script setup>
// Importa Leaflet
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import 'leaflet.awesome-markers/dist/leaflet.awesome-markers.css';
import 'leaflet.awesome-markers';
import '@fortawesome/fontawesome-free/css/all.css';
import { ref, onMounted } from 'vue';
import {toast} from 'vue3-toastify'
// Variables y datos de búsqueda
const map = ref(null);
const searchQuery = ref('');

// Lista de ubicaciones con coordenadas
const locations = {
  'Ciudad de Milagro': [-2.13396, -79.59337],
  'Vivero Milagro': [-2.1433364632021212, -79.57640597670138],
  'Vivero Plantilandia':[-2.1310410852055983, -79.91311289283892]
  // Agrega más ubicaciones aquí
};

// Inicializar el mapa y los marcadores
onMounted(() => {
  map.value = L.map('map', {
    center: [-2.13396, -79.59337],
    zoom: 13,
    zoomControl: true,
  });

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution:
      '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  }).addTo(map.value);

  // Icono de la ciudad de Milagro
  const milagroIcon = L.AwesomeMarkers.icon({
    icon: 'city',
    markerColor: 'blue',
    prefix: 'fa',
  });
  L.marker([-2.13396, -79.59337], { icon: milagroIcon }).addTo(map.value)
    .bindPopup('<b>Ciudad de Milagro</b>');

  // Icono para el vivero
  const viveroIcon = L.AwesomeMarkers.icon({
    icon: 'seedling',
    markerColor: 'green',
    prefix: 'fa',
  });
  L.marker([-2.1433364632021212, -79.57640597670138], { icon: viveroIcon }).addTo(map.value)
    .bindPopup('<b>Vivero Milagro</b>');
    const viveroPlantilandia = L.AwesomeMarkers.icon({
    icon: 'seedling',
    markerColor: 'green',
    prefix: 'fa',
  });
  L.marker([-2.1310410852055983, -79.91311289283892], { icon: viveroPlantilandia }).addTo(map.value)
    .bindPopup('<b>Vivero Plantilandia</b>');
});

// Función de búsqueda que centra el mapa en la ubicación buscada
const searchLocation = () => {
  const coordinates = locations[searchQuery.value];
  if (coordinates) {
    map.value.setView(coordinates, 20); // Centra el mapa en la ubicación encontrada
    L.popup()
      .setLatLng(coordinates)
      .setContent(`Ubicación encontrada: ${searchQuery.value}`)
      .openOn(map.value);
  } else {
    toast.error('No se encontró la dirección que buscaba, pruebe otra',{
      position: toast.POSITION.TOP_RIGHT,
      pauseOnHover: false
    })
  }
};
</script>

<style scoped>
/* Contenedor del mapa y título */
@import url('../assets/css/map.css');
/* Botones de zoom personalizados */
</style>
