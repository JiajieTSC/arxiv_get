import arxiv
import datetime
import os
import requests

# --- 配置区 ---
KEYWORDS = ['"Vision-Language-Action"', '"VLM"', '"LLM Reinforcement Learning"', '"LLM Agent"', '"VLM Agent"']
MAX_RESULTS = 10
# 建议在 GitHub Secrets 中配置你的 API Key (如 OpenAI 或 DeepSeek)
API_KEY = os.getenv("LLM_API_KEY") 
API_URL = "https://api.openai.com/v1/chat/completions" # 或其他兼容接口

def get_ai_summary(title, abstract):
    if not API_KEY:
        return "（未配置 API Key，仅显示原始摘要）"
    
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    prompt = f"请作为AI专家，用中文简要总结这篇论文的核心突破（3句话以内）：\n标题: {title}\n摘要: {abstract}"
    
    payload = {
        "model": "gpt-4o-mini", # 或者 deepseek-chat
        "messages": [{"role": "user", "content": prompt}]
    }
    try:
        response = requests.post(API_URL, json=payload, headers=headers, timeout=30)
        return response.json()['choices'][0]['message']['content']
    except:
        return "总结生成失败。"

def main():
    client = arxiv.Client()
    query = ' OR '.join([f'abs:{kw}' for kw in KEYWORDS])
    search = arxiv.Search(query=query, max_results=MAX_RESULTS, sort_by=arxiv.SortCriterion.SubmittedDate)

    html_content = f"""
    <html><head><meta charset="utf-8"><title>arXiv Daily - {datetime.date.today()}</title>
    <style>
        body {{ font-family: -apple-system, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; background: #f4f4f9; }}
        .card {{ background: white; padding: 20px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        h1 {{ color: #333; }}
        .tag {{ background: #007bff; color: white; padding: 2px 8px; border-radius: 4px; font-size: 0.8em; }}
        .summary {{ background: #e9ecef; padding: 10px; border-left: 4px solid #007bff; margin: 10px 0; }}
        a {{ color: #007bff; text-decoration: none; }}
    </style></head><body>
    <h1>🤖 arXiv 论文每日速递 ({datetime.date.today()})</h1>
    """

    for result in client.results(search):
        ai_brief = get_ai_summary(result.title, result.summary)
        html_content += f"""
        <div class="card">
            <h3>{result.title}</h3>
            <p><span class="tag">Published: {result.published.date()}</span> 
               <a href="{result.entry_id}" target="_blank">🔗 查看原文</a></p>
            <div class="summary"><strong>AI 核心总结：</strong><br>{ai_brief}</div>
            <details><summary>查看英文原版摘要</summary><p>{result.summary}</p></details>
        </div>
        """
    
    html_content += "</body></html>"
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

if __name__ == "__main__":
    main()