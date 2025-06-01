FROM python:3.9-slim

COPY . /search_github_app

WORKDIR /search_github_app

RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y bash
# 声明容器内的端口
EXPOSE 3001
    
CMD ["python", "app.py"]