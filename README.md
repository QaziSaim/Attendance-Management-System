# Student Attendance Management System

## Overview

The Student Attendance Management System is a comprehensive solution designed to streamline and manage student attendance efficiently. The system includes three panels: Student, Staff, and Head of Department (HOD). It allows for generating attendance sheets, as well as adding, removing, and updating courses, subjects, staff, students, and classes.

## Features

- **Student Panel**: 
  - View attendance records
  - View enrolled courses and subjects

- **Staff Panel**: 
  - Mark student attendance
  - Generate attendance sheets
  - Manage students (add, remove, update)
  - Manage subjects and courses

- **HOD Panel**: 
  - Oversee overall attendance records
  - Manage staff (add, remove, update)
  - Manage courses and classes
  - Generate comprehensive attendance reports

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/attendance-management-system.git
    ```
2. Navigate to the project directory:
    ```bash
    cd attendance-management-system
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```bash
    python app.py
    ```
2. Access the application in your web browser at `http://localhost:5000`.

## Project Structure

```plaintext
attendance-management-system/
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   ├── student.py
│   │   ├── staff.py
│   │   └── hod.py
│   ├── models.py
│   ├── templates/
│   │   ├── student/
│   │   ├── staff/
│   │   └── hod/
│   └── static/
├── requirements.txt
├── README.md
└── app.py
