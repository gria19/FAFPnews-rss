import os
import google.generativeai as genai
import time

# ✅ 从 GitHub Secrets 中读取 Gemini API Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel('models/gemini-pro')


def summarize_article(title, content):
    prompt = f"""请将下面这篇英文文章的内容翻译成中文并压缩为不超过200字的摘要，保持语义完整：

标题：{title}
正文：{content}"""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"❌ Gemini 出错：{e}")
        time.sleep(2)
        return None
