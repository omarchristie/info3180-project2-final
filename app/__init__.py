from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect


UPLOAD_FOLDER = './app/static/uploads'
TOKEN_SECRET = 'Thisissecret'

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://xlhgfdivrpfizb:a5c4c2c02697cc124ce2afc8fbe9f37cb16e65bb7549c9dae999324205f1bbfe@ec2-54-225-200-15.compute-1.amazonaws.com:5432/dee2ubeu8f74dg"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
csrf = CSRFProtect(app)

db = SQLAlchemy(app)


app.config.from_object(__name__)
filefolder = app.config['UPLOAD_FOLDER']
token_key = app.config['TOKEN_SECRET']
from app import views