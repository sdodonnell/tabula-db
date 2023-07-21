from app import db

#
# Users
#

class User(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    pronouns = db.Column(db.String)
    email = db.Column(db.String)

    # def _init(self, first_name, last_name, pronouns, email):
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.pronouns = pronouns
    #     self.email = email
    
    def save(self):
        db.session.add(self)
        db.session.commit()

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


#
# Item
#

class GradedItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    course_id = db.Column(db.Integer, db.ForeignKey('section.id'))
    description = db.Column(db.Text)
    file = db.Column(db.String) # URL
    due_date = db.Column(db.DateTime)
    created_date = db.Column(db.DateTime)
    submissions = db.relationship('Submission', back_populates='assignment')

class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.String)
    submitted_date = db.Column(db.DateTime)
    feedback = db.Column(db.Text)
    assignment_id = db.Column(db.Integer, db.ForeignKey('graded_item.id'))
    assignment = db.relationship('GradedItem', back_populates='submissions')

#
# Course
#

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

#
# Associations
#
current_enrollments = db.Table(
    'current_enrollments',
    db.Column('section_id', db.Integer, db.ForeignKey('section.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('student.id'), primary_key=True),
)

previous_enrollments = db.Table(
    'previous_enrollments',
    db.Column('section_id', db.Integer, db.ForeignKey('section.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('student.id'), primary_key=True),
)

# Only include these if we want to allow a section to be taught by multiple teachers at once.
# currently_teaching = db.Table(
#     'currently_teaching',
#     db.Column('section_id', db.Integer, db.ForeignKey('section.id'), primary_key=True),
#     db.Column('user_id', db.Integer, db.ForeignKey('teacher.id'), primary_key=True),
# )

# previously_teaching = db.Table(
#     'previously_teaching',
#     db.Column('section_id', db.Integer, db.ForeignKey('section.id'), primary_key=True),
#     db.Column('user_id', db.Integer, db.ForeignKey('teacher.id'), primary_key=True),
# )
