import { defineStore } from 'pinia';
import { ref } from 'vue';
import { scanPlantImage } from '../services/axios.scan';

export const useScanStore = defineStore('scan', () => {
  const scanResult = ref(null);
  const loading = ref(false);
  const error = ref(null);

  const scanImage = async (imageFile) => {
    loading.value = true;
    error.value = null;
    try {
      const response = await scanPlantImage(imageFile);
      scanResult.value = response.data;
    } catch (err) {
      error.value = err.response?.data?.error || 'Error al escanear la imagen';
      console.error('Error al escanear la imagen:', error.value);
    } finally {
      loading.value = false;
    }
  };

  const clearScanResult = () => {
    scanResult.value = null;
    error.value = null;
  };

  return { scanResult, loading, error, scanImage, clearScanResult };
});
