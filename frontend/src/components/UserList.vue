<template>
  <div>
    <h1>Contacts List</h1>
    <ul>
      <!-- add condition to see if there are no contacts then say "no contacts" -->
      <li v-if="contacts.length === 0">No contacts</li>
      <li v-else v-for="contact in contacts" :key="contact.id">{{ contact.name }}</li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import axios from "axios";

const contacts = ref<object[]>([]);

onMounted(async () => {
  try {
    const response = await axios.get<{ contacts: object[] }>(
      "http://127.0.0.1:5000/api/users"
    );
    console.log("response", response);
    contacts.value = response.data.contacts;
  } catch (error) {
    console.error(error);
  }
});
</script>
