FROM node:14-alpine

WORKDIR /usr/src/app

COPY ./app/package.json .

RUN npm i --silent --no-warnings

COPY ./app .

ENV HOST 0.0.0.0
EXPOSE 3000

CMD [ "npm", "run", "dev"]
