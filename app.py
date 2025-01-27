from flask import Flask, render_template, request

app = Flask(__name__)

list = ['Eggs', 'Milk', 'Bread', 'Butter']

@app.route('/', methods=['GET'])
def index():  # put application's code here
    return render_template('index.html', list=list)

@app.route('/', methods=['POST'])
def add():
    list.append(request.form['item'])
    return index()

@app.route('/complete', methods=['GET'])
def complete():
    value = request.args['index']
    list.pop(int(value))
    return index()

if __name__ == '__main__':
    app.run()
