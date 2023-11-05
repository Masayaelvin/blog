from flask import render_template, flash, url_for, redirect
from f_blog.forms import RegistrationForm, LoginForm
from f_blog.models import User, Post
from f_blog import app
posts = [
    {
        'author': 'Wayne wonder Asamba',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Masaya Elvin',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'

    }
]
@app.route('/')
def home():
        return render_template('home.html', posts=posts)

@app.route('/about')
def about():
        return render_template('about.html' , title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
        form= RegistrationForm()
        if form.validate_on_submit():
            flash(f'Account created for {form.username.data}!','success')
            return redirect(url_for('home'))
        return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
        form= LoginForm()
        if form.validate_on_submit():
            if form.email.data == 'masayaelvin@gmail.com' and form.password.data == 'masaya':
                flash('You have been logged in!', 'success')
                return redirect(url_for('home'))
            else:
                flash('incorrect password or  username', 'danger')
            
        return render_template('login.html', title='Login', form=form)
