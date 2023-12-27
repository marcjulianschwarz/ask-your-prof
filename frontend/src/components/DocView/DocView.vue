<template>
  <div v-if="props.doc" class="doc">
    <p class="content">{{ docDisplay }}</p>
    <Button v-if="showAll" @click="showAll = false">Show less</Button>
    <Button v-else="showAll" @click="showAll = true">Show more</Button>
  </div>
</template>

<script setup lang="ts">
import type { TextDocument } from "@/api/ChatAPI";
import { computed, defineProps, ref } from "vue";
import Button from "../Button/Button.vue";

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

<style scoped>
.content {
  text-align: justify;
  margin-bottom: 15px;
}
</style>
