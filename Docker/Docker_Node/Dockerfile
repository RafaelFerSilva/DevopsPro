FROM node:20.10.0-alpine3.19
WORKDIR /app
USER node
COPY --chown=node:node package*.json    .
RUN npm install
COPY --chown=node:node .    .
EXPOSE 8080
CMD [ "node", "server.js" ]