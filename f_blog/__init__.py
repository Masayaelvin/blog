from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'b7f8824fbd4c68a1943bffeebd6c92cf'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
from f_blog import routes