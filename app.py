from flask import Flask, render_template, request
import threading
import time
import requests

app = Flask(__name__)

def calculate_bmi(weight, height):
    height_meters = height / 100
    bmi = weight / (height_meters ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "過輕"
    elif 18.5 <= bmi < 24:
        return "正常"
    elif 24 <= bmi < 27:
        return "過重"
    elif 27 <= bmi < 30:
        return "輕度肥胖"
    elif 30 <= bmi < 35:
        return "中度肥胖"
    else:
        return "重度肥胖"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        bmi = calculate_bmi(weight, height)
        interpretation = interpret_bmi(bmi)
        return render_template('result.html', bmi=bmi, interpretation=interpretation)
    return render_template('index.html')

def keep_alive():
    while True:
        try:
            url = 'https://bmi-n182.onrender.com'  # 請替換成您的應用程式 URL
            response = requests.get(url)
            print('Keep-alive request sent.')
        except Exception as e:
            print('Error sending keep-alive request:', e)
        time.sleep(600)  # 每10分鐘發送一次 keep-alive 請求

if __name__ == '__main__':
    # 啟動定時的 keep-alive 請求
    keep_alive_thread = threading.Thread(target=keep_alive)
    keep_alive_thread.start()
    
    # 啟動Flask應用
    app.run(debug=True)
