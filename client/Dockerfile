# syntax=docker/dockerfile:1

FROM node:22.9-slim
WORKDIR /client
COPY package.json package.json
RUN npm install
COPY . .
CMD ["npm", "run", "dev", "--", "--host"]
