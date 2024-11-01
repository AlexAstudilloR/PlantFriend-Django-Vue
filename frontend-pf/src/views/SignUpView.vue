<script setup>
import { ref } from 'vue'
import { useUserStore } from '@/stores/userStore'
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faCloudArrowUp } from '@fortawesome/free-solid-svg-icons'
import { toast } from 'vue3-toastify';
// Agregar el ícono a la librería
library.add(faCloudArrowUp)

const userStore = useUserStore()

const username = ref('')
const nombre = ref('')
const email = ref('')
const telefono = ref('')
const password = ref('')
const imagen = ref(null)
const imagenName= ref('')

const handleRegister = async () => {
  const formData = new FormData();
  formData.append('nombre', nombre.value);
  formData.append('username', username.value);
  formData.append('email', email.value);
  formData.append('telefono', telefono.value);
  formData.append('password', password.value);
  formData.append('imagen', imagen.value); // Archivo de imagen
function notify(){
  toast.error('Ha ocurrido un error al crear el usuario',{
        position: toast.POSITION.BOTTOM_RIGHT,
      })
}
  try {
    await userStore.register(formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });
    toast.success('Usuario creado correctamente',{
      position: toast.POSITION.BOTTOM_RIGHT,
    })
  } catch (error) {
    
      notify()
    
  }
};

const triggerFileSelect = () => {
  document.getElementById('imagen').click()
}
const handleFileChange = (e) => {
  imagen.value = e.target.files[0];
  imagenName.value = imagen.value ? imagen.value.name : ''; // Guarda el nombre del archivo
};
</script>
<template>
  <div class="split-screen">
    <div class="left">
      <section class="copy">
        <h1>La naturaleza a tu alcance.</h1>
        <p>El jardín de tus sueños, en la palma de tu mano.</p>
      </section>
    </div>
    <div class="right">
      <form @submit.prevent="handleRegister">
        <section class="copy">
          <h2>Sign Up</h2>
          <div class="login-container">
            <p>¿Ya tienes cuenta? <router-link to="/login">Log In</router-link></p>
          </div>
          <div class="input-container image-upload">
            <label for="imagen">Foto de perfil</label>
            <input type="file" id="imagen" @change="handleFileChange" style="display: none" />
            <div class="img-content">
              <button type="button" class="image-button" @click="triggerFileSelect">
                <FontAwesomeIcon :icon="['fas', 'cloud-arrow-up']" />
              </button>
              <span v-if="imagenName" class="img-txt">{{ imagenName }}</span>
            </div>
          </div>
          <div class="input-container name">
            <label for="username">Nombre de usuario</label>
            <input type="text" id="username" placeholder="Ingrese su nombre de usuario" v-model="username" name="username" />
          </div>

          <div class="input-container name">
            <label for="telefono">Teléfono</label>
            <input type="tel" id="telefono" placeholder="Ingrese su número de teléfono" v-model="telefono" name="telefono" />
          </div>

          <div class="input-container name">
            <label for="nombre">Nombre completo</label>
            <input type="text" id="nombre" placeholder="Ingrese su nombre completo" v-model="nombre" name="nombre" />
          </div>

          <div class="input-container email">
            <label for="email">Email</label>
            <input type="email" id="email" placeholder="Ingrese su correo electrónico" v-model="email" name="email" />
          </div>

          <div class="input-container password">
            <label for="password">Password</label>
            <input id="password" v-model="password" placeholder="Ingrese su contraseña (mínimo 8 caracteres)" name="password" type="password" />
          </div>

          <button class="signup-btn" type="submit">Sign Up</button>
          <section class="copy legal">
            <p>
              <span class="small">
                Al continuar, aceptas nuestra <br />
                <a href="#">Política de Privacidad</a> &amp; <a href="#">Términos de Servicio</a>.
              </span>
            </p>
          </section>
        </section>
      </form>
    </div>
  </div>
</template>

<style scoped>
@import url('../assets/css/signUp.css');
</style>
