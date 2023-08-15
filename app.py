from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bmi(weight, height):
    height_meters = height / 100
    bmi = weight / (height_meters ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "過輕"
    elif bmi < 24:
        return "正常"
    elif bmi < 27:
        return "過重"
    elif bmi < 30:
        return "輕度肥胖"
    elif bmi < 35:
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

if __name__ == '__main__':
    app.run(debug=True)
