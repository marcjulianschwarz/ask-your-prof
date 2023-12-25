import "./assets/main.css";

import { createApp } from "vue";
import { createPinia } from "pinia";
import App from "./App/App.vue";

const pinia = createPinia();
const app = createApp(App);

app.use(pinia);
app.mount("#app");
