from flask import Flask, render_template, request
import requests
import markdown2
import os

app = Flask(__name__)

GITHUB_API_URL = "https://api.github.com/search/repositories"
README_URL_TEMPLATE = "https://raw.githubusercontent.com/{}/master/README.md"

# 可选：GitHub 令牌（从环境变量读取或硬编码）
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")

@app.route("/", methods=["GET"])
def index():
    print("Received request for index page")
    # 获取查询参数
    query = request.args.get("q", default="stars:>50000")
    language = request.args.get("language", default="")
    sort = request.args.get("sort", default="stars")
    order = request.args.get("order", default="desc")
    page = int(request.args.get("page", 1))

    full_query = query
    if language:
        full_query += f" language:{language}"

    params = {
        "q": full_query,
        "sort": sort,
        "order": order,
        "per_page": 20,
        "page": page
    }

    headers = {
        "Accept": "application/vnd.github+json"
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"

    response = requests.get(GITHUB_API_URL, params=params, headers=headers)
    print("response status code:", response.status_code)
    items = response.json().get("items", []) if response.status_code == 200 else []

    # 添加 README 内容（简单处理）
    results = []
    for repo in items:
        repo_data = repo.copy()
        try:
            readme_url = README_URL_TEMPLATE.format(repo["full_name"])
            readme_resp = requests.get(readme_url)
            if readme_resp.status_code == 200:
                raw = readme_resp.text[:1000]  # 只取前 1000 字节
                html = markdown2.markdown(raw)
                repo_data["readme"] = html
            else:
                repo_data["readme"] = ""
        except:
            repo_data["readme"] = ""
        results.append(repo_data)

    return render_template(
        "index.html",
        results=results,
        query=query,
        language=language,
        sort=sort,
        order=order,
        page=page
    )

if __name__ == "__main__":
    app.run(debug=True)
