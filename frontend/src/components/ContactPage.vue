<script setup lang="ts">
import axios from "axios";
import { onMounted, ref, computed } from "vue";

let contacts = ref<{ id: number; name: string; address: string; contact_number: string; email?: string }[]>([]);
const searchQuery = ref("");
const baseUrl = "http://localhost:5000";
const contactEndpoint = `${baseUrl}/api/contact`;
const headers =  {
    headers: {
        "Content-Type": "application/json",
        Accept: "application/json"
    }
};

onMounted(async () => {
  getContacts();
});

// Fetch contacts from the API
const getContacts = async () => {
    try {
        const response = await axios.get<{ contacts: object[] }>(
            `${contactEndpoint}/get`, headers
        );
        console.log("response", response);
        contacts.value = response.data.contacts as { id: number; name: string; address: string; contact_number: string; email?: string }[];

    } catch (error) {
        console.error(error);
    }
};

const deleteContact = async (contact: any) => {
    let delete_confirmed = confirm(`Are you sure you want to delete contact ${contact.name} with id: ${contact.id}?`);
    const deleteEndpoint = `${contactEndpoint}/delete/${contact.id}`;
    if (!delete_confirmed){
        return;
    }
    try {
        const response = await axios.delete(deleteEndpoint);
        console.log("response", response);
        if (response.status == 200) {
            alert(`Contact \"${contact.name}\" with id: ${contact.id} has been deleted successfully`);
        }
        contacts.value = response.data.contacts;
    } catch (error) {
        console.error(error);
    }
    getContacts();

}
const filteredContacts = computed(() => {
  return (contacts.value) ? contacts.value.filter((contact: any) => {
    const query = searchQuery.value.toLowerCase();
    return (
      contact.name.toLowerCase().includes(query) ||
      contact.email.toLowerCase().includes(query) ||
      contact.address.toLowerCase().includes(query) ||
      contact.contact_number.toLowerCase().includes(query)
    );
  }) : [];
});

</script>

<template>
  <div>
    <h1 class="text-xl font-bold mb-4">Contacts</h1>
    <input
      v-model="searchQuery"
      type="text"
      placeholder="Search contacts..."
      class="w-full p-2 border rounded mb-4"
    />
    <button>
      <router-link to="/contacts/new">
        Add Contact
      </router-link>
    </button>
    <div class="container">
        <div class="list-container">
            <ul>
            <li v-for="contact in filteredContacts" :key="contact.id" class="border p-2 mt-2">
                <span>{{ contact.name }} - {{ contact.email }}</span>
                <router-link :to="'contacts/' + contact.id">
                    <button class="ml-4 text-blue-500">Edit</button>
                </router-link>
                <button @click="deleteContact(contact)" class="ml-4 text-blue-500">Delete</button>
            </li>
            </ul>
        </div>
    </div>
  </div>
</template>
