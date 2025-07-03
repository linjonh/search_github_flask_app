#!/bin/bash
#创建识别指令的case语句，识别是创建还是更新docker,指令参数分别是-c，-u
case "$1" in
    -c|create)
        echo "▶ 创建新容器..."
        echo "▶ 停止旧容器..."
        docker stop search_github && docker rm search_github

        echo "▶ 删除镜像"
        docker rmi search_github

        echo "▶ 构建新镜像..."
        docker build -t ghcr.io/linjonh/search_github:latest .

        echo "▶ 推送镜像..."
        docker push  ghcr.io/linjonh/search_github:latest
        echo "✅ 创建完成！"
        exit 0
        ;;
    -u|update)
        echo "▶ 更新容器..."
        # 继续执行后续更新流程
        echo "▶ 停止旧容器..."
        docker stop search_github && docker rm search_github
        echo "▶ 删除镜像"
        docker rmi search_github

        echo "▶ pull镜像"
        docker pull ghcr.io/linjonh/search_github:latest

        echo "▶ 启动新容器..."
        docker run -d -p 3003:3003 --name search_github ghcr.io/linjonh/search_github:latest

        echo "✅ 更新完成！"
        ;;
    *)
        echo "用法: $0 {-c|create|-u|update}"
        exit 1
        ;;
esac


