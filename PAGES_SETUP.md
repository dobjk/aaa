# AAA Pages 配置说明

1. 将压缩包内 aaa 文件夹的内容复制到原来的 aaa 本地仓库目录。Windows 复制时请确认 .github 文件夹也被复制。不要删除原仓库的 .git。
2. 在 aaa 目录运行 `python upload_pages_config.py`，上传网站配置。原来的 MD 推送脚本不负责上传 .py 和 .yml，所以首次需要这一步。
3. GitHub 仓库 aaa → Settings → Pages → Build and deployment → Source 选择 GitHub Actions。
4. 如果第一次 Actions 运行因 Pages 未启用失败，完成第 3 步后到 Actions → Publish articles to GitHub Pages → Run workflow 重新运行。
5. 先用原来的脚本推送文章。Actions 部署成功后访问 https://dobjk.github.io/aaa/ 。仅已推送到 GitHub 的 MD 会出现在网站里。
6. 后续继续用原来的随机推送脚本；每次 main 分支推送触发网站更新。推送成功和网站部署完成是两个阶段。

## 地址

- 首页：https://dobjk.github.io/aaa/
- 完整目录：https://dobjk.github.io/aaa/catalog.html
- sitemap：https://dobjk.github.io/aaa/sitemap.xml
- 文章：原 MD 路径的后缀改为 .html，中文路径按 URL 编码。

构建时自动将 aaa 仓库文章内的 GitHub MD 链接替换成网页地址。其他仓库链接暂时保留 GitHub 地址，待它们启用 Pages 后再统一调整。原 MD 正文不改写，图片沿用原百度来源。

原有 index.html 和 sitemap.xml 保留在源码中；网站部署时由构建器在 _site 中生成替代文件，不会使用旧 GitHub 地址的 sitemap。

本包没有 .git、账号密码、SSH 密钥，也没有代你开启 GitHub Pages。1000 篇文章包含在包内；未核实正文资讯及内容真实性。本地预览构建：安装 Markdown==3.7 后运行 python build_pages.py。
