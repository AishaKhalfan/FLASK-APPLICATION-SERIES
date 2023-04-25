from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    #return 'Hello World!'
    return render_template('index.html')


@app.route('/about')
def about_page():
    #return 'About page'
    return render_template('about.html')


@app.route('/login')
def login_page():
    #return 'The login page'
    return render_template('login.html')


@app.route('/greet/<user>')
def greet(user):
    #return f'Hello {user}'
    return render_template('greet.html', user=user)

@app.route('/greet/<string:user>/<int:age>')
def greet_user(user, age):
    #return f'Hello {user} you are {age} years old'
    return render_template('greet_user.html', user=user, age=age)

@app.route('/contacts')
def contacts_page():
    #return '<h1>The contacts page</h1>'
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=True)