<template>
  <div class="chat-container">
    <div class="chat">
      <p>This is your prof. Ask a question about his or her lecture.</p>
      <form @submit="addMessage">
        <input type="text" v-model="question" placeholder="Ask a question" />
        <button class="ask-button" type="submit">Send</button>
      </form>
      <ChatHistory :messages="messages" />
    </div>
    <DocListView :docs="docs" :key="answer" />
  </div>
  <!-- <div class="video-container">
    <VideoView :videoPath="path" />
    <VideoView :videoPath="path" />
  </div> -->
</template>

<script setup lang="ts">
import { ref } from "vue";
import {
  askQuestion,
  BotChatMessage,
  HumanChatMessage,
  type TextDocument,
} from "@/api/ChatAPI";
import ChatHistory from "./ChatHistory/ChatHistory.vue";
import DocListView from "../DocListView/DocListView.vue";
import Button from "../Button/Button.vue";

const question = ref("");
const answer = ref("");
const docs = ref<TextDocument[]>([]);
const messages = ref<Array<BotChatMessage | HumanChatMessage>>([
  new BotChatMessage(1, "Hello, I am your prof. Ask me a question."),
]);

function addMessage(event: Event) {
  event.preventDefault();

  messages.value.push(new HumanChatMessage(1, question.value));

  askQuestion(question.value).then((answerRes) => {
    answer.value = answerRes.answer;
    messages.value.push(new BotChatMessage(1, "Here are some documents"));
    docs.value = answerRes.docs;
  });

  question.value = "";
}
</script>

<style scoped>
.chat-container {
  display: flex;
  flex-direction: row;
  gap: 20px;
  margin-top: 50px;
}

.chat {
  display: flex;
  flex-direction: column;
  gap: 20px;
  max-width: 900px;
}

.video-container {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  gap: 10px;
  max-width: 900px;
}

input {
  padding: 10px 20px 10px 20px;
  width: 300px;
  outline: none;
  border-radius: 500px;
  border-color: black;
  border-style: solid;
  background-color: #303030;
  color: white;
  font-size: 1rem;
}
form {
  display: flex;
  flex-direction: row;
  gap: 20px;
}
.ask-button {
  outline: none;
  border-radius: 500px;
  border-color: black;
  border-style: solid;
  background-color: #303030;
  padding: 10px 20px 10px 20px;
  color: white;
  font-size: 1rem;
  cursor: pointer;
}
#chat-history {
  margin-top: 50px;
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 0px;
}
.ai-chat {
  margin-left: 40px;
}
.doc-box {
  border-style: solid;
  border-color: black;
  border-width: 1px;
  border-radius: 10px;
  padding: 10px 20px 10px 20px;
  cursor: pointer;
}
.doc-box-content.hidden {
  display: none;
}
.doc-box-content {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
</style>
