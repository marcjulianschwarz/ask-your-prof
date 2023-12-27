<template>
  <div class="chat-history">
    <Message
      v-for="message in messages"
      :key="message.id"
      :message="message.message"
      :icon="message.icon"
    />
  </div>
</template>

<script setup lang="ts">
import type { BotChatMessage, HumanChatMessage } from "@/api/ChatAPI";
import Message from "./Message/Message.vue";

defineProps<{
  messages: (BotChatMessage | HumanChatMessage)[];
}>();
</script>

<style scoped>
.chat-history {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-top: 30px;
}
</style>
