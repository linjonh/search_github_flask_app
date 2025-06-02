#!/bin/bash

echo "▶ 停止旧容器..."
docker stop search_github && docker rm search_github

echo "▶ 删除镜像"
docker rmi search_github

echo "▶ 构建新镜像..."
docker build -t ghcr.io/linjonh/search_github:latest .

echo "▶ 启动新容器..."
docker run -d -p 3003:3003 --name search_github ghcr.io/linjonh/search_github:latest

echo "✅ 更新完成！"
