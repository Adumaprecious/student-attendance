# Project: Student Attendance Management System (SAMS)

SDLC (Software Development Life Cycle) Explanation:
1. Planning:

Project Name: Student Attendance Management System (SAMS)

Objective: Build a web-based system to record, track, and analyze student attendance for schools or universities.

Scope: User authentication, student management, attendance marking, attendance reports.

2. Requirements Gathering:
Functional Requirements:

User registration and login (Admin / Lecturer)

Student record creation and management

Attendance marking (Present / Absent)

Attendance reports and summaries

Non-Functional Requirements:

Secure authentication

Data integrity and accuracy

Responsive and easy-to-use interface

3. Design:

System Architecture: Client-Server (Web-based)

Technologies: Python, Flask, SQLAlchemy, HTML/CSS, JavaScript

Database Design:

Users

id

username

email

password

role

Students

id

name

matric_number

Attendance

id

student_id

date

status

4. Implementation:

Backend: Flask REST API for users, students, and attendance

Frontend: HTML/CSS and JavaScript for user interface and API integration

5. Testing:

Unit testing for API endpoints

Integration testing for attendance workflows

6. Deployment:

Deploy on Heroku or AWS

Configure database and environment variables
