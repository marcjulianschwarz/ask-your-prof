<script setup lang="ts">
import Expander from "@/components/Expander/Expander.vue";
import ChatSettings from "@/components/ChatSettings/ChatSettings.vue";
import ChatView from "@/components/ChatView/ChatView.vue";
import { ref } from "vue";

const prompt = ref(`Answer the question (see QUESTION) in a concise way.

You will have access to parts of a lecture transcript (see CONTEXT) that may help you answer the question. 
Please try to answer the question using only the information in the context. 
For this it might help to summarize the context in your own words.

If you can not answer the question that way, answer with "I have to use my general knowledge." 
and then answer the question using your general knowledge.

Only use your general knowledge when it is absolutely necessary.
In all other cases, try to answer the question using only the information in the context.

CONTEXT: {trans}

QUESTION: {question}
`);
</script>

<template>
  <div class="container">
    <h1>Ask Your Prof</h1>
    <Expander title="Settings">
      <ChatSettings v-model="prompt" />
    </Expander>
    <ChatView :prompt="prompt" />
  </div>
</template>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
}
</style>
