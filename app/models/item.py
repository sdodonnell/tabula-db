from models import db

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
