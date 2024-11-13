<script setup>
import L from 'leaflet'
import 'leaflet/dist/leaflet.css'
import 'leaflet.awesome-markers/dist/leaflet.awesome-markers.css'
import 'leaflet.awesome-markers'
import '@fortawesome/fontawesome-free/css/all.css'
import { ref, onMounted } from 'vue'
import { toast } from 'vue3-toastify'

const map = ref(null)
const searchQuery = ref('')
const defaultLocation = [-2.13396, -79.59337] // Coordenadas de "Ciudad de Milagro"

// Lista de ubicaciones con coordenadas
const locations = {
  'Ciudad de Milagro': defaultLocation,
  'Vivero Milagro': [-2.1433364632021212, -79.57640597670138],
  'Plantilandia': [-2.1310410852055983, -79.91311289283892],
  'Vivero Jhonatan': [-2.1447483028039347, -79.57438558896074],
  'Jardín vivero El sol': [-2.137391052888829, -79.59651124533325]
}

// Inicializar el mapa y los marcadores
onMounted(() => {
  navigator.geolocation.getCurrentPosition(
    (position) => {
      const userLocation = [position.coords.latitude, position.coords.longitude]
      initializeMap(userLocation) // Usa la ubicación del usuario
      addUserMarker(userLocation) // Agrega un marcador en la ubicación del usuario

      // Acercamiento a la ubicación del usuario
      map.value.setView(userLocation, 16) // Ajusta el zoom (por ejemplo, 16 para un acercamiento)
    },
    () => {
      initializeMap(defaultLocation) // Usa la ubicación predeterminada si se deniega el permiso
    }
  )
})

// Función para inicializar el mapa
const initializeMap = (initialLocation) => {
  map.value = L.map('map', {
    center: initialLocation,
    zoom: 13,
    zoomControl: true
  })

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map.value)

  // Marcador de Ciudad de Milagro
  const milagroIcon = L.AwesomeMarkers.icon({
    icon: 'city',
    markerColor: 'blue',
    prefix: 'fa'
  })
  L.marker(defaultLocation, { icon: milagroIcon })
    .addTo(map.value)
    .bindPopup('<b>Ciudad de Milagro</b>')

  // Marcadores de viveros
  const viveroIcon = L.AwesomeMarkers.icon({
    icon: 'seedling',
    markerColor: 'green',
    prefix: 'fa'
  })
  L.marker([-2.1433364632021212, -79.57640597670138], { icon: viveroIcon })
    .addTo(map.value)
    .bindPopup('<b>Vivero Milagro</b>')
  L.marker([-2.1310410852055983, -79.91311289283892], { icon: viveroIcon })
    .addTo(map.value)
    .bindPopup('<b>Vivero Plantilandia</b>')
  L.marker([-2.1447483028039347, -79.57438558896074], { icon: viveroIcon })
    .addTo(map.value)
    .bindPopup('<b>Vivero Jhonatan</b>')
  L.marker([-2.137391052888829, -79.59651124533325], { icon: viveroIcon })
    .addTo(map.value)
    .bindPopup('<b>Jardín vivero "El sol"</b>')
}

// Función para agregar un marcador en la ubicación del usuario
const addUserMarker = (userLocation) => {
  const userIcon = L.AwesomeMarkers.icon({
    icon: 'location-arrow',
    markerColor: 'red',
    prefix: 'fa'
  })
  L.marker(userLocation, { icon: userIcon })
    .addTo(map.value)
    .bindPopup('<b>Tu ubicación actual</b>')
}
  
// Función de búsqueda que centra el mapa en la ubicación buscada
const searchLocation = () => {
  // Verificar si la consulta de búsqueda está vacía
  if (!searchQuery.value.trim()) {
    toast.error('Debe ingresar un nombre', {
      position: toast.POSITION.TOP_RIGHT,
      pauseOnHover: false
    })
    return // Detener la ejecución de la función si el campo está vacío
  }

  // Convertir la consulta a minúsculas para hacer la búsqueda case-insensitive
  const query = searchQuery.value.toLowerCase()
  
  // Buscar la primera ubicación que contenga la consulta de búsqueda
  const locationName = Object.keys(locations).find(name => name.toLowerCase().includes(query))

  if (locationName) {
    const coordinates = locations[locationName]
    map.value.setView(coordinates, 20) // Centra el mapa en la ubicación encontrada
    L.popup()
      .setLatLng(coordinates)
      .setContent(`Ubicación encontrada: ${locationName}`)
      .openOn(map.value)
  } else {
    toast.error('No se encontró la dirección que buscaba, pruebe otra', {
      position: toast.POSITION.TOP_RIGHT,
      pauseOnHover: false
    })
  }
}
</script>

<template>
  <main>
    <!-- Sección de búsqueda -->
    <div class="search-container">
      <input
        v-model="searchQuery"
        type="text"
        placeholder="Buscar viveros cercanos..."
        id="searchBox"
      />
      <button @click="searchLocation">Buscar</button>
      <p class="explore-message">¡Explora los viveros más cercanos!</p>
    </div>
    <div id="map"></div>
  </main>
</template>
<style scoped>
@import url('../assets/css/map.css');
</style>
