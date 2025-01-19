# Use the Node.js 20 Alpine image
FROM node:22.12.0-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy only the package files to install dependencies
COPY class_react/package*.json .

# Install dependencies
RUN npm install

# Copy all the application files
COPY . .

# Build the React app for production
RUN npm run build

# Install a lightweight HTTP server to serve the static build files
RUN npm install -g serve

# Expose port 3000 for the application
EXPOSE 3000

# Command to run the app using 'serve'
CMD ["serve", "-s", "build", "-l", "3000"]