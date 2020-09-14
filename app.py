from flask import Flask
from flask import request
from flask import render_template
from urllib import parse

app = Flask(__name__)

@app.route('/')
def index():
    if request.args.get('expr'):
        answer = eval(parse.unquote(request.full_path.split('expr=')[1]))
        return render_template('index.html', answer=answer)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()