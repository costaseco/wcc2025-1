from flask import Flask, render_template, request

from application import get_Items, add_Item, complete_item
from data import init_db

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    list = get_Items()
    return render_template('index.html', list=list)

@app.route('/', methods=['POST'])
def add():
    item = request.form['item']
    add_Item(item)
    return index()

# presentation module (presentation.py)
@app.route('/complete', methods=['GET'])
def complete():
    id = request.args['id']
    complete_item(id)
    return index()

init_db()

if __name__ == '__main__':
    app.run()
