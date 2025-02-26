<template>
    <div class="landing-page">
        <h1>Welcome to the Contacts CRUD App</h1>
        <p>Manage your contacts easily with this simple CRUD application.</p>
        <router-link to="/contacts">Click here to start interacting</router-link>

    </div>
</template>

<script>
export default {
    data() {
        return {
            contacts: [
                { id: 1, name: "John Doe", email: "john@example.com" },
                { id: 2, name: "Jane Smith", email: "jane@example.com" },
                { id: 3, name: "Bob Johnson", email: "bob@example.com" }
            ],
            newContact: { name: "", email: "" }
        };
    },
    methods: {
        addContact() {
            // Generate a unique ID for the new contact
            const newId = this.contacts.length + 1;

            // Add the new contact to the contacts array
            this.contacts.push({ id: newId, ...this.newContact });

            // Clear the form inputs
            this.newContact = { name: "", email: "" };
        },
        editContact(contact) {
            // Implement the edit functionality here
            // You can open a modal or navigate to a separate edit page
        },
        deleteContact(contact) {
            // Implement the delete functionality here
            // You can show a confirmation dialog before deleting the contact
            // and then remove it from the contacts array
        }
    }
};
</script>

<style scoped>
/* Add your custom styles here */
</style>