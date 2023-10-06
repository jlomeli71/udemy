# This is a dynamic routing flask app

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

if __name__ == '__main__':
    # app.run()
    app.run(debug=True)