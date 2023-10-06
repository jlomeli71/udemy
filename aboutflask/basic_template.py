# This is a simple flask app
# the html file must be in a templates directory

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "Jose"
    my_list = ['oranges','apples','grapes', 'bananas', 'mangos']
    my_dict = {
        'hobbies': 'going to the movies',
        'likes': 'chocolate cake',
        'dislikes': 'sugar'
    }
    return render_template('basic.html', name=name, my_list=my_list, my_dict=my_dict)

if __name__ == '__main__':
    app.run(debug=True)
