<template>
  <svg
    xmlns="http://www.w3.org/2000/svg"
    width="24"
    height="24"
    viewBox="0 0 24 24"
    :class="[size, direction]"
  >
    <polygon
      points="7.293 4.707 14.586 12 7.293 19.293 8.707 20.707 17.414 12 8.707 3.293 7.293 4.707"
    />
  </svg>
</template>

<script setup lang="ts">
withDefaults(
  defineProps<{
    direction: "left" | "right" | "up" | "down";
    size: "small" | "medium" | "large";
  }>(),
  {
    direction: "left",
    size: "small",
  }
);
</script>

<style scoped>
svg {
  fill: lightgray;
  cursor: pointer;
  flex-shrink: 0;
}

svg.small {
  width: 25px;
  height: 25px;
}

svg.medium {
  width: 50px;
  height: 50px;
}

svg.large {
  width: 100px;
  height: 100px;
}

svg.left {
  transform: rotate(180deg);
}

svg.up {
  transform: rotate(-90deg);
}

svg.down {
  transform: rotate(90deg);
}

svg.right {
  transform: rotate(0deg);
}

svg:hover {
  fill: gray;
}
</style>
