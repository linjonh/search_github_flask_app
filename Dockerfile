FROM ubuntu

COPY . /search_github_app

WORKDIR /search_github_app

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install --no-cache-dir -r requirements.txt

# 声明容器内的端口
EXPOSE 3001
    
CMD ["python3", "app.py"]

