#! ./bin/python3.8

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def welcome():
    if request.method == 'POST':
        return 'Hello World! via POST'
    elif request.method == 'GET':
        return 'Hello World! via GET'
    else:
        return 'Hello World!'

@app.route('/index', methods=['GET', 'POST'])
def html_page():
    return render_template('index.html')

@app.route('/form', methods=['POST', 'GET'])
def form():
    if request.method=='GET':
        return render_template('form01.html')
    elif request.method=='POST' and 'your_name' in request.form:
        name=request.form.get('your_name')
        print(name)
        return render_template('form01.html', yourname=name)


if __name__ == '__main__':
    app.run()
