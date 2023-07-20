from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.sqlite'
db = SQLAlchemy(app)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def hello_world():
    return "<p>Hello, world!</p>"

@app.route('/user/<int:id>')
def user(id):
    return f"<p>User number {id}</p>"

@app.route('/dashboard')
def dashboard():
    return "<h1>Dashboard</h1>"

from app import controller, models
