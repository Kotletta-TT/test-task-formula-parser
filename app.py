from flask import Flask
from flask import request
from flask import render_template
from urllib import parse
import math

app = Flask(__name__)
EXPRESSION_PATH_INDEX = 1


@app.route('/')
def index():
    answer = None
    if request.args.get('expr'):
        answer = get_answer(request.full_path)
    return render_template('index.html', answer=answer)


def get_answer(expression):
    return eval(parse.unquote(expression.split('expr=')[EXPRESSION_PATH_INDEX]))


if __name__ == '__main__':
    app.run()
