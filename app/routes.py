from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Whisllay'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day here!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'That physician was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)