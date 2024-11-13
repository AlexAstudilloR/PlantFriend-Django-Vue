<script setup>
import { ref, computed } from 'vue'

import { useScanStore } from '../stores/scanStore'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faCloudArrowUp } from '@fortawesome/free-solid-svg-icons'
import { library } from '@fortawesome/fontawesome-svg-core'
import { storeToRefs } from 'pinia'
import ModalResults from '../components/ModalResults.vue'
import { toast } from 'vue3-toastify'
import { FulfillingSquareSpinner } from 'epic-spinners'
library.add(faCloudArrowUp)

const fileInput = ref(null)
const fileName = ref('')
const imagePreview = ref(null)
const selectedFile = ref(null) // Nueva referencia para almacenar el archivo seleccionado
const showModal = ref(false) // Nueva variable para controlar la visibilidad del modal

const scanStore = useScanStore()
const { scanResult, loading, error } = storeToRefs(scanStore)
const nombreCientifico = computed(() => scanResult.value?.nombre_cientifico || 'Desconocido')
const nombreComun = computed(() => scanResult.value?.nombre_comun || 'No disponible')
const probabilidad = computed(() => scanResult.value?.probabilidad || 'N/A')

const triggerFileInput = () => {
  fileInput.value.click()
}

const handleImageUpload = (event) => {
  const file = event.target.files[0]
  if (file) {
    fileName.value = file.name
    const reader = new FileReader()
    reader.onload = (e) => {
      imagePreview.value = e.target.result
    }
    reader.readAsDataURL(file)

    selectedFile.value = file // Asigna el archivo a `selectedFile`
    scanStore.clearScanResult()
  }
}

const submitImage = async () => {
  if (selectedFile.value) {
    await scanStore.scanImage(selectedFile.value) // Envia la imagen al store
    showModal.value = true // Mostrar el modal después de enviar la imagen
  } else {
    toast.error('No se ha seleccionado ninguna imagen', {
      position: toast.POSITION.TOP_RIGHT,
      pauseOnHover: false
    })
  }
}
</script>
<template>
  <div class="box">
    <h2 class="title">Cargar Imagen</h2>
    <input
      type="file"
      id="real-file"
      ref="fileInput"
      @change="handleImageUpload"
      accept="image/*"
      hidden
    />
    <div v-if="imagePreview" id="image-preview-container" class="box-preview">
      <img :src="imagePreview" alt="Vista previa de la imagen" id="image-preview" />
    </div>
    <button type="button" id="custom-button" @click="triggerFileInput">
      <font-awesome-icon :icon="['fas', 'cloud-arrow-up']" />
      <strong> CARGAR FOTO</strong>
    </button>
    <span id="custom-text">{{ fileName || 'No hay ninguna imagen' }}</span>
    <br />
    <button class="boton" @click="submitImage">Enviar</button>

    <div v-if="loading" class="spinner-overlay">
      <fulfilling-square-spinner :animation-duration="2000" :size="30" color="#4caf50" />
    </div>
    <div v-if="error" class="error">
      {{ error }}
    </div>
  </div>

  <!-- Modal de Resultados -->
  <ModalResults :show="showModal" @close="showModal = false">
  
  <div class="titleContainer">
    <h4 class="modal-title">Resultados del Escaneo</h4>
    <div v-if="imagePreview" id="image-preview-container" class="box-preview">
      <img :src="imagePreview" alt="Vista previa de la imagen" id="image-preview" />
    </div>

    <!-- Mostrar mensaje de error si la probabilidad es baja -->
    <div v-if="probabilidad < 0.05">
      <p style="color: red; font-weight: bold; text-align: center;">
        ¿Está seguro que subió imagen de una planta?. Intente nuevamente.
      </p>
    </div>

    <!-- Mostrar los datos solo si la probabilidad es suficiente -->
    <template v-else>
      <p style="font-weight: 500">{{ nombreCientifico }}</p>

      <div v-if="nombreCientifico === 'Desconocido' || nombreComun === 'No disponible'">
        <p style="color: red; font-weight: bold;">
          No se obtuvo una planta de forma precisa, intente nuevamente
        </p>
      </div>

      <h4>Descripción</h4>
      <p style="text-align: center">{{ nombreComun }}</p>
      <h4>Probabilidad</h4>
      <p>{{ probabilidad }}</p>
    </template>
  </div>
</ModalResults>
</template>

<style scoped>
.spinner-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgba(255, 255, 255, 0.8);
  z-index: 1000;
}

.titleContainer {
  text-align: center;
  width: 100%;
}
.sciName {
  font-weight: 600;
}
/* Sección principal */
.scanner-section {
  text-align: center;
  padding: 50px;
  background-color: #ffffff;
}
.modal-title{
  color: #4caf50;
  text-align: center;
}
.scanner-section h1 {
  color: #4caf50;
  font-family: 'Poppins', sans-serif;
}

.scanner-section p {
  color: #000000;
  font-family: 'Poppins', sans-serif;
}

/* Botón principal */
#scan-button {
  background-color: #4caf50;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  border: none;
  transition: background-color 0.3s ease;
  font-family: 'Poppins', sans-serif;
}

/* Estilo para los botones de la página */
.boton {
  margin-top: 20px;
  width: 90px;
  height: 35px;
  border-radius: 3px;
  background-color: #4caf50;
  font-family: 'Poppins', sans-serif;
  cursor: pointer;
  border: none;
  color: white;
  border-radius: 10px;
  align-content: center;
}

.boton:hover {
  color: #ffffff;
  background-color: #157436;
}

/* Estilos de la caja principal */
.box {
  background-color: rgb(235, 255, 227);
  padding: 25px;
  text-align: center;
  width: 50%;
  max-width: 400px;
  box-sizing: border-box;
  box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
  margin: 50px auto; /* Centramos la caja */
  border-radius: 15px;
}

/* Título */
.title {
  margin-bottom: 20px;
  font-weight: 600;
  font-family: 'Poppins', sans-serif;
  color: #3a3a3a;
}

/* Botón de carga personalizada */
#custom-button {
  padding: 10px;
  color: white;
  background-color: #21863a;
  border-radius: 5px;
  cursor: pointer;
  border: 0;
}

#custom-button:hover {
  background-color: #117725;
}

/* Texto cuando no hay archivo seleccionado */
#custom-text {
  margin-left: 10px;
  font-family: sans-serif;
  color: #aaa;
}

/* Previsualización de imagen */
#image-preview {
  height: 200px;
  width: 200px;
  margin-bottom: 10px;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 4px 12px;
  border-radius: 10px;
}

/* Responsive Design */
/* Ajustes para pantallas pequeñas */
@media (max-width: 768px) {
  .box {
    width: 80%; /* Caja más ancha en móviles */
    max-width: none; /* Sin límite en el ancho */
    margin-top: 30px;
    padding: 20px;
  }

  #image-preview {
    width: 150px;
    height: auto;
  }

  .boton {
    width: 100%; /* Botón más ancho en móviles */
  }
}

/* Ajustes para pantallas muy pequeñas (por debajo de 480px) */
@media (max-width: 480px) {
  .box {
    width: 90%;
    padding: 15px;
  }

  #image-preview {
    width: 120px;
    height: auto;
  }

  #custom-button {
    width: 100%; /* Botón de cargar foto ocupa todo el ancho */
    padding: 12px;
  }

  .boton {
    width: 100%; /* Botón enviar ocupa todo el ancho */
  }
}
</style>
