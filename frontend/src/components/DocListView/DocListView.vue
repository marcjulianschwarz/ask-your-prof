<template>
  <div v-if="props.docs.length > 0" class="doc-list-view">
    <div class="header">
      <p class="doc-title">{{ currentDoc.id || "Lecture Video 11" }}</p>
      <div class="controls">
        <ArrowButton @click="previousDoc" direction="left" size="small" />
        <p class="idx">{{ diplayIndex }} / {{ docs.length }}</p>
        <ArrowButton @click="nextDoc" direction="right" size="small" />
      </div>
    </div>

    <DocView :doc="currentDoc" :key="currentDoc.content" />
  </div>
</template>

<script setup lang="ts">
import DocView from "../DocView/DocView.vue";
import { computed, defineProps, ref } from "vue";
import type { TextDocument } from "@/api/ChatAPI";
import ArrowButton from "../Button/ArrowButton.vue";

const props = defineProps<{ docs: TextDocument[] }>();
const selectedIndex = ref(0);

const currentDoc = computed(() => {
  return props.docs[selectedIndex.value];
});

const diplayIndex = computed(() => {
  return selectedIndex.value + 1;
});

function nextDoc() {
  if (selectedIndex.value < props.docs.length - 1) {
    selectedIndex.value++;
  }
}

function previousDoc() {
  if (selectedIndex.value > 0) {
    selectedIndex.value--;
  }
}
</script>

<style scoped>
.doc-list-view {
  /* gap: 1rem;
  display: flex;
  flex-direction: row;
  width: 500px;
  align-items: center; */
  max-width: 600px;
}

.header {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.doc-title {
  font-weight: bold;
  color: rgb(85, 85, 85);
}

.controls {
  display: flex;
  gap: 1rem;
  align-items: center;
  justify-content: flex-end;
  user-select: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.idx {
  width: 40px;
  text-align: center;
  user-select: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.btn {
  color: #007bff;
  cursor: pointer;
  user-select: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  /* For Internet Explorer: */
}
</style>
