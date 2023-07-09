from .db import db

class User(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    gender = db.Column(db.String)
    email = db.Column(db.String)


class Student(User, db.Model):
    current_courses = db.relationship(
        'Section',
        secondary='current_enrollments', back_populates="students"
    )
    previous_courses = db.relationship(
        'Section',
        secondary='previous_enrollments'
    )
    year = db.Column(db.Integer)


class Teacher(User, db.Model):
    courses = db.relationship('Section', back_populates='teacher')
