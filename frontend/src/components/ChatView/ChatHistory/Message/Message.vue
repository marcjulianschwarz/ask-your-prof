<template>
  <div class="message-container">
    <p class="icon">{{ icon }}</p>
    <p class="message">{{ message }}</p>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  message: string;
  icon: string;
}>();
</script>

<style scoped>
.message-container {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 20px;
}

.icon {
  font-size: 1.5rem;
}
</style>
