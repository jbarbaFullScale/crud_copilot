import { createRouter, createWebHistory } from "vue-router";
import LandingPage from "./components/LandingPage.vue";
import ContactPage from "./components/ContactPage.vue";
import ContactDetailsPage from "./components/ContactDetailsPage.vue";

const routes = [
  { path: "/", component: LandingPage },
  { path: "/contacts", component: ContactPage },
  { path: "/contacts/:id", component: ContactDetailsPage, props: true },
  { path: "/contacts/new", component: ContactDetailsPage, props: true },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
