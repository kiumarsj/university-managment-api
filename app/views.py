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
