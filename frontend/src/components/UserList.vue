<template>
  <div>
    <h1>User List</h1>
    <ul>
      <li v-for="user in users" :key="user">{{ user }}</li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import axios from "axios";

const users = ref<string[]>([]);

onMounted(async () => {
  try {
    const response = await axios.get<{ users: string[] }>(
      "http://127.0.0.1:5000/api/users"
    );
    users.value = response.data.users;
  } catch (error) {
    console.error(error);
  }
});
</script>
