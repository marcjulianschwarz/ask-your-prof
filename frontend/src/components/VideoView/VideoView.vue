<template>
  <video class="video" ref="videoRef" controls>
    <source :src="videoPath" type="video/mp4" />
    Your browser does not support the video.
  </video>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";

defineProps<{
  videoPath: string;
}>();

const videoRef = ref<HTMLVideoElement | null>(null);

onMounted(() => {
  if (videoRef.value) {
    videoRef.value.currentTime = 3600;
  }
});
</script>

<style scoped>
.video {
  min-width: 300px;
  max-width: 400px;
}
</style>
