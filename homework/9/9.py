import os
import sys
from groq import Groq

# 獲取主題和問題
title = input("請輸入主題：")
question = " ".join(sys.argv[1:])
print("問題：", question)

# 創建 Groq 客戶端
client = Groq(api_key="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")

# 構建消息內容，並明確指示使用繁體中文
message_content = f"""
請使用繁體中文寫一本書。書的主題是{title}，書名需與{title}相關。將書分為一個書名與三個小標題，每個小標題至少200到750字。
"""

try:
    # 創建聊天完成
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message_content,
            }
        ],
        model="llama3-70b-8192",
    )

    # 打印生成的內容
    print(chat_completion.choices[0].message.content)

except Exception as e:
    print(f"Error: {e}")
