<template>
  <div v-if="isVisible" class="modal-overlay" @click="closeModal">
    <div class="modal-container" @click.stop>
      <h2 class="modal-title">{{ title }}</h2>
      <slot></slot>
      <button class="close-button" @click="closeModal">Cerrar</button>
    </div>
  </div>
</template>

<script setup>
import { ref, defineProps, defineEmits, watch } from 'vue';
const isVisible = ref(false);

const props = defineProps({
  title: {
    type: String,
    default: 'Modal Title',
  },
  show: Boolean,
});

const emit = defineEmits(['close']);

watch(
  () => props.show,
  (newValue) => {
    isVisible.value = newValue;
  }
);

const closeModal = () => {
  isVisible.value = false;
  emit('close');
};
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.7); /* Fondo oscuro */
  display: flex;
  justify-content: center; /* Centrado horizontal */
  align-items: center; /* Centrado vertical */
  z-index: 1000;
}

.modal-container {
  background: white;
  padding: 20px;
  border-radius: 8px;
  max-width: 90%;
  width: 500px;
  height: 700px; /* Ancho fijo */
  text-align: center;
}

.modal-title {
  font-size: 1.5em;
  font-weight: bold;
  margin: 0 0 20px;
  color: #21863a;
}

.close-button {
  margin-top: 20px;
  background-color: #21863a;
  color: white;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
  border-radius: 5px;
}

.close-button:hover {
  background-color: #17622b;
}
</style>
