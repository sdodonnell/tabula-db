from .db import db

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
