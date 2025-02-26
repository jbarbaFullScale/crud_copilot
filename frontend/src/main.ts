import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from "./router.js"; // Import the router


const app = createApp(App);
app.use(router); // Use Vue Router
app.mount("#app");
import { useRouter } from "vue-router";
