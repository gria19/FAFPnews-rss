from openai import OpenAI
import time

client = OpenAI()

def summarize_article(title, content):
    prompt = f"""请将下面这篇英文文章的内容翻译成中文并压缩为不超过500字的摘要，保持语义完整：

标题：{title}
正文：{content}"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "你是一个擅长总结英文文章的中文编辑。"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=400
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"❌ ChatGPT 出错：{e}")
        time.sleep(2)
        return None
