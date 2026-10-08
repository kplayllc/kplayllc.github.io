# Kplay LLC — Quantitative Trading & Research Homepage

这是一个用于 **private investment / proprietary quantitative trading research** 的单页公司主页。整体是深色、简洁的科技金融风格；没有登录、交易接口、客户账户或资金募集功能。

网页使用 **HTML + CSS + 少量 JavaScript**，另外提供 **纯 Python 本地预览服务**。不需要安装 Flask 或任何第三方 Python 库。

## 文件结构

```text
kplay-quant-homepage/
├── app.py                # PyCharm 本地运行入口（Python 标准库）
├── index.html            # 主页内容
├── assets/
│   ├── style.css         # 网页样式 / 手机适配
│   ├── main.js           # 手机菜单、滚动过渡、版权年份
│   ├── favicon.svg       # 浏览器标签图标
│   └── og-image.svg      # 分享链接时的封面图
├── .gitignore
└── README.md
```

## 1. PyCharm 本地打开

1. 解压文件夹，在 PyCharm 里 **Open** 这个文件夹。
2. 使用 Python 3.9+ 解释器（项目不需要 pip install）。
3. 右键 `app.py` → **Run 'app'**，或在 Terminal 执行：

   ```bash
   python app.py
   ```

4. 浏览器打开：**http://127.0.0.1:8000**。
5. 修改 `index.html` 或 `assets/style.css`，刷新浏览器即可看效果。

如果端口 8000 被占用：

```bash
# macOS / Linux
PORT=8080 python app.py

# Windows PowerShell
$env:PORT=8080; python app.py
```

## 2. 上传 GitHub / 发布在线网站

**GitHub 是代码托管服务，不会自动运行 Python 程序。** 但本项目主页是静态网页，可以直接使用免费的 **GitHub Pages**，无需运行 Python。

1. 在 GitHub 创建仓库，例如 `kplay-website`。
2. 将本文件夹的文件上传到仓库 **根目录**（确保根目录有 `index.html`）。
3. 打开仓库的 **Settings → Pages**。
4. 在 **Build and deployment** 中选择 **Deploy from a branch**。
5. Branch 选 `main`，目录选 `/ (root)`，点击 **Save**。
6. 网站将在 GitHub Pages 完成部署后使用类似以下的地址：
   `https://YOUR-GITHUB-USERNAME.github.io/kplay-website/`

若要使用自己的域名，可随后配置 GitHub Pages 的 Custom domain 和域名 DNS。

## 3. 怎么改内容

- **公司名称 / 标题**：搜索 `index.html` 中的 `KPLAY`、`Kplay LLC`。
- **首页文案**：`index.html` 中 `<section class="hero">`。
- **三个业务重点**：`index.html` 中 `id="focus"`。
- **研究/交易开发流程**：`index.html` 中 `id="process"`。
- **公司介绍**：`index.html` 中 `id="company"`。
- **配色**：`assets/style.css` 开头的 `:root`，特别是 `--accent: #c5ff7b`。
- **网站标题 / 搜索引擎描述 / 分享封面**：`index.html` 的 `<head>` 和 `assets/og-image.svg`。

## 4. 发布前检查

- 文案只描述 **自有资金、私人投资、量化研究和系统开发**，不承诺收益，也不展示编造的业绩数据。
- 页面中的曲线标注了 **Conceptual illustration**，并不是交易业绩。
- 主页不包含投资建议、客户资金募集或交易账户入口。
- 如之后计划对外管理资金或提供投资咨询，在网站发布相应宣传内容前应先确认适用的合规要求。

## 5. 日后扩展交易系统

建议把未来的交易系统（策略研究、回测、数据、交易执行）放在**独立私有仓库**和隔离环境中，不要把 API keys、券商凭证、资金账户数据或实际交易系统代码放到公开的公司主页仓库。这个网站目前仅用于公开展示公司信息。
