<template>
    <div class="box">
      <h2 class="title">Cargar Imagen</h2>
      <form @submit.prevent="handleSubmit" enctype="multipart/form-data">
        <!-- Input de carga de imagen oculto -->
        <input 
          type="file" 
          id="real-file" 
          ref="fileInput" 
          @change="handleImageUpload" 
          accept="image/*" 
          hidden 
        />
        <!-- Botón personalizado para cargar imagen -->
        <button type="button" id="custom-button" @click="triggerFileInput">
          <font-awesome-icon :icon="['fas', 'cloud-arrow-up']" />
          <strong> CARGAR FOTO</strong>
        </button>
        <span id="custom-text">{{ fileName || 'No file chosen, yet.' }}</span>
        <br>
        <!-- Contenedor de previsualización de imagen -->
        <div v-if="imagePreview" id="image-preview-container" class="box-preview">
          <img :src="imagePreview" alt="Vista previa de la imagen" id="image-preview" />
        </div>
        <button class="boton" type="submit">Enviar</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { library } from '@fortawesome/fontawesome-svg-core';
  import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
  import { faCloudArrowUp } from '@fortawesome/free-solid-svg-icons';
  
  // Agregar el ícono a la librería
  library.add(faCloudArrowUp);
  
  // Variables reactivas para el archivo y su previsualización
  const fileInput = ref(null); // Referencia al input de archivo
  const fileName = ref(''); // Nombre del archivo
  const imagePreview = ref(null); // Fuente de la imagen para previsualización
  
  // Función para activar el input de archivo
  const triggerFileInput = () => {
    fileInput.value.click();
  };
  
  // Función para manejar la carga de imagen
  const handleImageUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
      fileName.value = file.name; // Asigna el nombre del archivo
      const reader = new FileReader();
      reader.onload = (e) => {
        imagePreview.value = e.target.result; // Asigna la URL de previsualización
      };
      reader.readAsDataURL(file);
    }
  };
  
  // Función para manejar el envío del formulario
  const handleSubmit = () => {
    // Aquí puedes procesar el archivo o enviar la imagen a tu API
    console.log("Imagen enviada:", fileName.value);
  };
  </script>
<style scoped>
/* Estilo general del cuerpo */


/* Sección principal */
.scanner-section {
    text-align: center;
    padding: 50px;
    background-color: #ffffff;
}

.scanner-section h1 {
    color: #4CAF50;
    font-family: 'Poppins', sans-serif;
}

.scanner-section p {
    color: #000000;
    font-family: 'Poppins', sans-serif;
}

/* Botón principal */
#scan-button {
    background-color: #4CAF50;
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
    background-color: #23bd2b;
    font-family: 'Poppins', sans-serif;
    cursor: pointer;
    border: none;
    color: white;
    
   
}

.boton:hover {
    color: #ffffff;
    background-color: #1b9b48;
}

/* Estilos de la caja principal */
.box {
    background-color: rgb(238, 238, 238);
    padding: 25px;
    text-align: center;
    width: 50%;
    max-width: 400px;
    box-sizing: border-box;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    margin: 50px auto; /* Centramos la caja */
    border-radius: 20px;
}

/* Título */
.title {
    margin-bottom: 20px;
}

/* Botón de carga personalizada */
#custom-button {
    padding: 10px;
    color: white;
    background-color: #007400;
    border: 1px solid #000;
    border-radius: 5px;
    cursor: pointer;
}

#custom-button:hover {
    background-color: #025913;
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
    width: 175px;
    margin-top: 10px;
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