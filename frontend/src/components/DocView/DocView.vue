<template>
  <div v-if="props.doc" class="doc">
    <p class="content">{{ docDisplay }}</p>
    <p v-if="showAll" @click="showAll = false" class="show-more">Show less</p>
    <p v-else="showAll" @click="showAll = true" class="show-more">Show more</p>
  </div>
</template>

<script setup lang="ts">
import type { TextDocument } from "@/api/ChatAPI";
import { computed, defineProps, ref } from "vue";

const props = defineProps<{
  doc: TextDocument;
}>();

const showAll = ref(false);

const docDisplay = computed(() => {
  if (showAll.value) {
    return props.doc.content;
  } else if (props.doc.content.length < 100) {
    return props.doc.content;
  } else {
    return props.doc.content.substring(0, 200) + "...";
  }
});
</script>

<style scoped src="./DocView.css"></style>
