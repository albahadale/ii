from flask import Flask, render_template_string
import random
import os

app = Flask(__name__)

jokes = [
    "مرة واحد اشترى ساعة طلعت ضيقة، سواها نص ساعة.",
    "واحد سأل محشش: شنو الفرق بين الأسبوع والموس؟ قال: الموس فيه حلاقة!",
    "بخيل تزوج، راح لشهر العسل وحده!",
    "عصبي وجعه ضرسه، راح للدكتور قاله: اقلع كل سنوني وخلي هو وحده مثل الجلب!"
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>موقع نكت</title>
    <style>
        body { font-family: sans-serif; background: #f4f4f9; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .card { background: white; padding: 30px; border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); text-align: center; }
        button { background: #007bff; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="card">
        <h1>😂 نكتة عشوائية</h1>
        <p style="font-size: 1.5rem;">{{ joke }}</p>
        <button onclick="location.reload()">نكتة ثانية</button>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, joke=random.choice(jokes))

if __name__ == '__main__':
    # مهم جداً للسيرفرات الخارجية
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
