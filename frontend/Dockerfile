FROM  node:20-alpine

WORKDIR  /app

COPY class_react/package*.json .

RUN npm install 

COPY . .

EXPOSE $PORT

CMD ["npm", "start"]