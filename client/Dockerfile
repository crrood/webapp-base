# syntax=docker/dockerfile:1

FROM node:20
WORKDIR /client
COPY package.json package.json
RUN npm install
COPY . .
CMD ["npm", "run", "dev", "--", "--host"]
