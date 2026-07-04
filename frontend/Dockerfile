FROM node:22-alpine AS base
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .

FROM base AS development
CMD ["npm", "run", "dev"]

FROM base AS production
RUN npm run build
CMD ["npm", "run", "start"]
