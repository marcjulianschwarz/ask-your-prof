<template>
  <button>
    <slot />
  </button>
</template>

<style scoped>
button {
  color: #007bff;
  cursor: pointer;
  outline: none;
  border: none;
  background-color: white;
  font-size: 1rem;
  width: fit-content;
  padding: 0;
}

button:hover {
  color: #81b9f4;
}
</style>
