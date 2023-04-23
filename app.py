from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/about')
def about_page():
    return 'The about page'

@app.route('/login')
def login_page():
    return 'The login page'

@app.route('/greet/<user>')
def greet(user):
    return f'Hello {user}'

if __name__ == '__main__':
    app.run(debug=True)