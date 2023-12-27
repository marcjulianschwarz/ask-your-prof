<script setup lang="ts">
import ChatView from "@/components/ChatView/ChatView.vue";
</script>

<template>
  <div class="container">
    <h1>Ask your Prof</h1>
    <ChatView />
  </div>
</template>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
}
</style>
