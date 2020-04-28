#! ./bin/python3.8

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def bmi_calc_html():
    bmi_table = {
        1: 'Severe Thinness	',
        2: 'Moderate Thinness',
        3: 'Mild Thinness',
        4: 'Normal',
        5: 'Overweight',
        6: 'Obese Class I',
        7: 'Obese Class II',
        8: 'Obese Class III',
    }
    if request.method == 'GET':
        return render_template('bmi_calc.html')
    elif request.method == 'POST':
        try:
            height = int(request.form.get('height'))
            weight = int(request.form.get('weight'))
            bmi = bmi_calc(weight, height)
            if bmi < 16:
                obesity = bmi_table[1]
            elif bmi >= 16 and bmi < 17:
                obesity = bmi_table[2]
            elif bmi >= 17 and bmi < 18.5:
                obesity = bmi_table[3]
            elif bmi >= 18.5 and bmi < 25:
                obesity = bmi_table[4]
            elif bmi >= 25 and bmi < 30:
                obesity = bmi_table[5]
            elif bmi >= 30 and bmi < 35:
                obesity = bmi_table[6]
            elif bmi >= 35 and bmi < 40:
                obesity = bmi_table[7]
            elif bmi >= 40:
                obesity = bmi_table[8]
            else:
                obesity = 'under construction!'
            return render_template('bmi_calc.html', bmi=bmi, obesity=obesity)
        except:
            return 'Values you have introduced are wrong. Please try again', render_template('bmi_calc.html')
    else:
        return 'Oops, something went wrong'


def bmi_calc(weight, height):
    return round(weight / ((height / 100) ** 2), 2)


if __name__ == '__main__':
    app.run()
