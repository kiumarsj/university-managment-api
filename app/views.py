from app import app, db, mail
from app.models import Student, Course, Grade
from flask import jsonify, request, url_for
from flask_mail import Message

# Students
@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([student.to_dict() for student in students])

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get_or_404(id)
    return jsonify(student.to_dict())

@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json() or {}
    if 'name' not in data or 'email' not in data or 'password' not in data:
        return jsonify({'message': 'Missing required parameters.'}), 404

# Courses
@app.route('/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return jsonify([course.to_dict() for course in courses])

@app.route('/courses/<int:id>', methods=['GET'])
def get_course(id):
    course = Course.query.get_or_404(id)
    return jsonify(course.to_dict())

@app.route('/courses', methods=['POST'])
def create_course():
    data = request.get_json() or {}
    if 'name' not in data or 'code' not in data or 'description' not in data:
        return jsonify({'message': 'Missing required parameters.'}), 404

# Grades
@app.route('/grades', methods=['GET'])
def get_grades():
    grades = Grade.query.all()
    return jsonify([grade.to_dict() for grade in grades])

@app.route('/grades/<int:id>', methods=['GET'])
def get_grade(id):
    grade = Grade.query.get_or_404(id)
    return jsonify(grade.to_dict())

@app.route('/grades', methods=['POST'])
def create_grade():
    data = request.get_json() or {}
    if 'student_id' not in data or 'course_id' not in data or 'grade' not in data:
        return jsonify({'message': 'Missing required parameters.'}), 404
    
# Email
@app.route('/email', methods=['POST'])
def send_email():
    data = request.get_json() or {}
    if 'subject' not in data or 'body' not in data or 'recipient' not in data:
        return jsonify({'message': 'Missing required parameters.'}), 404

    msg = Message(data['subject'],
                    sender=app.config['MAIL_USERNAME'],
                    recipients=[data['recipient']])
    msg.body = data['body']
    mail.send(msg)
    return jsonify({'message': 'Email sent.'})
