# docker 运行方式

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

# socialify https://socialify.git.ci/

## background pattern

```
Signal
Charlie Brown
Formal Invitation
Plus
Circuit Board
Overlapping Hexagons
Brick Wall
Floating Cogs
Diagonal Stripes
Solid
Transparent
```

## font

```
Inter
Bitter
Raleway
Rokkitt
Source Code Pro
JetBrains Mono
KoHo
Jost
```

## theme

```
dark
light
auto
```

## language

<select id="language-select" name="language" class="select select-bordered select-sm font-semibold" aria-labelledby="language-select-title "><option value="Python">Python</option><option value="HTML">HTML</option><option value="────────" disabled="" style="color: rgb(153, 153, 153); font-style: italic;">────────</option><option value="Amazon">Amazon</option><option value="AMD">AMD</option><option value="Angular">Angular</option><option value="Ansible">Ansible</option><option value="Apple">Apple</option><option value="AssemblyScript">AssemblyScript</option><option value="AWS">AWS</option><option value="Bun">Bun</option><option value="C">C</option><option value="C#">C#</option><option value="C++">C++</option><option value="Clojure">Clojure</option><option value="Cloudflare">Cloudflare</option><option value="CMake">CMake</option><option value="CoffeeScript">CoffeeScript</option><option value="Crystal">Crystal</option><option value="CSS">CSS</option><option value="D">D</option><option value="Dart">Dart</option><option value="Delphi">Delphi</option><option value="Deno">Deno</option><option value="DigitalOcean">DigitalOcean</option><option value="Discord">Discord</option><option value="Django">Django</option><option value="DM">DM</option><option value="Docker">Docker</option><option value="Dockerfile">Dockerfile</option><option value="Elixir">Elixir</option><option value="Elm">Elm</option><option value="Erlang">Erlang</option><option value="ESLint">ESLint</option><option value="Express">Express</option><option value="F#">F#</option><option value="FastAPI">FastAPI</option><option value="Figma">Figma</option><option value="Flask">Flask</option><option value="Flutter">Flutter</option><option value="Fortran">Fortran</option><option value="Gatsby">Gatsby</option><option value="Git">Git</option><option value="GitHub">GitHub</option><option value="GitHub Actions">GitHub Actions</option><option value="Go">Go</option><option value="Google">Google</option><option value="Google Cloud">Google Cloud</option><option value="GraphQL">GraphQL</option><option value="Groovy">Groovy</option><option value="Haskell">Haskell</option><option value="Heroku">Heroku</option><option value="Hugging Face">Hugging Face</option><option value="Java">Java</option><option value="JavaScript">JavaScript</option><option value="Julia">Julia</option><option value="Jupyter Notebook">Jupyter Notebook</option><option value="Kafka">Kafka</option><option value="Kotlin">Kotlin</option><option value="Kubernetes">Kubernetes</option><option value="Laravel">Laravel</option><option value="Linux">Linux</option><option value="Lua">Lua</option><option value="macOS">macOS</option><option value="Microsoft">Microsoft</option><option value="Microsoft Azure">Microsoft Azure</option><option value="MongoDB">MongoDB</option><option value="MySQL">MySQL</option><option value="NestJS">NestJS</option><option value=".NET">.NET</option><option value="Netlify">Netlify</option><option value="Next.js">Next.js</option><option value="Nginx">Nginx</option><option value="Nim">Nim</option><option value="Node.js">Node.js</option><option value="NPM">NPM</option><option value="Nuxt">Nuxt</option><option value="Nvidia">Nvidia</option><option value="OCaml">OCaml</option><option value="OpenAI">OpenAI</option><option value="OpenCV">OpenCV</option><option value="Perl">Perl</option><option value="PHP">PHP</option><option value="PostgreSQL">PostgreSQL</option><option value="PowerShell">PowerShell</option><option value="Puppet">Puppet</option><option value="PyTorch">PyTorch</option><option value="R">R</option><option value="React">React</option><option value="Redis">Redis</option><option value="Ruby">Ruby</option><option value="Ruby on Rails">Ruby on Rails</option><option value="Rust">Rust</option><option value="Sass">Sass</option><option value="Scala">Scala</option><option value="scikit-learn">scikit-learn</option><option value="Shell">Shell</option><option value="Slack">Slack</option><option value="Spring Boot">Spring Boot</option><option value="Supabase">Supabase</option><option value="Svelte">Svelte</option><option value="Swift">Swift</option><option value="Tailwind">Tailwind</option><option value="Tampermonkey">Tampermonkey</option><option value="TensorFlow">TensorFlow</option><option value="Terraform">Terraform</option><option value="Twitch">Twitch</option><option value="TypeScript">TypeScript</option><option value="Vercel">Vercel</option><option value="Visual Studio">Visual Studio</option><option value="VSCode">VSCode</option><option value="Vue">Vue</option><option value="WebAssembly">WebAssembly</option><option value="Webpack">Webpack</option><option value="Windows">Windows</option><option value="Zig">Zig</option></select>


![](https://socialify.git.ci/EbookFoundation/free-programming-books/image?custom_language=Python&description=1&font=Raleway&forks=1&issues=1&language=1&logo=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F4921183%3Fv%3D4&name=1&owner=1&pattern=Floating+Cogs&pulls=1&stargazers=1&theme=Dark)

![free-programming-books](https://socialify.git.ci/{{repo.full_name}}/image?custom_language={{repo.language}}&description=1&font=Raleway&forks=1&issues=1&language=1&logo={{repo.owner.avatar_url | urlencode }}&name=1&owner=1&pattern=Brick+Wall&pulls=1&stargazers=1&theme=Dark)
https://socialify.git.ci/EbookFoundation/free-programming-books/image?custom_language=C%23&description=1&font=KoHo&forks=1&issues=1&language=1&logo=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F4921183%3Fv%3D4&name=1&owner=1&pattern=Floating+Cogs&pulls=1&stargazers=1&theme=Light