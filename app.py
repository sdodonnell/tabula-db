from flask import Flask, request
from models.db import db
from models.user import User, Teacher, Student
from models.item import GradedItem, Submission
from models.course import Course, Section
from models.associations import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.sqlite'
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

@app.post('/add-user')
def add_user():
    user = Teacher(
        first_name = request.form['first_name'],
        last_name = request.form['last_name'],
        email = request.form['email']
    )
    db.session.add(user)
    db.session.commit()
    return f'Successfully added user {user.id}\n'
