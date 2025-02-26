<script setup lang="ts">
import { ref, defineProps, defineEmits, watch } from "vue";

// Define props to handle edit mode
const props = defineProps<{
  contact?: {
    id?: number;
    name: string;
    email: string;
    address: string;
    contact_number: string;
  };
}>();

// Emit events when form is submitted
const emit = defineEmits(["save", "update"]);

// Form data (reactive state)
const contactData = ref({
  name: props.contact?.name || "",
  email: props.contact?.email || "",
  address: props.contact?.address || "",
  contact_number: props.contact?.contact_number || "",
});

// Watch for prop changes (if editing an existing contact)
watch(
  () => props.contact,
  (newContact) => {
    if (newContact) {
      contactData.value = { ...newContact };
    }
  },
  { deep: true }
);

// Handle form submission
const submitForm = () => {
  if (props.contact?.id) {
    emit("update", { ...contactData.value, id: props.contact.id });
  } else {
    emit("save", contactData.value);
  }
  clearForm();
};

// Clear form data and resetting the button to "Add Contact"
const clearForm = () => {
  contactData.value = {
    name: "",
    email: "",
    address: "",
    contact_number: "",
  };
};
</script>

<template>
  <!-- div with border color white -->
  <div class="border-white">
    <form @submit.prevent="submitForm" class="space-y-4 p-4 border rounded-lg shadow-md max-w-md mx-auto">
      <div>
        <label class="block font-medium text-gray-700">Name: </label>
        <input v-model="contactData.name" type="text" class="w-full border rounded p-2" required />
      </div>

      <div>
        <label class="block font-medium text-gray-700">Email: </label>
        <input v-model="contactData.email" type="email" class="w-full border rounded p-2" required />
      </div>

      <div>
        <label class="block font-medium text-gray-700">Address: </label>
        <input v-model="contactData.address" type="text" class="w-full border rounded p-2" required />
      </div>

      <div>
        <label class="block font-medium text-gray-700">Contact Number: </label>
        <input v-model="contactData.contact_number" type="text" class="w-full border rounded p-2" required />
      </div>

      <button
        type="submit"
        class="w-full bg-blue-600 text-white py-2 rounded-md hover:bg-blue-700 transition"
      >
        {{ props.contact?.id ? "Update Contact" : "Add Contact" }}
      </button>
    </form>
  </div>
</template>
