# 构建前端React应用
FROM node:latest as build
WORKDIR /app
COPY ./react_app/package*.json /app/
#COPY ./react_app/package-lock.json /app/
RUN npm install
COPY ./react_app/ /app/
RUN npm run build

# 启动React.js服务
CMD ["npm", "start"]