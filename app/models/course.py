from models import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    term = db.Column(db.String)
    description = db.Column(db.Text)
    syllabus = db.Column(db.String) # URL
    sections = db.relationship('Section', back_populates='course')

class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    course = db.relationship('Course', back_populates='sections')
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'))
    teacher = db.relationship('Teacher', back_populates='courses')
    students = db.relationship(
        'Student',
        secondary='current_enrollments', 
        back_populates="current_courses"
    )
    assignments = db.relationship('GradedItem', backref='course')
