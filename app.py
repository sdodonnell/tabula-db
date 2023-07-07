from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<p>Hello, world!</p>"

@app.route('/user/<int:id>')
def user(id):
    return f"<p>User number {id}</p>"

@app.route('/dashboard')
def dashboard():
    return "<h1>Dashboard</h1>"
