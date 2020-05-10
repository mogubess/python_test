'''
Flaskだけにできることjinja2
templateシステムで、出力するhtmlに変数を渡すことができる
'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/echo/<thing>')
def echo(thing):
    return render_template('flask2.html', thing=thing)

app.run(port=9999, debug=True)
