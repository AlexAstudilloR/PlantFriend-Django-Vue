<template>
  <div class="login-container">
    <div class="login-card">
      <h2>Iniciar sesión</h2>
      <form @submit.prevent="handleLogin">
        <div class="input-group">
          <label for="username">Nombre de usuario</label>
          <input type="text" id="username" v-model="username" required />
        </div>
        <div class="input-group">
          <label for="password">Contraseña</label>
          <div class="password-wrapper">
            <input :type="passwordFieldType" id="password" v-model="password" required />
            <i :class="['fa', passwordFieldIcon]" @click="togglePasswordVisibility"></i>
          </div>
        </div>
        <button type="submit" class="login-button">Iniciar sesión</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { computed, ref } from "vue";
import { useUserStore } from '@/stores/userStore';

const userStore = useUserStore();
const username = ref('');
const password = ref('');
const hidePassword = ref(true);

const passwordFieldIcon = computed(() => hidePassword.value ? "fa-eye" : "fa-eye-slash");
const passwordFieldType = computed(() => hidePassword.value ? "password" : "text");

const togglePasswordVisibility = () => {
  hidePassword.value = !hidePassword.value;
};

const handleLogin = async () => {
  try {
    await userStore.login({ username: username.value, password: password.value });
    alert('Inicio de sesión exitoso');
    // Aquí puedes añadir redirección después del inicio de sesión
  } catch (error) {
    alert('Error en el inicio de sesión. Verifica tus credenciales.');
  }
};
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100%;
  
  padding: 20px;
}

.login-card {
  background-color: #ffffff;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  width: 100%;
  max-width: 400px;
  text-align: center;
}

.login-card h2 {
  margin-bottom: 1.5rem;
  color: #2e7d32;
}

.input-group {
  margin-bottom: 1.5rem;
  text-align: left;
}

.input-group label {
  color: #2e7d32;
  font-weight: bold;
  margin-bottom: 0.5rem;
  display: block;
}

.input-group input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 1rem;
}

.password-wrapper {
  position: relative;
}

.password-wrapper input {
  width: calc(100% - 30px);
  padding-right: 30px;
}

.password-wrapper i {
  position: absolute;
  top: 50%;
  right: 10px;
  transform: translateY(-50%);
  cursor: pointer;
  color: #2e7d32;
}

.login-button {
  width: 100%;
  padding: 0.75rem;
  background-color: #388e3c;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
}

.login-button:hover {
  background-color: #2e7d32;
}
</style>