from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

app = Flask(__name__)

app.secret_key = 'secret'

posts=[
    {
        'id':1,
        'title':'What is Flask?',
        'content':'Flask is a micro web framework written in Python'
    },
    {
    'id':2,
    'title':'Python is fun',
    'content':'Python is a programming language'
    },
    {
    'id':3,
    'title':'Is Flask good for a begginer?',
    'content':'Yes it is'
    },
    {
    'id':4,
    'title':'Coding is hard!',
    'content':'No it is not'
    },
]

class signupForm(FlaskForm):
    username = StringField(label='Username',validators=[DataRequired(message="username should not be blank"),
                                                          Length(min=5, max=25)])
    email= StringField(label='Email', validators=[DataRequired(message="email should not be blank"), 
                                                  Length(min=5, max=45, message="email should be between 5 and 45 characters")])
    password = PasswordField(label='Password', validators=[DataRequired(message="password should not be blank"),
                                                           Length(min=5, max=12, message="password should be between 5 and 12 characters")])
    
    confirm_password= PasswordField(label='Confirm Password', validators=[DataRequired(message="password should not be blank"), 
                                                                          Length(min=5, max=12, message="password should be between 5 and 12 characters"), 
                                                                          EqualTo('password', message="passwords should match")])
    submit = SubmitField(label='Sign Up')    

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(message="email should not be blank"),
                                                         Length(min=5, max=25)])
    password = PasswordField(label='Password', validators=[DataRequired(message="password should not be blank"),
                                                           Length(min=5, max=12, message="password should be between 5 and 12 characters")])
    submit = SubmitField(label='Login')


@app.route('/')
def index():
    #return 'Hello World!'
    title = 'Home Page'
    context = {
        'title':title,
        'posts': posts
    }
    return render_template('index.html', **context)

@app.route('/signup', methods=['GET', 'POST'])
def signup_page():
    form= signupForm()

    if request.method == 'POST':
        return 'Form posted'

    context= {
        'form': form
    }

    return render_template('signup.html', **context)

@app.route('/about')
def about_page():
    #return 'About page'
    title = 'About Page'
    context = {
        'title': title,
        'posts': posts
    }
    return render_template('about.html', **context)

@app.route('/login')
def login_page():
    #return 'The login page'
    
    title = 'Login Page'
    form= LoginForm()
    context = {
        'title': title,
        'form': form
    }
    return render_template('login.html', **context)

@app.route('/greet/<user>')
def greet(user):
    #return f'Hello {user}'
    #return render_template('greet.html', user=user)
    title = 'Greet Page'
    context = {
        'title': title,
        'user': user
    }  
    return render_template('greet.html', **context)


@app.route('/greet/<string:user>/<int:age>')
def greet_user(user, age):
    #return f'Hello {user} you are {age} years old'
    #return render_template('greet_user.html', user=user, age=age)
    title = 'Greet User Page'
    context = {
        'title': title,
        'user': user,
        'age': age
    }
    return render_template('greet_user.html', **context)


@app.route('/contacts')
def contacts_page():
    #return '<h1>The contacts page</h1>'
    title = 'Contacts Page'
    context = {
        'title': title
    }
    return render_template('contacts.html', **context)


if __name__ == '__main__':
    app.run(debug=True)