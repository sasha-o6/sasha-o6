from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/first')
def hello():
    a = None
    b = ' 86 '
    c = 12
    
    return f"{a},{b},{c}"

if __name__ == '__main__':
    app.run('0.0.0.0')
