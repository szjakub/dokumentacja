FROM node:14-alpine

WORKDIR /usr/src/app

COPY ./app /usr/src/app

RUN npm i

ENV HOST 0.0.0.0
EXPOSE 3000

CMD [ "npm", "run", "dev"]
