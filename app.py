from flask import Flask, render_template, request
import requests
import markdown2
import os
import json
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
        "per_page": 30,
        "page": page
    }

    headers = {
        "Accept": "application/vnd.github+json",
        "user-agent":"search github app"
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"

    response = requests.get(GITHUB_API_URL, params=params, headers=headers)
    print("response status code:", response.status_code)
    print(f"response content size={len(response.text)}")
    data=response.json()

    total_count=data.get("total_count",0)
    print(f"total_count repo={total_count}")
    # total_count=0#for test
    if total_count>0:
        items =data.get("items", []) if response.status_code == 200 else []
    else:
        print("load offline data")
        with open("star_over_1w.json","r",encoding="utf-8") as f:
            strs=f.read()
            items=json.loads(strs)["items"]
    
    print(f"loadded items size={len(items)}")
    # 添加 README 内容（简单处理）
    results = []
    for repo in items:
        repo_data = repo.copy()
        # fetch_and_clean_readme(repo, repo_data)
        #处理描述过长问题，处理star数量
        if repo_data.get("description") is not None:
            repo_data["description"]=repo_data.get("description")[:100]
        repo_data["stargazers_count"]=f"{repo_data['stargazers_count']:,}"
        repo_data["forks_count"]=f"{repo_data['forks_count']:,}"
        results.append(repo_data)
        print("Processed repo:", repo_data["full_name"])
    return render_template(
        "index.html",
        results=results,
        query=query,
        language=language,
        sort=sort,
        order=order,
        page=page
    )

def fetch_and_clean_readme(repo, repo_data):
    try:
        readme_url = README_URL_TEMPLATE.format(repo["full_name"])
        readme_resp = requests.get(readme_url)
        if readme_resp.status_code == 200:
            raw = readme_resp.text[:1000]  # 只取前 1000 字节
            html = markdown2.markdown(raw)
            soup = BeautifulSoup(html, 'html.parser')

                # 清理非法嵌套：移除 p 包裹的 a 或未闭合元素
            for a in soup.find_all("a"):
                if a.find_parent("p"):
                    a.unwrap()
            clean_html = str(soup)
            repo_data["readme"] = clean_html
        else:
            repo_data["readme"] = ""
    except:
        repo_data["readme"] = ""

if __name__ == "__main__":
    app.run(debug=True,port=3001)
