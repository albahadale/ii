from flask import Flask, render_template_string
import random

app = Flask(__name__)

jokes = [
    "محشش يسأل خويه: ليش القطار مهم؟ قاله: لأن تحته خطين!",
    "عصبي وجعه ضرسه، راح للدكتور قاله اقلع كل سنوني وخلي هو وحده مثل الجلب!",
    "بخيل اشترى نص كيلو تفاح، لقى وحدة خربانة، رجعها وطلب نص كيلو ثاني!",
    "واحد محشش شاف اشارة 'ممنوع الوقوف' قام انبطح!",
    "عجوز راحت للمستشفى، قالولها لازم تسوين أشعة، قالتلهم: ما يصير تلفزيون؟"
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>نكت ع الماشي</title>
    <style>
        body { font-family: 'Tahoma', sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; color: white; }
        .card { background: white; color: #333; padding: 40px; border-radius: 25px; box-shadow: 0 15px 35px rgba(0,0,0,0.2); text-align: center; width: 85%; max-width: 450px; }
        h1 { color: #764ba2; margin-bottom: 20px; font-size: 28px; }
        .joke { font-size: 22px; margin: 30px 0; min-height: 80px; line-height: 1.5; }
        button { background: #ff4757; color: white; border: none; padding: 15px 30px; font-size: 18px; border-radius: 50px; cursor: pointer; transition: 0.3s; width: 100%; box-shadow: 0 4px 15px rgba(255, 71, 87, 0.3); }
        button:hover { background: #ff6b81; transform: translateY(-2px); }
    </style>
</head>
<body>
    <div class="card">
        <h1>😂 اضحك معنا</h1>
        <div class="joke">{{ joke }}</div>
        <button onclick="location.reload()">نكتة غيرها</button>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, joke=random.choice(jokes))

# هذا الجزء مهم لـ Vercel
app.debug = True
