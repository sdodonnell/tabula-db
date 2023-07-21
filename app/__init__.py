from flask import Flask
from flask_sqlalchemy import SQLAlchemy

tabula = Flask(__name__)
tabula.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.sqlite'
db = SQLAlchemy()
db.init_app(tabula)

with tabula.app_context():
    db.create_all()

@tabula.route('/')
def hello_world():
    return "<p>Hello, world!</p>"

@tabula.route('/user/<int:id>')
def user(id):
    return f"<p>User number {id}</p>"

@tabula.route('/dashboard')
def dashboard():
    return "<h1>Dashboard</h1>"

from app import models, controller
