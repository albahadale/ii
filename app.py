import streamlit as st
import random

# إعدادات الصفحة
st.set_page_config(page_title="موقع نكت وونسة", page_icon="😂")

# ستايل CSS
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #ff4b4b; color: white; font-weight: bold; }
    .joke-text { font-size: 25px; text-align: center; padding: 20px; background: white; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); color: black; }
    </style>
    """, unsafe_allow_html=True) # تم تصحيح الكلمة هنا

st.title("😂 رادار النكت")
st.subheader("اضغط على الزر حتى تضحك!")

jokes = [
    "محشش يسأل خويه: ليش القطار مهم؟ قاله: لأن تحته خطين!",
    "مرة واحد عصبي وجعه ضرسه، راح للدكتور قاله اقلع كل سنوني وخلي هو وحده مثل الجلب!",
    "بخيل اشترى نص كيلو تفاح، لقى وحدة خربانة، رجعها وطلب نص كيلو ثاني!",
    "واحد محشش شاف اشارة 'ممنوع الوقوف' قام انبطح!",
    "عجوز راحت للمستشفى، قالولها لازم تسوين أشعة، قالتلهم: ما يصير تلفزيون؟"
]

if st.button('انطيني نكتة قوية!'):
    joke = random.choice(jokes)
    st.markdown(f'<div class="joke-text">{joke}</div>', unsafe_allow_html=True)
    st.balloons()
else:
    st.info("انتظر النكتة هنا...")
