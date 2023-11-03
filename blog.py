from flask import Flask, render_template, flash, url_for, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'b7f8824fbd4c68a1943bffeebd6c92cf'
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

if __name__ == '__main__':
    app.run(debug=True)