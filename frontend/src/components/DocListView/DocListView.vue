<template>
  <div v-if="props.docs" class="doc-list-view">
    <h2>Current Documents</h2>
    <div class="controls">
      <Button @click="previousDoc">Previous</Button>
      <p class="idx">{{ diplayIndex }}</p>
      <Button @click="nextDoc">Next</Button>
    </div>
    <DocView :doc="currentDoc" :key="currentDoc.content" />
  </div>
</template>

<script setup lang="ts">
import DocView from "../DocView/DocView.vue";
import { computed, defineProps, ref } from "vue";
import type { TextDocument } from "@/api/ChatAPI";
import Button from "../Button/Button.vue";

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
