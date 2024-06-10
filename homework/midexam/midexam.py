#由chatgpt輔助
import datetime
import requests

# 獲取當前月份和時間
current_time = datetime.datetime.now()
month = current_time.month
hour = current_time.hour

# 根據月份確定季節
if month in [3, 4, 5]:
    season = "春季"
elif month in [6, 7, 8]:
    season = "夏季"
elif month in [9, 10, 11]:
    season = "秋季"
else:
    season = "冬季"

# 根據時間確定用餐時段
if 5 <= hour < 10:
    meal_time = "早餐"
elif 10 <= hour < 14:
    meal_time = "午餐"
elif 14 <= hour < 17:
    meal_time = "下午茶"
elif 17 <= hour < 21:
    meal_time = "晚餐"
else:
    meal_time = "宵夜"

# 使用ipinfo.io獲取位置
try:
    response = requests.get('https://ipinfo.io?token=6a4407cf14d781')
    location_data = response.json()
    location = location_data.get('city', '台北')  # 如果無法獲取城市，預設為台北
except Exception as e:
    location = '台北'
    print(f"Error fetching location: {e}")

# 輸入用戶的特殊需求
special_request = input("請輸入您的特殊需求（例如：我想吃飯或麵，我想吃冷的）：")

# 確保 Groq 客戶端模組已正確導入
try:
    from groq import Groq

    # 創建 Groq 客戶端
    client = Groq(api_key="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")

    # 構建消息內容，並明確指示使用繁體中文
    message_content = f"""
    現在是{current_time.strftime('%Y年%m月%d日 %H:%M')}，我在{location}，季節是{season}，目前是{meal_time}時間。我想吃{special_request}。請問這個時間點推薦吃什麼？請顧慮營養均衡，並全部使用繁體中文回答，請將所有食物名稱翻譯成中文。
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
            temperature=0.3,  # 控制生成文本的多樣性和冒險程度
            max_tokens=500  # 控制生成文本的長度
        )

        # 打印生成的內容
        print(chat_completion.choices[0].message.content)

    except Exception as e:
        print(f"Error: {e}")
except ImportError as e:
    print(f"Error importing Groq: {e}")
