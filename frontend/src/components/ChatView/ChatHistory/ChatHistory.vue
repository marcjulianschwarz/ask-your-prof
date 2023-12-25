<template>
  <div class="chat-history">
    <Message
      v-for="message in messages"
      :key="message.id"
      :message="message.text"
      :type="message.type"
    />
  </div>
</template>

<script setup lang="ts">
import Message from "./Message/Message.vue";
import { defineProps } from "vue";

interface ChatMessage {
  id: number;
  text: string;
  type: string;
}

const props = defineProps<{
  messages: ChatMessage[];
}>();
</script>

<style scoped src="./ChatHistory.css"></style>
