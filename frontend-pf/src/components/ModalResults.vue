<!-- src/components/Modal.vue -->
<template>
    <div class="modal-overlay" @click="closeModal">
      <div class="modal-content" @click.stop>
        
        <h2 class="titulo">{{ title }}</h2>
        <slot></slot>
      </div>
    </div>
  </template>
  
  <script setup>
  import { defineProps, defineEmits } from 'vue';
  
  defineProps({
    title: {
      type: String,
      default: 'Modal Title'
    }
  });
  
  const emit = defineEmits(['close']);
  
  const closeModal = () => {
    emit('close');
  };
  </script>
  
  <style scoped>
  .modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5); /* Fondo oscuro */
  display: flex;
  justify-content: center; /* Centrado horizontal */
  align-items: center; /* Centrado vertical */
  z-index: 1000; /* Asegura que esté en la capa superior */
}
.titulo{
    width: 100%;
    text-align: center;
    background-color: #21863a;
    color: rgb(255, 255, 255);
    border-radius: 5px 5px 0 0;
}
.modal-content {
  background: white;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  align-items: center;
  width: 600px;
  height: 700px;
  max-width: 80%;
  border-radius: 5px;


}

.close-button {
  position: absolute;
  top: 10px;
  right: 10px;
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
}
  </style>
  