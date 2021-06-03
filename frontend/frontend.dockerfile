FROM node:14-alpine

ENV APP_ROOT /app

WORKDIR ${APP_ROOT}

RUN npm install

ENV HOST 0.0.0.0

EXPOSE 3000

CMD ["npm", "run", "start"]