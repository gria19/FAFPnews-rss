import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")


def summarize_article(title, content):
    prompt = f"""
你是一位新闻翻译和摘要专家。请将以下英文新闻翻译成中文，并生成一段 500字以内的中文摘要：

标题：{title}

正文：{content}

输出格式：
1. 中文标题：
2. 中文翻译（简要段落）：
3. 中文摘要（500字以内）：
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "你是一位严谨的财经新闻翻译员"},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()
