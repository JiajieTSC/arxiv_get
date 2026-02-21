# 🤖 arXiv Daily Research Bot

这是一个基于 **GitHub Actions + Python + LLM** 的自动化科研情报工具。它每天定时从 arXiv 抓取 **VLA (Vision-Language-Action)**、**VLM** 和 **LLM RL** 领域的最新论文，并利用大模型生成中文技术摘要，最后自动部署为静态网页。

## 🌟 功能特点

* **自动追踪**：每日定时运行，无需人工干预。
* **智能总结**：使用 LLM（如 GPT-4o-mini）将晦涩的英文摘要提炼为 3 句中文核心贡献。
* **零成本托管**：利用 GitHub Actions 进行运算，GitHub Pages 进行网页展示，完全免费。
* **移动端友好**：生成的网页采用响应式设计，方便在手机上随时翻阅。

## 🛠️ 技术栈

* **核心语言**: Python 3.10
* **数据来源**: [arXiv API](https://arxiv.org/help/api/)
* **自动化**: GitHub Actions
* **网页部署**: GitHub Pages
* **AI 引擎**: OpenAI / DeepSeek API (兼容 OpenAI 格式)

## 🚀 快速开始

### 1. 克隆/创建仓库

将本项目的所有代码上传至你的 GitHub 仓库：

* `arxiv_bot.py`: 核心处理逻辑。
* `.github/workflows/daily_arxiv.yml`: 自动化流水线配置。

### 2. 配置 API Key (重要)

为了让机器人能够生成总结，你需要配置 LLM 的 API 密钥：

1. 前往仓库的 **Settings** -> **Secrets and variables** -> **Actions**。
2. 点击 **New repository secret**。
3. Name 填入：`LLM_API_KEY`。
4. Value 填入：你的 API 密钥（如 `sk-xxxx...`）。

### 3. 开启权限

1. 前往 **Settings** -> **Actions** -> **General**。
2. 找到 **Workflow permissions**，选择 **Read and write permissions**。
3. 点击 **Save**。

### 4. 激活网页展示

1. 手动运行一次 Action（在 **Actions** 标签页选择 workflow 并点击 **Run workflow**）。
2. 运行成功后，前往 **Settings** -> **Pages**。
3. 在 **Branch** 处选择 `gh-pages` 分支并点击 **Save**。
4. 几分钟后，你的专属论文周报网站即可上线！

## 📂 项目结构

```bash
.
├── .github/workflows/
│   └── daily_arxiv.yml    # 每天早晨 9:00 自动运行的定时任务
├── arxiv_bot.py           # 抓取论文、调用 AI 并生成 HTML 的脚本
├── README.md              # 项目说明文档
└── index.html             # (自动生成) 最终展示的网页

```

## ⚙️ 自定义配置

你可以直接在 `arxiv_bot.py` 中修改 `KEYWORDS` 变量来追踪你感兴趣的方向：

```python
KEYWORDS = ['"Vision-Language-Action"', '"VLM"', '"LLM RL"']

```

---

## ⚠️ 免责声明

本项目生成的总结由 AI 自动完成，仅供科研参考。请务必点击链接阅读原论文以获取准确信息。

---

**💡 提示**：如果你想修改 AI 总结的风格（比如更硬核或更通俗），可以调整 `arxiv_bot.py` 中的 `prompt` 变量。

---
