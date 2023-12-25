<template>
  <div v-if="props.docs" class="doc-list-view">
    <h2>Current Documents</h2>
    <div class="controls">
      <p class="btn" @click="previousDoc">Previous</p>
      <p class="idx">{{ diplayIndex }}</p>
      <p class="btn" @click="nextDoc">Next</p>
    </div>
    <DocView :doc="currentDoc" :key="currentDoc.content" />
  </div>
</template>

<script setup lang="ts">
import DocView from "../DocView/DocView.vue";
import { computed, defineProps, ref } from "vue";
import type { TextDocument } from "@/api/ChatAPI";

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

<style scoped src="./DocListView.css"></style>
