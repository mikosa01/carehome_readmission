# Use Node.js to build the app
FROM node:18-alpine AS builder

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json to install dependencies
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the app source code
COPY . .

# Build the app for production
RUN npm run build

# Use a lightweight web server to serve the built app
FROM nginx:alpine

# Copy the production build from the builder stage
COPY --from=builder /app/build /usr/share/nginx/html

# Expose port 80 to serve the app
EXPOSE 80

# Start the Nginx server
CMD ["nginx", "-g", "daemon off;"]