from flask import request
from app import tabula, db
from app.models import Student, Teacher


@tabula.post('/add-user')
def add_user():
    user = Teacher(
        first_name=request.form['first_name'],
        last_name=request.form['last_name'],
        email=request.form['email'],
        pronouns=request.form['pronouns'],
    )
    db.session.add(user)
    db.session.commit()
    return f'Successfully added user {user.id}\n'


def update_user():
    pass


def delete_user():
    pass


def get_user():
    pass


@tabula.get('/all-students')
def get_all_students():
    students = db.session.execute(db.select(Student)).scalars().all()
    json = [{
        "firstName": student.first_name,
        "lastName": student.last_name,
        "email": student.email,
        "pronouns": student.pronouns
    } for student in students]
    return json
