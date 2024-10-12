<template>
  <div class="settings">
    <form>
      <div>
        <label for="prompt">Prompt</label>
        <textarea
          id="prompt"
          :value="model"
          placeholder="Enter a prompt for the chat"
        />
      </div>
      <p>Hello {{ model }}</p>
      <Button>Update Settings</Button>
    </form>
  </div>
</template>

<script setup lang="ts">
import Button from "@/components/Button/Button.vue";
import { defineModel } from "vue";

const model = defineModel<string>();
</script>

<style scoped>
textarea {
  width: 700px;
  height: 300px;
  font-size: 1rem;
}

form > div {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

label {
  font-size: 1rem;
  font-weight: bold;
}
</style>
