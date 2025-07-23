from flask import Flask

# 'app' ဆိုတဲ့ variable ကို gunicorn က ရှာပြီး run မှာဖြစ်ပါတယ်
app = Flask(__name__)

@app.route('/')
def home():
    # ဒီစာသားကို သင်၏ website မှာ မြင်ရပါလိမ့်မယ်
    return "Hello Zonc! This is the first successful deployment."

# ဒီအပိုင်းက သင်၏ local computer မှာ တိုက်ရိုက် run စမ်းကြည့်ဖို့အတွက်ပါ
# Render က ဒီအပိုင်းကို အသုံးမပြုပါဘူး
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)