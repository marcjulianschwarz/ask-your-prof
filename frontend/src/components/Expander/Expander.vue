<template>
  <div class="expander">
    <div class="expander__header" @click="expand">
      <p>{{ title }}</p>
    </div>

    <div v-if="expanded" class="expander__body">
      <slot />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

const expanded = ref(false);

const expand = () => {
  expanded.value = !expanded.value;
};

defineProps<{
  title: string;
}>();
</script>

<style scoped>
.expander {
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-bottom: 1rem;
}

.expander__header {
  padding: 1rem;
  cursor: pointer;
}

.expander__header > p {
  font-weight: bold;
}

.expander__body {
  padding: 1rem;
}
</style>
