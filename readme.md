# FAFPnews-rss

自动抓取 Foreign Policy 与 Foreign Affairs 的最新文章，使用 ChatGPT 自动翻译成中文并生成简要摘要，最终发布为 RSS Feed。

## 🧩 功能

- 自动抓取每日最新新闻（支持登录态）
- 使用 OpenAI API 翻译英文文章并生成摘要
- 生成符合标准的 RSS 输出（供 RSS 阅读器订阅）
- GitHub Actions 自动运行并部署到 GitHub Pages

## 🚀 快速开始

1. **Fork 本仓库** 或新建仓库后复制本项目结构
2. **添加 GitHub Secrets**（在 `Settings > Secrets > Actions`）
   - `OPENAI_API_KEY`：你的 OpenAI API 密钥
   - `FP_COOKIE`：你从 Foreign Policy 获取的 Cookie
   - `FA_COOKIE`：你从 Foreign Affairs 获取的 Cookie
3. **启用 GitHub Pages**（部署 RSS 输出）
   - 进入仓库 `Settings > Pages`
   - Source 选择 `gh-pages` 分支
4. 自动生成的 RSS 地址示例：
   ```
   https://your-username.github.io/foreign-news-rss/rss.xml
   ```

## 📱 推荐 RSS 阅读器

- **Reeder**（iOS/macOS）
- **NetNewsWire**（开源免费）
- **Feedly**（跨平台）

## 📦 依赖

请确保环境中安装以下 Python 库（GitHub Actions 会自动安装）：

```
beautifulsoup4
requests
openai
feedgen
```

## 🧠 示例调用结果

生成的 RSS 条目包括：
- 中文标题
- 原始文章链接
- ChatGPT 翻译后的简明摘要

---

如有任何问题，欢迎创建 Issue 或联系作者。
