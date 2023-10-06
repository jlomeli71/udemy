
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/info')
def info():
    return '<h1>This is some information about ...</h1>'

@app.route('/contact/<name>')
def contact(name):
    return f'<h1>This is the contact information from {name}</h1>'

@app.route('/puppy/<name>')
def puppy(name):
    if name[-1] != 'y':
        name = name + 'y'
    else:
        name = name.replace('y', 'iful')         
    return f'<h1>Your puppy latin name is {name}</h1>'


if __name__ == '__main__':
    # app.run()
    app.run(debug=True)