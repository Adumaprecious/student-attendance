from flask import Flask, request, jsonify
from models import db, User, Student, Attendance

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sams.db'
db.init_app(app)

@app.route('/users', methods=['POST'])
def create_user():
    user = User(
        username=request.json['username'],
        email=request.json['email'],
        password=request.json['password'],
        role=request.json['role']
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/students', methods=['POST'])
def create_student():
    student = Student(
        name=request.json['name'],
        matric_number=request.json['matric_number']
    )
    db.session.add(student)
    db.session.commit()
    return jsonify({'message': 'Student added successfully'}), 201

@app.route('/attendance', methods=['POST'])
def mark_attendance():
    attendance = Attendance(
        student_id=request.json['student_id'],
        date=request.json['date'],
        status=request.json['status']
    )
    db.session.add(attendance)
    db.session.commit()
    return jsonify({'message': 'Attendance recorded successfully'}), 201
