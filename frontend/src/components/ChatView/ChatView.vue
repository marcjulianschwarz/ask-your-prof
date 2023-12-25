<template>
  <h1>Ask your Prof</h1>
  <div class="chat-container">
    <div class="chat-view-container">
      <p>This is your prof. Ask a question about his or her lecture.</p>
      <form @submit="say">
        <input type="text" v-model="question" placeholder="Ask a question" />
        <button type="submit">Send</button>
      </form>
      <ChatHistory :messages="messages" />
    </div>
    <!-- <DocListView :docs="docs" :key="answer" /> -->
    <VideoView :videoPath="path" />
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { askQuestion, type TextDocument } from "@/api/ChatAPI";
import ChatHistory from "./ChatHistory/ChatHistory.vue";
import DocListView from "../DocListView/DocListView.vue";
import VideoView from "../VideoView/VideoView.vue";

const path = "http://127.0.0.1:5000/video?doc_id=20211011-2";
const question = ref("");
const answer = ref("");
const messages = ref([
  {
    id: 1,
    text: "Hello! I am an AI.",
    type: "🤖",
  },
  {
    id: 2,
    text: "Hi I am a nice human that is awesome.",
    type: "👨🏻‍💻",
  },
  {
    id: 3,
    text: "Moin.",
    type: "🤖",
  },
]);

const docs = ref<TextDocument[]>([]);

function say(event: Event) {
  event.preventDefault();
  messages.value.push({
    id: messages.value.length + 1,
    text: question.value,
    type: "👨🏻‍💻",
  });

  askQuestion(question.value).then((answerRes) => {
    answer.value = answerRes.answer;
    messages.value.push({
      id: messages.value.length + 1,
      text: answer.value,
      type: "🤖",
    });
    docs.value = answerRes.docs;
  });

  question.value = "";
}
</script>

<style scoped src="./ChatView.css"></style>
