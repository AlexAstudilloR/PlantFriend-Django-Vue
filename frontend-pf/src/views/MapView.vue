<template>
  <div class="map-container">
    <!-- Título -->
    <div class="map-title">
      <h1>¡Explorar viveros cercanos!</h1>
    </div>

    <!-- Mapa Leaflet -->
    <div id="map" class="leaflet-map"></div>
  </div>
</template>

<script setup>
// Importa Leaflet
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import 'leaflet-defaulticon-compatibility';
import 'leaflet-defaulticon-compatibility/dist/leaflet-defaulticon-compatibility.css';

// Inicializar el mapa después de que el componente se monte
import { onMounted } from 'vue';

onMounted(() => {
  const map = L.map('map').setView([-2.13396, -79.59337], 13);

  // Añadir la capa de mapa (OpenStreetMap en este caso)
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  }).addTo(map);
  const marker= L.marker([-2.13396, -79.59337]).addTo(map)
  marker.bindPopup("<b>Ciudad de Milagro</b>").openPopup();
  const vivero =L.marker([-2.1433364632021212, -79.57640597670138]).addTo(map)
  vivero.bindPopup("<b>Vivero</b>").openPopup();
  
});
</script>

<style scoped>
/* Contenedor del mapa y título */
.map-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100vh;
  box-sizing: border-box;
}

.map-title {
  text-align: center;
  margin-bottom: 20px;
}

.leaflet-map {
  width: 100%;
  height: 60vh; /* Ajusta el tamaño del mapa según sea necesario */
}

@media (min-width: 768px) {
  .map-container {
    flex-direction: row;
  }

  .map-title {
    width: 50%;
    padding-right: 20px;
  }

  .leaflet-map {
    width: 50%;
    height: 80vh;
  }
}
</style>
