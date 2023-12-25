<template>
  <div class="message-container">
    <p class="icon">{{ type }}</p>
    <p class="message">{{ message }}</p>
  </div>
</template>

<script setup lang="ts">
import { withDefaults, defineProps } from "vue";

const props = withDefaults(
  defineProps<{
    message: string;
    type: string;
  }>(),
  {
    message: "",
    type: "",
  }
);
</script>

<style scoped src="./Message.css"></style>
