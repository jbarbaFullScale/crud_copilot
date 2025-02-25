<script setup lang="ts">
import axios from "axios";
import { onMounted, ref } from "vue";
import ContactForm from "./ContactForm.vue";

const contacts = ref<object[]>([]);
const baseUrl = "http://127.0.0.1:5000";
const saveUpdateDeleteEndpoint = `${baseUrl}/api/contact`;
const allContactsEndpoint = `${baseUrl}/api/users`;

onMounted(async () => {
  getContacts();
});

// Track the selected contact for editing
const selectedContact = ref(null);

// Fetch contacts from the API
const getContacts = async () => {
    try {
        const response = await axios.get<{ contacts: object[] }>(
            allContactsEndpoint
        );
        console.log("response", response);
        contacts.value = response.data.contacts;
    } catch (error) {
        console.error(error);
    }
};

// Save or update contact to the API
const saveUpdateContact = async (contact: any) => {
    debugger;
    let response = null;
    try {
        if (contact.id) {
            // if there is a contact.id, then we consider this process as update
            response = await axios.put(saveUpdateDeleteEndpoint, contact);
        } else {
            // considering this as a create new record process
            response = await axios.post(saveUpdateDeleteEndpoint, contact);
        }
        console.log("response", response);
        contacts.value = response.data.contacts;
    } catch (error) {
        console.error(error);
    }
    getContacts();
}

// Handle saving a new contact
const saveContact = async (contact: any) => {
    selectedContact.value = null;
    saveUpdateContact(contact)
};

// Handle updating an existing contact
const updateContact = (contact: any) => {
    const index = contacts.value.findIndex((c) => c.id === contact.id);
    if (index !== -1) {
        contacts.value[index] = contact;
    }
    selectedContact.value = null;
    saveUpdateContact(contact);
    getContacts();
};


// Set contact for editing
const editContact = (contact: any) => {
    selectedContact.value = contact;
};

const deleteContact = async (contact: any) => {
    let delete_confirmed = confirm(`Are you sure you want to delete contact ${contact.name} with id: ${contact.id}?`);
    const deleteEndpoint = `${saveUpdateDeleteEndpoint}/${contact.id}`;
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

</script>

<template>
  <div>
    <h1 class="text-xl font-bold mb-4">Contacts</h1>
    <ContactForm
      :contact="selectedContact"
      @save="saveContact"
      @update="updateContact"
    />
    <ul>
      <li v-for="contact in contacts" :key="contact.id" class="border p-2 mt-2">
        <span>{{ contact.name }} - {{ contact.email }}</span>
        <button @click="editContact(contact)" class="ml-4 text-blue-500">Edit</button>
        <button @click="deleteContact(contact)" class="ml-4 text-blue-500">Delete</button>
      </li>
    </ul>
  </div>
</template>
