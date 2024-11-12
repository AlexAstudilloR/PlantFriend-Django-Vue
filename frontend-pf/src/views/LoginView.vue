<template>
  <div class="split-screen">
    <div class="left">
      <section class="copy">
        <h1>La naturaleza a tu alcance.</h1>
        <p>El jardín de tus sueños, en la palma de tu mano.</p>
      </section>
    </div>
    <div class="right">
      <form @submit.prevent="handleLogin">
        <section class="copy">
          <h2>Login</h2>
          <div class="login-container">
            <p>¿No tienes cuenta? <router-link to="/register">Sign Up</router-link></p>
          </div>
          <div class="input-container name">
            <label for="username">Username</label>
            <input
              type="text"
              placeholder="Ingresa tu nombre de usuario"
              id="username"
              v-model="username"
              name="username"
            />
          </div>

          <div class="input-container password">
            <label for="password">Password</label>
            <div class="password-field">
              <input
                :type="passwordFieldType"
                id="password"
                v-model="password"
                placeholder="Debe de tener al menos 8 caracteres"
              />
            </div>
          </div>

          <button class="signup-btn" type="submit">Login</button>
          <section class="copy legal">
            <p>
              <span class="small"
                >By continuing, you agree to accept our <br />
                <a href="#">Privacy Policy</a> &amp; <a href="#">Terms of Service</a>.
              </span>
            </p>
          </section>
        </section>
      </form>
    </div>
  </div>
</template>

<script setup>
import { computed, ref } from 'vue';
import { useUserStore } from '@/stores/userStore';
import { useRouter } from 'vue-router';
import { toast } from 'vue3-toastify';

const userStore = useUserStore();
const username = ref('');
const password = ref('');
const hidePassword = ref(true);

const router = useRouter();

const passwordFieldType = computed(() => (hidePassword.value ? 'password' : 'text'));

const handleLogin = async () => {
  try {
    await userStore.login({ username: username.value, password: password.value });
    router.push('/home'); // Redirige solo después de un inicio de sesión exitoso
  } catch (error) {
    toast.error('Ha ocurrido un error, verifica tus credenciales', {
      position: toast.POSITION.TOP_RIGHT,
      pauseOnHover: false
    });
  }
};
</script>



<style scoped>
@import "../assets/css/shared-styles.css";
</style>
