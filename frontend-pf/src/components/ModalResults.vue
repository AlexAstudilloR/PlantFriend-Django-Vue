<!-- src/components/CustomModal.vue -->
<template>
  <VueFinalModal
    v-model="isVisible"
    :classes="modalClasses"
    :width="500"
    :height="300"
    :padding="0"
    @click-overlay="closeModal"
  >
    <div class="modal-content">
      <h2 class="modal-title">{{ title }}</h2>
      <slot></slot>
      <button class="close-button" @click="closeModal">Cerrar</button>
    </div>
  </VueFinalModal>
</template>

<script setup>
import { ref, defineProps, defineEmits } from 'vue';


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

const modalClasses = {
  overlay: 'custom-overlay',
  content: 'custom-content',
};
</script>

<style scoped>
.custom-overlay {
  background: rgba(0, 0, 0, 0.7);
}

.custom-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  border-radius: 8px;
}

.modal-content {
  padding: 20px;
  text-align: center;
  background: white;
  border-radius: 8px;
  width: 100%;
}

.modal-title {
  font-size: 1.5em;
  font-weight: bold;
  margin: 0;
  background-color: #21863a;
  color: white;
  padding: 15px;
  border-radius: 8px 8px 0 0;
  width: 100%;
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