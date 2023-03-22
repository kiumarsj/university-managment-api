from app import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fullname = db.Column(db.String(128), index=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=True)
    email = db.Column(db.String(120), index=True, unique=True)
    phone_number = db.Column(db.String(20), nullable=True)
    password_hash = db.Column(db.String(128))
    enrolled_courses = db.relationship('Course', secondary='enrollment', backref='students')
    grades = db.relationship('Grade', backref='student', lazy=True)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    description = db.Column(db.Text)
    capacity = db.Column(db.Integer)

enrollment = db.Table('enrollment',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'))
)

class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    grade = db.Column(db.Float)
