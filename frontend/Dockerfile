# Use official Node.js image as base
FROM node:18

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the frontend code
COPY . .

# Build the Vue project
RUN npm run build

# Expose port for serving the frontend
EXPOSE 5173

# Start the frontend server
CMD ["npm", "run", "dev"]
