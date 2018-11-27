# coding=utf-8
from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def hello_world():
    return 'hello world!!!!'

@app.route('/aaa/')
def test2():
    return 'hello wo'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
