# docker运行方式

## ubuntu:latest

```bash
docker run --rm -it   -v "$(pwd):/search_github_app"   -w "/search_github_app"   -p 3001:3001   ubuntu bash -c "apt-get update && apt-get install -y python3 python3-pip && pip3 install --no-cache-dir -r requirements.txt && python3 app.py"
```

## python:3.9-slim

```bash
docker run --rm -it \
    -v "$(pwd):/search_github_app" \
    -w "/search_github_app" \
    -p 3001:3001 \
    python:3.9-slim bash -c "apt-get update && apt-get install -y bash && pip install --no-cache-dir -r requirements.txt && python app.py"
```

## python:3.9-alpine

```bash
docker run --rm -it -p 3001:3001 -v "$(pwd):/app" -w "/app" python:3.9-alpine sh -c "apk add --no-cache bash && pip install --no-cache-dir -r requirements.txt && python app.py"
```
