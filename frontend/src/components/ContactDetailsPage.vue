<script setup lang="ts">
import { ref, onMounted } from "vue";
import axios from "axios";
import { useRoute, useRouter } from "vue-router";
import ContactForm from "./ContactForm.vue";

// Base API URL
let contacts = ref<{ id: number | undefined; name: string; address: string; contact_number: string; email?: string }[]>([]);
const baseUrl = "http://localhost:5000";
const contactEndpoint = `${baseUrl}/api/contact`;
const selectedContact = ref<{
    id?: number;
    name: string;
    email: string;  // Ensure email is always a string
    address: string;
    contact_number: string;
}>({
  id: undefined,
  name: "",
  email: "",  // Default to empty string instead of undefined
  address: "",
  contact_number: "",
});

const route = useRoute();
const router = useRouter();

const headers = {
  headers: {
    "Content-Type": "application/json",
    "Accept": "application/json",
  },
};

// Fetch contact details on mount
const fetchContactDetails = async () => {
  try {
    const contactId = route.params.id;
    if (contactId) {
      const response = await axios.get(`${contactEndpoint}/get/${contactId}`, headers);
      contacts.value = response.data.contact;
    }
  } catch (error) {
    console.error("Error fetching contact details:", error);
  }
};

const saveContact = async (contact: any) => {
    saveUpdateContact(contact);
};

const updateContact = (contact: any) => {
    const index = contacts.value.findIndex((c) => c.id === contact.id);
    if (index !== -1) {
        contacts.value[index] = contact;
    }
    saveUpdateContact(contact);
};

// Save or update contact
const saveUpdateContact = async (contact: any) => {
    let response = null;
    try {
        if (contact.id) {
            // if there is a contact.id, then we consider this process as update
            response = await axios.put(`${contactEndpoint}/update/${contact.id}`, contact, headers);
        } else {
            // considering this as a create new record process
            response = await axios.post(`${contactEndpoint}/create`, contact, headers);
        }
        console.log("response", response);
        contacts.value = response.data.contacts;
    } catch (error) {
        console.error(error);
    }
    router.push("/contacts");
}


// Fetch contacts on component mount
onMounted(fetchContactDetails);
</script>

<template>
  <div class="contact-details">
    <h1>Contact Details</h1>
    <ContactForm
    :contact="selectedContact"
    @save="saveContact"
    @update="updateContact"
    />
  </div>
</template>

<style scoped>
.contact-details {
  max-width: 600px;
  margin: 0 auto;
}
.contact-info {
  margin-top: 20px;
}
</style>
