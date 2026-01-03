# from flask import Flask, render_template
# from flask_wtf import FlaskForm
# from wtforms import StringField,PasswordField,SubmitField
# from wtforms.validators import DataRequired, Email, ValidationError

# app = Flask(__name__)

# class RegisterForm(FlaskForm):
#     name = StringField("Name",validators = [DataRequired()])
#     email = StringField("Email",validators = [DataRequired(), Email()])
#     password = PasswordField("Password",validators = [DataRequired()])
#     submit = SubmitField("Register")
    

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/register')
# def register():
#     return render_template('register.html')

# @app.route('/login')
# def login():
#     return render_template('login.html')

# @app.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html')

# if __name__ == '__main__':
#     app.run(debug = True)

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Register")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    return render_template('register.html', form=form)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)