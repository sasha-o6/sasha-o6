from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    return f"Osipov Oleksander TI-81" #@sasha_o6

@app.route('/first')
def first():
    a = None
    b = ' 86 '
    c = 12
    return f"{a} {b} {c}"

if __name__ == '__main__':
    app.run('0.0.0.0')
